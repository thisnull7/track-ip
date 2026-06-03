#!/usr/bin/env python3

# Created by null7

import sys
import json
import requests
from colorama import init, Fore, Back, Style

init(autoreset=True)

BANNER = f"""
{Fore.RED}{Style.BRIGHT}
████████╗██████╗  █████╗  ██████╗██╗  ██╗   ██╗██████╗ 
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝   ██║██╔══██╗
   ██║   ██████╔╝███████║██║     █████╔╝    ██║██████╔╝
   ██║   ██╔══██╗██╔══██║██║     ██╔═██╗    ██║██╔═══╝ 
   ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗   ██║██║     
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝╚═╝     
{Fore.RED}═══════════════════════════════════════════════════════════
{Fore.RED}[ {Fore.WHITE}TRACK IP {Fore.RED}] {Fore.YELLOW}Precision Geolocation & Network Intel
{Fore.RED}[ {Fore.WHITE}Created by null7 {Fore.RED}] {Fore.YELLOW}Leave nothing but fear.
{Fore.RED}═══════════════════════════════════════════════════════════
"""

SKULL_LINES = [
    f"{Fore.RED}                 .-\"\"\"-.",
    f"{Fore.RED}                /       \\",
    f"{Fore.RED}                \\       /",
    f"{Fore.RED}                 '-...-'",
    f"{Fore.WHITE}            ☠️  NO HIDING  ☠️",
]

def print_skull():
    for line in SKULL_LINES:
        print(line)

def get_ip_info(ip):
    try:
        url = f"http://ip-api.com/json/{ip}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,asname,reverse,mobile,proxy,hosting,query"
        resp = requests.get(url, timeout=10)
        data = resp.json()
        if data.get("status") == "fail":
            return None, data.get("message", "Unknown error")
        return data, None
    except Exception as e:
        return None, str(e)

def display_info(data):
    print(Fore.RED + Style.BRIGHT + "☠️  TARGET ACQUIRED ☠️" + Style.RESET_ALL)
    print(Fore.RED + "═" * 55)
    fields = [
        ("IP Address", data.get("query")),
        ("Country", f"{data.get('country')} ({data.get('countryCode')})"),
        ("Region", f"{data.get('regionName')} ({data.get('region')})"),
        ("City", data.get("city")),
        ("ZIP Code", data.get("zip")),
        ("Coordinates", f"{data.get('lat')}, {data.get('lon')}"),
        ("Timezone", data.get("timezone")),
        ("ISP", data.get("isp")),
        ("Organization", data.get("org")),
        ("AS Number/Name", f"{data.get('as')} {data.get('asname')}"),
        ("Reverse DNS", data.get("reverse")),
        ("Mobile", "Yes" if data.get("mobile") else "No"),
        ("Proxy/VPN", "Yes" if data.get("proxy") else "No"),
        ("Hosting/DC", "Yes" if data.get("hosting") else "No"),
    ]
    for label, value in fields:
        print(f"{Fore.RED}{label:20}{Fore.WHITE}: {Fore.GREEN}{value}")
    
    lat = data.get("lat")
    lon = data.get("lon")
    if lat and lon:
        maps_link = f"https://www.google.com/maps?q={lat},{lon}"
        print(Fore.RED + "═" * 55)
        print(Fore.CYAN + Style.BRIGHT + "📍 Maps Location:")
        print(Fore.WHITE + maps_link)
        print(Fore.RED + "═" * 55)

if __name__ == "__main__":
    print(BANNER)
    if len(sys.argv) > 1:
        target_ip = sys.argv[1]
    else:
        print(Fore.YELLOW + "[?] IP target" + Fore.WHITE)
        target_ip = input(Fore.RED + "    ➤ " + Fore.WHITE).strip()
        if not target_ip:
            print(Fore.RED + "[!] No IP entered.")
            sys.exit(1)

    print(Fore.YELLOW + f"\n[*] Tracking {target_ip} ...\n")
    print_skull()
    
    info, error = get_ip_info(target_ip)
    if error:
        print(Fore.RED + f"[!] Failed Tracking: {error}")
        sys.exit(1)
    
    display_info(info)
    print(Fore.RED + "[✓] Digital footprints exposed. Targets can't hide..\n")