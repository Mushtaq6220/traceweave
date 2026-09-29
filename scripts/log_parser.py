#!/usr/bin/env python3
"""
TraceWave SOC Lab: Sysmon & Security Log Telemetry Parser
Author: Mohammad Mushtaq
"""

import json
import sys

def parse_sysmon_event(event_json):
    try:
        data = json.loads(event_json)
        event_id = data.get("win", {}).get("system", {}).get("eventID")
        event_data = data.get("win", {}).get("eventdata", {})
        print(f"[+] Sysmon Event ID {event_id}: Image={event_data.get('image')} CommandLine={event_data.get('commandLine')}")
    except Exception as e:
        print(f"[-] Error parsing event: {e}")

if __name__ == '__main__':
    print("[*] TraceWave Log Parser Initialized")
