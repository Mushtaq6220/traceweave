# 🛡️ SOC Analyst Lab: TraceWave

> **Building Real-World Investigations from Telemetry & Weaving Event Logs into Cohesive Threat Analysis**

Welcome to **TraceWave - SOC Analyst Lab**, an enterprise-grade threat detection, digital forensics, and incident response (DFIR) simulation environment. This repository documents an 8-day end-to-end security operations project covering lab architecture, telemetry engineering (Sysmon, Wazuh SIEM), adversary simulation (MITRE ATT&CK), detection engineering (Sigma & Wazuh rules), forensic evidence collection, and formal incident reporting.

---

## 📌 Repository Architecture & Directory Structure

```text
soc-analyst-lab/
│
├── README.md                   # Main lab overview, objectives, and documentation
├── .gitignore                  # Git exclusions for logs, dumps, and credentials
├── lab_inventory.md            # Hardware, VM, network, and software asset inventory
├── attack_scenario_plan.md     # MITRE ATT&CK adversary simulation and execution plan
├── timeline.md                 # Master chronological timeline of adversary actions & alerts
├── iocs.md                     # Indicators of Compromise (Hashes, IPs, Domains, Registry keys)
│
├── architecture/
│   └── architecture.png        # High-resolution network & telemetry pipeline diagram
│
├── notes/                      # Daily progress logs, engineering hurdles, and learning notes
│   ├── day01.md                # Lab Design & Network Architecture
│   ├── day02.md                # Infrastructure Deployment & OS Hardening
│   ├── day03.md                # Telemetry Setup (Sysmon, Auditd, Winlogbeat)
│   ├── day04.md                # SIEM & Log Pipeline Deployment (Wazuh Manager/Indexer)
│   ├── day05.md                # Adversary Emulation & Attack Execution
│   ├── day06.md                # Alert Triage & Detection Rule Engineering
│   ├── day07.md                # Deep-Dive DFIR & Memory/Disk Artifact Analysis
│   └── day08.md                # Final Incident Reporting & Post-Incident Review
│
├── evidence/                   # Raw telemetry, event exports, and PCAPs
│   ├── README.md               # Evidence handling and chain-of-custody guidelines
│   ├── day01/ to day08/        # Partitioned evidence stores per operational day
│
├── configs/                    # System & Agent configuration templates
│   ├── sysmon/                 # Custom Sysmon configuration XMLs
│   └── wazuh/                  # Wazuh agent and server configuration templates
│
├── detections/                 # Custom detection engineering rules
│   ├── README.md               # Rule writing methodologies and validation steps
│   ├── wazuh/                  # Custom Wazuh XML detection rules
│   └── sigma/                  # Custom Sigma YAML detection rules
│
├── investigations/             # Case files and forensic analysis walkthroughs
│   ├── README.md               # Investigation methodology & triage playbooks
│   └── investigation-01.md     # Incident-001: Cobalt Strike / PowerView Compromise
│
├── reports/                    # Formal Incident Reports
│   ├── Incident_Report.md      # Executive and technical incident summary (Markdown)
│   └── Incident_Report.pdf     # Formatted PDF Incident Report
│
└── scripts/                    # SOC automation, log parsing, and IOC extraction utilities
```

---

## 🎯 Lab Objectives

1. **Telemetry & Visibility Pipeline**: Instrument Windows Endpoints (Sysmon, Windows Event Forwarding) and Linux servers with Wazuh Agent to achieve deep endpoint visibility.
2. **Adversary Simulation**: Replicate real-world Advanced Persistent Threat (APT) tactics mapped to the **MITRE ATT&CK** matrix.
3. **Detection Engineering**: Author high-fidelity **Sigma** and **Wazuh** rules to detect living-off-the-land binaries (LOLBins), credential dumping, lateral movement, and command-and-control (C2) channels.
4. **DFIR & Incident Handling**: Conduct root-cause analysis, reconstruct attack timelines, parse artifacts ($MFT, Shimcache, Prefetch, Registry), and produce executive-grade incident reports.

---

## 🔬 Core Technologies & Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| **SIEM & XDR** | Wazuh 4.x / Elastic Stack | Centralized Log Aggregation, Correlation, & Alerting |
| **Endpoint Telemetry** | Sysmon (Modular Config) | Process Creation (EID 1), Network Connections (EID 3), Image Loads (EID 7) |
| **Detection Format** | Sigma / Wazuh Rules | Portable rule specifications mapped to ATT&CK techniques |
| **Adversary Emulation** | Atomic Red Team / Custom Scripts | Standardized technique execution & validation |
| **Forensic Triage** | Velociraptor / KAPE / FTK Imager | Artifact extraction and timeline generation |
| **Network Security** | Zeek / Wireshark / Suricata | Network session analysis, DNS tunneling & C2 detection |

---

## 📊 8-Day SOC Analyst Roadmap Summary

- **Day 01**: Lab topology planning, subnet segmentation, and architecture mapping.
- **Day 02**: Provisioning Domain Controller, Windows 11 Endpoint, Ubuntu Web Server, and Kali Linux.
- **Day 03**: Fine-tuning Sysmon configurations and Windows Advanced Audit Policies.
- **Day 04**: Deploying Wazuh Manager, Agent onboarding, and pipeline health verification.
- **Day 05**: Executing multi-stage cyber attack scenario (Phishing -> LOLBins -> LSASS Dump -> Lateral Movement).
- **Day 06**: Triage alerts, investigate false positives, write Sigma & Wazuh detection rules.
- **Day 07**: Evidence extraction, memory artifact triage, timeline reconstruction.
- **Day 08**: Drafting comprehensive Incident Report, Executive Briefing, and Remediation Roadmap.

---

## 👤 Author

- **Analyst**: Mohammad Mushtaq
- **GitHub**: [@Mushtaq6220](https://github.com/Mushtaq6220)
- **Repository**: [traceweave](https://github.com/Mushtaq6220/traceweave)
