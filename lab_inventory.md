# 📋 Lab Asset & Systems Inventory

This document tracks all physical hosts, virtual machines, networking appliances, software packages, and log forwarding configurations in the **TraceWave SOC Lab**.

---

## 🖥️ Virtual Machine Inventory

| Hostname | Role / Description | OS | IP Address | Subnet / VLAN | RAM / vCPU | Installed Agents | Log Sources |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `DC01.corp.local` | Domain Controller / Active Directory | Windows Server 2022 | `192.168.10.10` | VLAN 10 (Corp LAN) | 4 GB / 2 vCPU | Wazuh Agent, Sysmon | Security.evtx, System.evtx, Sysmon.evtx, DNS Server |
| `WKSTN01.corp.local` | Finance Workstation / Target Endpoint | Windows 11 Enterprise | `192.168.10.50` | VLAN 10 (Corp LAN) | 8 GB / 4 vCPU | Wazuh Agent, Sysmon | Security.evtx, Sysmon.evtx, PowerShell Operational |
| `SRV-WEB01` | Public Web & App Server | Ubuntu 22.04 LTS | `192.168.20.15` | VLAN 20 (DMZ) | 4 GB / 2 vCPU | Wazuh Agent, Auditd | `/var/log/auth.log`, `/var/log/nginx/`, Auditd |
| `SIEM-WAZUH` | Centralized Wazuh SIEM & Indexer | Ubuntu 22.04 LTS | `192.168.30.100` | VLAN 30 (SecOps) | 8 GB / 4 vCPU | Wazuh Server, OpenSearch | Syslog (514), Agent Registration (1514/1515) |
| `KALI-ATTACK` | Adversary Emulation Platform | Kali Linux 2024.x | `192.168.99.50` | VLAN 99 (Attacker) | 4 GB / 2 vCPU | Metasploit, Covenant, Impacket | Attack telemetry & staging logs |

---

## 🌐 Network Segmentation & Firewall Rules

| Source Subnet | Destination Subnet | Port / Protocol | Purpose / Description | Action |
| :--- | :--- | :--- | :--- | :--- |
| `VLAN 10` (Corp LAN) | `VLAN 30` (SecOps) | TCP 1514, 1515 | Wazuh Agent event streaming and registration | **ALLOW** |
| `VLAN 20` (DMZ) | `VLAN 30` (SecOps) | TCP 1514, 1515 | Wazuh Agent DMZ event streaming | **ALLOW** |
| `VLAN 99` (Attacker) | `VLAN 20` (DMZ) | TCP 80, 443 | Public HTTP/HTTPS exposure for initial web exploit | **ALLOW** |
| `VLAN 99` (Attacker) | `VLAN 10` (Corp LAN) | ANY | Direct access blocked (Simulates perimeter firewall) | **DENY** |
| `VLAN 10` (Corp LAN) | `VLAN 99` (Attacker) | TCP 443, 8443 | Simulated C2 outbound egress connection | **ALLOW** |

---

## 📦 Software & Tooling Matrix

- **Sysmon**: v15.14 with SwiftOnSecurity modular XML profile.
- **Wazuh Agent**: v4.8.0 on Windows Server 2022, Windows 11, and Linux.
- **Wazuh Manager / Indexer / Dashboard**: v4.8.0 all-in-one deployment.
- **Sigma CLI**: `sigmac` and `sigma-cli` for converter automation.
- **Adversary Simulation Tools**: Atomic Red Team, Impacket, Mimikatz, PowerShell Empire stager.
