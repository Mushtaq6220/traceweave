# 📑 Official Cybersecurity Incident Report

**Incident ID**: INC-2026-0929-01  
**Target Organization**: TraceWave Corp  
**Incident Severity**: **HIGH / CRITICAL**  
**Date of Incident**: 2026-09-29  
**Lead Analyst**: Mohammad Mushtaq (SOC Lead)  

---

## 1. Executive Summary

On September 29, 2026, at 14:15 UTC, the TraceWave Security Operations Center (SOC) detected unauthorized adversary activity originating on workstation `WKSTN01` (`192.168.10.50`). The adversary successfully gained initial access via a spearphishing macro attachment, performed a User Account Control (UAC) bypass using `fodhelper.exe`, dumped credential material from the Local Security Authority Subsystem Service (`lsass.exe`), and moved laterally to the primary Domain Controller (`DC01`). 

Immediate containment actions isolated the infected hosts, blocked outbound Command & Control (C2) communication, and neutralized the threat before widespread data destruction occurred.

---

## 2. Impact Assessment

| Scope Area | Impact Rating | Description |
| :--- | :--- | :--- |
| **Confidentiality** | **HIGH** | Financial staging archive (`finance_dump.zip`) accessed; potential credential exposure. |
| **Integrity** | **MEDIUM** | Registry modifications on `WKSTN01` and staging scripts placed on `DC01`. |
| **Availability** | **LOW** | No disruption to critical customer-facing services or business operations. |

---

## 3. Root Cause Analysis

1. **Initial Vector**: Macro execution allowed under Microsoft Office default policy for external attachments.
2. **Missing EDR Prevention**: LSASS memory read access was not blocked by native OS controls.
3. **Privilege Over-Assignment**: Standard user account held cached administrative session credentials on shared endpoint.

---

## 4. Corrective Actions & Strategic Recommendations

- [x] **Immediate**: Reset all Domain Administrator passwords and rotate Active Directory KRBTGT hash twice.
- [x] **Detection**: Deployed custom Sysmon and Wazuh rules for LOLBins and LSASS access.
- [ ] **Policy**: Enforce Attack Surface Reduction (ASR) rule *Block all Office applications from creating child processes*.
- [ ] **Architecture**: Implement LAPS (Local Administrator Password Solution) and Credential Guard.
