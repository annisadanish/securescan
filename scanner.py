"""
SecureScan
Author: Annisa Danish (@annisadanish)
GitHub: https://github.com/annisadanish/securescan

Educational security scanner. Only scan assets you own
or have permission to test.
"""

import ssl
import socket
import requests
from datetime import datetime, timezone
from urllib.parse import urlparse


SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy",
]


def normalize_url(target):
    if not target.startswith(("http://", "https://")):
        target = "https://" + target
    return target


def check_headers(url):
    result = {
        "url": url,
        "status_code": None,
        "headers_found": {},
        "headers_missing": [],
        "error": None,
    }
    try:
        resp = requests.get(
            url,
            timeout=10,
            allow_redirects=True,
            headers={"User-Agent": "SecureScan/1.0 (educational)"},
        )
        result["status_code"] = resp.status_code
        for h in SECURITY_HEADERS:
            if h in resp.headers:
                result["headers_found"][h] = resp.headers[h]
            else:
                result["headers_missing"].append(h)
    except requests.RequestException as e:
        result["error"] = str(e)
    return result


def check_ssl(hostname, port=443):
    result = {
        "hostname": hostname,
        "issuer": None,
        "subject": None,
        "expires": None,
        "days_left": None,
        "error": None,
    }
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((hostname, port), timeout=10) as sock:
            with ctx.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()

        result["issuer"] = dict(x[0] for x in cert["issuer"])
        result["subject"] = dict(x[0] for x in cert["subject"])
        expiry_str = cert["notAfter"]
        expiry = datetime.strptime(expiry_str, "%b %d %H:%M:%S %Y %Z")
        expiry = expiry.replace(tzinfo=timezone.utc)
        result["expires"] = expiry.isoformat()
        result["days_left"] = (expiry - datetime.now(timezone.utc)).days
    except Exception as e:
        result["error"] = str(e)
    return result


def check_cookies(url):
    result = {"cookies": []}
    try:
        resp = requests.get(
            url,
            timeout=10,
            allow_redirects=True,
            headers={"User-Agent": "SecureScan/1.0 (educational)"},
        )
        for c in resp.cookies:
            result["cookies"].append({
                "name": c.name,
                "secure": c.secure,
                "httponly": "HttpOnly" in str(c._rest) if hasattr(c, "_rest") else None,
                "domain": c.domain,
            })
    except requests.RequestException as e:
        result["error"] = str(e)
    return result


def scan(target):
    url = normalize_url(target)
    hostname = urlparse(url).hostname

    return {
        "target": target,
        "url": url,
        "headers": check_headers(url),
        "ssl": check_ssl(hostname),
        "cookies": check_cookies(url),
    }
