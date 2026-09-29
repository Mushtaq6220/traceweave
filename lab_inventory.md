# 📋 Lab Asset & Systems Inventory

## 🖥️ Virtual Machine Inventory

# Lab Inventory

| Machine | Role | Hypervisor | Hostname | IP Address | OS Version | Network Mode |
|---|---|---|---|---|---|---|
| Windows | Victim / Sysmon host | Physical host | bugbountyhunter | 192.168.56.1 | Windows 11 | Home LAN |
| Kali | Attacker | VMware | kali | 192.168.x.x | Kali 2025.3 | Bridged |
| Ubuntu | Wazuh manager | VirtualBox | ubuntu | 192.168.x.x | Ubuntu 24.04 LTS | Bridged |

**Git version (Kali): 2.53.0**
**Python version (Kali):3.13.7**
**PowerShell version (Windows):5.1.26100.9549**

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
