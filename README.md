## General Programming

Just a collection of random programming stuff.

<br>

### 🔎 enumSubs – Subdomain Enumeration Script

`enumSubs` is a script that integrates multiple subdomain enumeration tools: **findomain**, **subfinder**, **sublist3r**, and **amass**.

![Screenshot-2](https://github.com/user-attachments/assets/cb3c599a-f8e8-4588-b234-634f5cee25da)

<br>

🚀 Usage

To enumerate a single domain:
```
python3 enumSubs.py domain.com
```

To enumerate multiple domains from a file:
```
python3 enumSubs.py -f domains.txt
```

<br>

| Flag    | Usage |
| -------- | ------- |
| -h | Displays help and available options |
| -f <file> | Enumerates multiple domains from a file  |
| -a | Includes Amass for deeper enumeration |
