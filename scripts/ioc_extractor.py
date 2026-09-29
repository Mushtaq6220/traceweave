#!/usr/bin/env python3
"""
TraceWave SOC Lab: IOC Extractor & Defanger Utility
Author: Mohammad Mushtaq
"""

import re
import sys

def defang_ip(ip):
    return ip.replace('.', '[.]')

def defang_url(url):
    return url.replace('http://', 'hxxp://').replace('https://', 'hxxps://').replace('.', '[.]')

def extract_iocs(text):
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    sha256_pattern = r'\b[a-fA-F0-9]{64}\b'
    
    ips = re.findall(ip_pattern, text)
    hashes = re.findall(sha256_pattern, text)
    
    print("=== Extracted IP Addresses (Defanged) ===")
    for ip in set(ips):
        print(f" - {defang_ip(ip)}")
        
    print("\n=== Extracted SHA-256 Hashes ===")
    for h in set(hashes):
        print(f" - {h}")

if __name__ == '__main__':
    sample_text = """
    Attacker hosted payload on 192.168.99.50 and contacted C2 at 10.0.0.1.
    Hash: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    """
    extract_iocs(sample_text)
