# 🔍 Network Recon Toolkit

A Python-based Network Reconnaissance Toolkit designed for learning cybersecurity concepts and performing authorized network information gathering.

## 🚀 Features

- 🌐 Domain to IP Lookup
- 🔄 Reverse DNS Lookup
- 📡 DNS Records Lookup
- 📋 WHOIS Information
- 📶 Ping Tool
- 🖥️ Host Information
- 🔍 Port Scanner
- 🌍 IP Information Lookup

## 🛠️ Technologies Used

- Python
- Socket Programming
- DNS Resolution
- Network Reconnaissance Concepts

## 📂 Project Structure

```text
Network-Recon-Toolkit
│
├── core/
│   ├── __init__.py
│   │
│   ├── dns_lookup.py
│   ├── dns_records.py
│   ├── host_info.py
│   ├── ip_info.py
│   ├── ping_tool.py
│   ├── port_scanner.py
│   ├── whois_lookup.py
│   │
│   ├── asn_lookup.py
│   ├── banner_grabber.py
│   ├── reverse_dns.py
│   ├── security_headers.py
│   ├── robots_analyzer.py
│   └── sitemap_finder.py
│
│
├── handlers/
│   ├── __init__.py
│   │
│   ├── dns_handler.py
│   ├── host_info_handler.py
│   ├── ip_handler.py
│   ├── ip_info_handler.py
│   ├── ping_handler.py
│   ├── port_scanner_handler.py
│   ├── whois_handler.py
│   │
│   ├── asn_lookup_handler.py
│   ├── banner_grabber_handler.py
│   ├── reverse_dns_handler.py
│   ├── security_headers_handler.py
│   ├── robots_analyzer_handler.py
│   └── sitemap_finder_handler.py
│
│
├── utils/
│   ├── __init__.py
│   ├── validators.py
│   ├── formatter.py
│   ├── constants.py
│   ├── exceptions.py
│   ├── logger.py
│   └── http_client.py
│
│
├── tests/
│   ├── __init__.py
│   ├── test_dns.py
│   ├── test_ip.py
│   ├── test_scanner.py
│   └── test_security_headers.py
│
│
├── docs/
│   ├── architecture.md
│   ├── modules.md
│   └── usage.md
│
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
│
├── logs/
│   └── .gitkeep
│
│
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── CHANGELOG.md
├── CONTRIBUTING.md
├── main.py
└── menu.py

⚙️ Installation
1. Clone the repository

git clone https://github.com/xenoverhubofficial09-netizen/Network-Recon-Toolkit.git

2. Go to project folder

cd Network-Recon-Toolkit

3. Install dependencies

pip install -r requirements.txt

▶️ Usage

Run the toolkit:
python main.py

📦 Dependencies

This project uses:

requests
dnspython
python-whois
colorama
pyfiglet

All dependencies are listed in:
requirements.txt

🛡️ Legal Disclaimer

Network Recon Toolkit is developed strictly for:

Educational purposes
Authorized security testing
Cybersecurity research
Network analysis in controlled environments

Users must have proper authorization before performing any security assessment.
Do not use this toolkit against systems, networks, or websites without explicit permission.
The developer assumes no responsibility for misuse, illegal activity, or unauthorized access attempts.
Use responsibly and follow applicable laws and regulations.

👨‍💻 Author

Xenover !

Cybersecurity Student | Python Developer | Security Tool Builder
