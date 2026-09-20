<div align="center">

### 🔐 SecureScan

**A lightweight security scanner for websites you own or have permission to test.**

Built with Python • Made by [@annisadanish](https://github.com/annisadanish)

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Made by](https://img.shields.io/badge/Made%20by-@annisadanish-cyan?style=for-the-badge)](https://github.com/annisadanish)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## ✨ Features

| Feature | Description |
|---|---|
| 🛡️ Security Headers | Detects missing headers (CSP, HSTS, X-Frame-Options, etc.) |
| 🔒 SSL Check | Shows issuer, expiry date, and days remaining |
| 🍪 Cookie Flags | Audits Secure and HttpOnly flags |
| 📄 JSON Export | Save report as JSON for automation |
| 🎨 Pretty Output | Colored terminal output via rich |

---

## 🚀 Installation

    git clone git@github.com:annisadanish/securescan.git
    cd securescan
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

---

## 💻 Usage

    python main.py <domain>
    python main.py <domain> --json

Examples:

    python main.py example.com
    python main.py example.com --json

---

## 📸 Sample Output

    Scanning example.com ...

    HTTP Status: 200
    Security Headers: ...
    SSL Certificate: ...
    Cookies: ...

    — SecureScan by @annisadanish —

---

## ⚖️ Ethical Use

This tool is built for **educational purposes** and **authorized testing only**.

Only scan:

- Your own websites
- Lab environments
- CTF challenges
- Targets with **written permission**

**Never** scan websites without authorization.

---

<div align="center">

**Made with 🖤 by [Annisa Danish](https://github.com/annisadanish)**

⭐ Star this repo if you find it useful!

</div>
