# 🎯 Adversary Attack Scenario Plan

### Scenario Codename: **Operation Crimson Velvet**
**Threat Actor Profile**: APT-style Opportunistic FinCrime Group  
**Target**: Corporate Finance Workstation (`WKSTN01`) & Active Directory Domain Controller (`DC01`)

---

## 🗺️ MITRE ATT&CK Matrix Mapping

| Phase / Tactic | Technique ID | Technique Name | Tool / Command Executed | Detection Target |
| :--- | :--- | :--- | :--- | :--- |
| **Initial Access** | `T1566.001` | Spearphishing Attachment | Malicious Macro-enabled document / HTA payload | Sysmon EID 1 (MSOffice spawning MSHTA/Powershell) |
| **Execution** | `T1059.001` | PowerShell Execution | Encoded PowerShell downloading second stage | Sysmon EID 1 + Win Event 4104 (Script Block) |
| **Persistence** | `T1547.001` | Registry Run Keys / Startup | `reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run` | Sysmon EID 12/13 (Registry modification) |
| **Privilege Escalation** | `T1548.002` | Bypass UAC (Fodhelper) | `fodhelper.exe` registry hijacking | Sysmon EID 1, 13 (HKCU Software Classes ms-settings) |
| **Defense Evasion** | `T1562.001` | Disable Security Tools | `Set-MpPreference -DisableRealtimeMonitoring $true` | Event ID 5001 (Defender Realtime Disabled) |
| **Credential Access** | `T1003.001` | LSASS Memory Dumping | `procdump.exe` / `mimikatz.exe sekurlsa::logonpasswords` | Sysmon EID 10 (ProcessAccess to lsass.exe) |
| **Discovery** | `T1087.002` | Domain Account Discovery | `net user /domain`, `nltest /dclist:` | Sysmon EID 1, Event ID 4688 |
| **Lateral Movement** | `T1021.002` | SMB/Windows Admin Shares | `psexec.py` / `wmic process call create` | Sysmon EID 1, Event ID 4624 (Type 3 logon) |
| **Collection & C2** | `T1071.001` | Web Protocols (HTTPS C2) | Beaconing over Port 443 with Jitter | Sysmon EID 3 (Network Connect) |
| **Exfiltration** | `T1048.003` | Exfiltration Over Alternative Protocol | Encrypted ZIP staged via DNS / Cloud Storage | Sysmon EID 11 (File creation in `\AppData\Local\Temp`) |

---

## 🛠️ Step-by-Step Execution Sequence

1. **Initial Vector**: Target user on `WKSTN01` opens invoice attachment `Invoice_Q3.docm`.
2. **Staging & Beaconing**: Macro spawns hidden PowerShell, downloads payload from `192.168.99.50:8000/stage2.bin`, and initiates reverse C2 channel.
3. **Local Recon & PrivEsc**: Attacker runs `whoami /all`, `net localgroup administrators`, and performs UAC bypass using `fodhelper`.
4. **Credential Harvesting**: In elevated context, attacker dumps `lsass.exe` using `rundll32.exe comsvcs.dll, MiniDump` and extracts Domain Admin credentials.
5. **Lateral Spread**: Using harvested Domain Admin credentials, attacker connects to `DC01` via WMI/WinRM.
6. **Data Staging & Exfiltration**: Customer database and finance records zipped and staged in `C:\Users\Public\archive.zip` and exfiltrated.
