# 📁 Forensic Evidence & Artifact Repository

This directory contains raw evidence, captured logs, packet captures, and triage dumps collected throughout the 8-day lab exercises.

---

## 🔒 Chain of Custody & Evidence Handling Protocol

1. **Integrity Verification**: All forensic artifacts must be hashed (SHA-256) upon acquisition and recorded in `iocs.md`.
2. **Read-Only Preservation**: Work on forensic copies or extracted CSV/JSON exports; never modify primary evidentiary archives.
3. **Partitioning**:
   - `day01/` to `day08/`: Daily telemetry logs, screenshots, and alert exports.

---

## 📂 Subfolder Index

- `day01/`: Network topology files and initial base config captures.
- `day02/`: VM build logs and baseline OS event logs.
- `day03/`: Sysmon & Auditd configuration exports.
- `day04/`: Wazuh agent registration validation logs.
- `day05/`: Raw attack simulation logs (Sysmon, Security, Application).
- `day06/`: Alert triggers, false positive analysis samples.
- `day07/`: Memory dump triage outputs, MFT parse CSVs, Prefetch exports.
- `day08/`: Final evidence packages and executive sign-off records.
