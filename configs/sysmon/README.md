# ⚙️ Sysmon Configuration Profiles

This directory contains the custom **Sysmon (System Monitor)** configuration XMLs deployed to Windows Endpoints (`WKSTN01`) and Domain Controllers (`DC01`).

---

## 📄 Key Configs Included:
- `sysmonconfig-export.xml`: Modular configuration derived from SwiftOnSecurity & Florian Roth's best practices, tuned for SOC detection.

### Monitored Event IDs:
- **EID 1**: Process Creation (full CLI, hashes, parent-child relationships).
- **EID 3**: Network Connection (outbound socket connections with process context).
- **EID 7**: Image Loaded (DLLs loaded by sensitive binaries).
- **EID 8**: CreateRemoteThread (Process injection detection).
- **EID 10**: ProcessAccess (LSASS and sensitive token inspection).
- **EID 11**: FileCreate (Persistence and staging folders).
- **EID 12/13/14**: RegistryEvent (Run keys, services, UAC bypass keys).
