# ⏱️ Master Incident & Telemetry Timeline

All timestamps recorded in **UTC** during the simulated exercise.

---

| Timestamp (UTC) | Source Host | Source Artifact / Event ID | Activity Description | Severity | Analyst Initial Findings |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `2026-09-29 14:15:02` | `WKSTN01` | Sysmon EID 1 | `WINWORD.EXE` spawned `cmd.exe` -> `powershell.exe` | **CRITICAL** | Initial compromise via malicious macro attachment. |
| `2026-09-29 14:15:22` | `WKSTN01` | Sysmon EID 3 | Outbound connection from `powershell.exe` to `192.168.99.50:8000` | **HIGH** | Second-stage payload download over HTTP. |
| `2026-09-29 14:16:10` | `WKSTN01` | Security EID 4104 | PowerShell Script Block logged base64 encoded stager | **HIGH** | Execution of in-memory Cobalt Strike beacon. |
| `2026-09-29 14:18:45` | `WKSTN01` | Sysmon EID 13 | Registry write to `HKCU\Software\Classes\ms-settings\Shell\Open\command` | **HIGH** | Fodhelper UAC Bypass technique observed. |
| `2026-09-29 14:19:02` | `WKSTN01` | Sysmon EID 1 | Elevated `cmd.exe` spawned under high integrity token | **CRITICAL** | Privilege escalation confirmed on workstation. |
| `2026-09-29 14:22:15` | `WKSTN01` | Sysmon EID 10 | Target Image `C:\Windows\System32\lsass.exe` accessed by `rundll32.exe` | **CRITICAL** | LSASS memory dump attempt via `comsvcs.dll`. |
| `2026-09-29 14:25:30` | `WKSTN01` | Sysmon EID 1 | Recon commands: `net user /domain`, `net group "Domain Admins" /domain` | **MEDIUM** | Active Directory enumeration. |
| `2026-09-29 14:31:00` | `DC01` | Security EID 4624 | Successful Logon Type 3 (Network) with `CORP\da_admin` from `192.168.10.50` | **HIGH** | Lateral movement initiation to Domain Controller. |
| `2026-09-29 14:33:12` | `DC01` | Sysmon EID 1 | `wmic.exe` process created `certutil.exe` staging utility | **CRITICAL** | Remote execution on primary Domain Controller. |
| `2026-09-29 14:40:00` | `WKSTN01` | Sysmon EID 11 | File created: `C:\Users\Public\finance_dump.zip` (18.4 MB) | **HIGH** | Data staging prior to exfiltration. |
| `2026-09-29 14:42:18` | `WKSTN01` | Sysmon EID 3 | Outbound HTTPS transfer to `192.168.99.50:443` | **CRITICAL** | Data exfiltration completed. |
| `2026-09-29 14:50:00` | `SIEM-WAZUH`| Wazuh Alert | Analyst triggered host containment on `WKSTN01` & `DC01` | **INFO** | Containment and active remediation started. |
