
# 🍜 Async Port Scanner 🍜

Welcome to the **Async Port Scanner**, a blazing-fast, lightweight, and deliciously simple port scanner built with Python and `asyncio`! 🚀 This project is designed to help you scan ports asynchronously with up to **1000 parallel tasks** at once. It's like ordering 1000 pizzas 🍕 at the same time—efficient and satisfying! 😄


## 🥡 Features

- **Asynchronous Scanning**: Uses Python's `asyncio` for super-fast port scanning. Think of it as cooking multiple dishes at once! 🍳
- **Customizable Port Range**: Specify the starting and ending ports to scan exactly what you need. 🎯
- **Efficient Task Management**: Limits to 1000 parallel tasks at a time to avoid overloading your system. 🛠️
- **User-Friendly Input**: Interactive prompts guide you through entering the target IP and port range. 🧑‍🍳
- **No Dependencies**: Uses only Python's standard library—no extra ingredients required! 🥕

---

## 🥖 How to Use

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/bitkeyhash/Async-Port-Scanner.git && cd Async-Port-Scanner
```

### 2️⃣ Install Requirements

Make sure you have Python 3.8 or higher installed. Then install dependencies (if any):

```bash
pip install -r requirements.txt
```

> Note: This script uses only Python's standard library, so no additional libraries are required! 🎉

### 3️⃣ Run the Script

Fire up the scanner by running:

```bash
python aps.py
```

You'll be prompted to enter:
- The target IP address (e.g., `192.168.1.1`)
- The starting port (e.g., `1`)
- The ending port (e.g., `65535`)

The script will then scan all ports in the specified range and display which ones are open! 🛳️

---

## 🥗 Example Output

```plaintext
Welcome to the Async Port Scanner!
Enter the target IP address: 192.168.1.1
Enter the starting port (e.g., 1): 20
Enter the ending port (e.g., 100)

Scanning IP: 192.168.1.1 from port 20 to 100...

[OPEN] Port 22 is open on 192.168.1.1
[OPEN] Port 80 is open on 192.168.1.1

Scan complete!
```

---

## 🌮 Requirements

This script requires **Python 3.8+**.

Install Python dependencies (if needed) using:

```bash
pip install -r requirements.txt
```

---

## 🍩 How It Works (Under the Hood)

Here’s how this tasty scanner operates:

1. **Asynchronous Magic**:
   - Uses `asyncio` to handle multiple connections simultaneously.
   - Limits concurrency to **200 tasks** using a semaphore (`asyncio.Semaphore`)—like having only so many burners on your stove! 🔥

2. **Port Scanning**:
   - Attempts to connect to each port in the specified range.
   - If successful, it reports the port as "open." Otherwise, it silently skips closed ports.

3. **Interactive Input**:
   - Prompts you for the target IP address and port range.
   - Validates inputs to ensure everything is within proper limits (ports between `1-65535`).

---

## 🧁 Why Use This?

- You're hungry for speed ⚡.
- You want something lightweight with no unnecessary dependencies 🥗.
- You love Python and want an easy-to-understand script 🐍.
- You need a quick tool for network troubleshooting or ethical hacking 🍕.

---

## 🍔 Contributing

Got some spicy ideas 🌶️? Found a bug 🐞? Feel free to contribute!

1. Fork this repository 🍴.
2. Create a new branch (`git checkout -b feature/my-feature`).
3. Commit your changes (`git commit -m "Add my feature"`).
4. Push your branch (`git push origin feature/my-feature`).
5. Open a pull request 🚀.

---

## ☕ License

This project is licensed under the MIT License—because sharing is caring! ❤️ Feel free to use, modify, and distribute this script as you like.

---

## 🍣 A Final Note

This tool is intended for **ethical purposes only** 🙏—always ensure you have permission before scanning any network or device.

Now go ahead and scan responsibly... Bon appétit! 🍽️

---

Let me know if you'd like me to tweak anything further or add more flair! 😊

---
