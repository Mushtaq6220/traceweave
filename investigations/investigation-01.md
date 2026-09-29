# 📑 Investigation Case File: IR-2026-001

**Case Name**: Operation Crimson Velvet - Compromise of `WKSTN01` & Lateral Spread to `DC01`  
**Lead Investigator**: Mohammad Mushtaq  
**Date Opened**: 2026-09-29  
**Case Status**: CLOSED / REMEDIATED  
**Classification**: High-Impact Enterprise Compromise  

---

## 1. Trigger & Initial Alert
- **Alert**: Wazuh Rule ID `100101` (LSASS MiniDump via comsvcs.dll) and Rule ID `100102` (Fodhelper UAC Bypass).
- **Source Host**: `WKSTN01.corp.local` (`192.168.10.50`)
- **User Context**: `CORP\jdoe` -> Elevated to `CORP\da_admin`

---

## 2. Investigation Findings & Triage

### Phase 1: Initial Vector Analysis
- The user received an email with subject *"Overdue Invoice #9921"* containing `Invoice_Q3.docm`.
- Opening the document caused `WINWORD.EXE` (PID: 4820) to spawn `cmd.exe` and `powershell.exe`.
- PowerShell executed a base64-encoded download cradle fetching `http://192.168.99.50:8000/stage2.bin`.

### Phase 2: Privilege Escalation
- Attacker leveraged `fodhelper.exe` UAC bypass by writing `C:\Windows\System32\cmd.exe` to `HKCU\Software\Classes\ms-settings\Shell\Open\command`.
- Spawned high-integrity command shell without triggering standard UAC prompt.

### Phase 3: Credential Dumping & Lateral Movement
- High-integrity process executed `rundll32.exe C:\Windows\System32\comsvcs.dll, MiniDump 672 C:\Windows\Temp\lsass_dump.dmp full`.
- Domain Admin credentials for `CORP\da_admin` extracted.
- Remote WMI / SMB connections made from `192.168.10.50` to `192.168.10.10` (`DC01`).

---

## 3. Containment Actions Taken
1. **Network Isolation**: Applied host isolation rule on `WKSTN01` via Wazuh active response.
2. **Account Revocation**: Disabled `CORP\jdoe` and reset `CORP\da_admin` Kerberos KRBTGT password.
3. **Firewall Block**: Blocked IP `192.168.99.50` and domain `cdn-update-auth.com` on perimeter firewall.

---

## 4. Remediation & Verification
- Extracted and safely wiped all temp staging files (`lsass_dump.dmp`, `finance_dump.zip`).
- Deployed Sigma & Wazuh detection rules to prevent future bypasses.
- Host reimaged and returned to production after baseline verification.
