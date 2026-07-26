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
Network-Recon-Toolkit/
│
├── core/
│   ├── dns_lookup.py
│   ├── dns_records.py
│   ├── host_info.py
│   ├── ip_info.py
│   ├── ping_tool.py
│   ├── port_scanner.py
│   └── whois_lookup.py
│
├── handlers/
│   ├── dns_handler.py
│   ├── host_info_handler.py
│   ├── ip_handler.py
│   ├── ip_info_handler.py
│   ├── ping_handler.py
│   ├── port_scanner_handler.py
│   └── whois_handler.py
│
├── utils/
│   ├── common_ports.py
│   ├── constants.py
│   ├── formatter.py
│   └── validators.py
│
├── main.py
├── menu.py
├── requirements.txt
└── README.md

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

⚠️ Disclaimer

This tool is created for educational purposes and authorized security testing only.

Do not use this tool against systems or networks without permission.

The developer is not responsible for any misuse of this toolkit.

👨‍💻 Author

Xenover