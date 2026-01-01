#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import sys
import time
import os
import random

# Colors for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear_screen()
    print(f"{Colors.CYAN}{Colors.BOLD}")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║   🐞 BUG HTTP INJECTOR FRESH GETTER - POWERFUL EDITION 🚀    ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print(f"{Colors.GREEN}")
    print("  Author       : Z3R0-K")
    print("  Organization : Mari Partner")
    print("  Github       : hndko")
    print(f"{Colors.CYAN}")
    print("  [ NOTE ] : Auto scraping fresh bugs for your injection needs.")
    print(f"{Colors.ENDC}")
    print("=" * 64)
    print()

def typing_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def get_bugs():
    url = "https://atsameip.intercode.ca/"

    print(f"{Colors.WARNING} [⏳] Connecting to server... {url}{Colors.ENDC}")

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            print(f"{Colors.GREEN} [✅] Connected Successfully!{Colors.ENDC}\n")

            soup = BeautifulSoup(response.text, 'html.parser')

            # This logic depends on the website structure.
            # Assuming we are looking for links or a specific list.
            # Based on 'Recent Queries' or similar sections.

            links = []
            # Gather all links that look like domains (simplified logic)
            for a in soup.find_all('a', href=True):
                href = a['href']
                text = a.text.strip()
                if text and '.' in text and not text.startswith('http'):
                    links.append(text)
                elif 'http' in href:
                     # sometimes the text is empty or different, check href
                     pass

            # Filter duplicates
            links = list(set(links))

            if links:
                print(f"{Colors.BOLD}[🚀] Found {len(links)} Potential Bugs:{Colors.ENDC}")
                print("-" * 40)
                for i, link in enumerate(links):
                    # Aesthetic delay effect
                    if i < 20: # Limit output or full list
                        sys.stdout.write(f"{Colors.BLUE} [{i+1}] 🐛 {link} {Colors.ENDC}\n")
                        time.sleep(0.05)
                    else:
                        sys.stdout.write(f"{Colors.BLUE} [{i+1}] 🐛 {link} {Colors.ENDC}\n")
                print("-" * 40)
                print(f"{Colors.GREEN} [🎉] Done! Happy Injecting. {Colors.ENDC}")
            else:
                print(f"{Colors.FAIL} [❌] No bugs found on the page. Structure might have changed.{Colors.ENDC}")

        else:
            print(f"{Colors.FAIL} [❌] Failed to retrieve data. Status Code: {response.status_code}{Colors.ENDC}")

    except Exception as e:
        print(f"{Colors.FAIL} [💥] Error: {str(e)}{Colors.ENDC}")

if __name__ == "__main__":
    banner()
    try:
        get_bugs()
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING} [👋] Exiting... Bye!{Colors.ENDC}")