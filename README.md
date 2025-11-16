# DirFinder

**DirFinder** is a lightweight **directory brute-forcing tool** written in **Python**.
It helps you discover hidden directories and files on a target web server using a **custom wordlist** — perfect for security testing, pentesting, or analyzing a website’s attack surface.

---

## 🚀 Features

- Scans and enumerates directories on a given target URL
- Handles HTTP status codes and connection errors gracefully
- Simple text-based user interface
- Supports custom wordlists
- Works on **Windows**, **Linux**, and **macOS**

---

## ⚙️ Requirements

Make sure you have **Python 3.x** installed along with the `requests` module.

### Install dependencies:

```bash
pip install requests
```

---

## 📂 Usage

1. Clone or download this repository:

   ```bash
   git clone https://github.com/Christian-Lancini/DirFinder.git
   cd DirFinder
   ```

2. Run the script:

   ```bash
   python main.py
   ```

3. Follow the interactive menu:

   ```
   1 - Start scan
   2 - Exit
   ```

4. Enter:

   - The target URL (e.g., `https://example.com`)
   - The path to your wordlist (e.g., `wordlists/common.txt`)

   Ex. Wordlist:

   ```
   home
   admin
   ...
   ```

---

## 📘 Example Output

```
[*] Directory found: https://example.com/admin
[!] Access denied: https://example.com/private
[?] https://example.com/tmp: 302
[STOP] Scan completed!
```

---

## 🧰 Project Structure

```
DirFinder/
├── main.py        # Main script
├── wordlists/          # (Optional) Folder for your wordlists
│   └── common.txt
└── README.md           # This file
```

---

## ⚠️ Disclaimer

> ⚠️ **Ethical use only**
> DirFinder is designed for **educational** and **authorized security testing** purposes only.
> Do **not** use this tool against systems you don’t own or have explicit permission to test.
> Unauthorized use may violate laws and regulations.

---

---

## 👨‍💻 Author

📧 Contact: [[your-email@example.com](mailto:chrilanci00@gmail.com)]

---
