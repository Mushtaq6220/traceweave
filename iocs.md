# 🔍 Indicators of Compromise (IOCs)

All indicators from **Operation Crimson Velvet** categorized and formatted for defensive integration (SIEM, EDR, Firewall, DNS blocklist).

---

## 1. Network Indicators

| Type | Value (Defanged) | Protocol / Port | Threat Association | Confidence |
| :--- | :--- | :--- | :--- | :--- |
| **IPv4** | `192.168.99[.]50` | TCP 8000 | Payload Delivery Staging Server | High |
| **IPv4** | `192.168.99[.]50` | TCP 443 | C2 Command & Control / Exfiltration | High |
| **Domain** | `cdn-update-auth[.]com` | HTTPS | Primary C2 Domain | High |
| **URL** | `http://192.168.99[.]50:8000/stage2[.]bin` | HTTP | Malicious Second-Stage Stager | High |
| **URL** | `http://cdn-update-auth[.]com/api/v1/sync` | HTTPS | C2 Polling Endpoint | High |

---

## 2. File & Hash Indicators

| Filename | SHA-256 Hash | File Type | Path Staged / Observed | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Invoice_Q3.docm` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | MS Word (Macro) | `C:\Users\jdoe\Downloads\` | Initial Phishing Lure |
| `stage2.bin` | `5f4dcc3b5aa765d61d8327deb882cf992b95990a9151374abd8ff14c810d8a9e` | Shellcode / Binary | In-Memory / PowerShell Heap | Cobalt Strike Stager |
| `lsass_dump.dmp` | `8f828a213e4b77f8849b2750e303fc8f2d5773ff4d2df468e82ef620e2ef648d` | Minidump | `C:\Windows\Temp\lsass_dump.dmp` | LSASS Memory Dump |
| `finance_dump.zip` | `c4ca4238a0b923820dcc509a6f75849b2c0fd3f6b92a40b904494a86f99a8b11` | Encrypted ZIP | `C:\Users\Public\` | Staged Exfiltration Archive |

---

## 3. Host-Based & Behavioral Indicators

| Category | Artifact / Key / Command | Behavior / ATT&CK Technique |
| :--- | :--- | :--- |
| **Registry** | `HKCU\Software\Classes\ms-settings\Shell\Open\command` | UAC Bypass via `fodhelper.exe` (T1548.002) |
| **Registry** | `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\Updater` | Persistence Registry Key (T1547.001) |
| **Command Line** | `rundll32.exe C:\Windows\System32\comsvcs.dll, MiniDump [PID] C:\Windows\Temp\lsass_dump.dmp full` | Native LSASS dump via comsvcs DLL (T1003.001) |
| **Command Line** | `powershell.exe -nop -w hidden -enc WwB...` | Hidden Encoded PowerShell Execution (T1059.001) |
| **Process Access** | Source: `rundll32.exe` -> Target: `lsass.exe` (AccessMask: `0x1FFFFF`) | Full access mask granted on LSASS process |
