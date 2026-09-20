# SecureScan

A basic security scanner for websites you own or have permission to test.

## Features
- Check security headers (CSP, HSTS, X-Frame-Options)
- Check SSL expiry & issuer
- Check cookie flags (Secure, HttpOnly, SameSite)
- Simple reflected XSS test (own domains only)
- Export reports as JSON/PDF

## Tech Stack
Python 3, FastAPI, requests, Rich, Jinja2

## Installation
pip install -r requirements.txt
uvicorn app.main:app --reload

## Ethical Use
Only scan your own assets, labs, CTFs, or targets with written permission.
