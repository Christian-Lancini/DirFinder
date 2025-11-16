import requests
import os

def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")


def dirFinder(url, wordlist):
    try:
        with open(wordlist, "r") as file:
            directories = file.read().splitlines()
    except Exception as e:
        print(e)
        return

    for directory in directories:
        directory = directory.strip()
        if not directory:
            continue
        
        full_url = f"{url}/{directory.lstrip('/')}"
        
        try:
            response = requests.get(full_url, timeout=5)
            if response.status_code == 200:
                print(f"\n[*] Directory found: {full_url}")
            elif response.status_code == 403:
                print(f"[!] Access denied: {full_url}")
            elif response.status_code == 404:
                pass
            else:
                print(f"[?]{full_url}: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error while requesting {full_url}: {e}")

def main():
    while True:
        clear()
        print(r""" 
    ________  .__      ___________.__            .___            
    \______ \ |__|_____\_   _____/|__| ____    __| _/___________ 
    |    |  \|  \_  __ \    __)  |  |/    \  / __ |/ __ \_  __ \
    |    `   \  ||  | \/     \   |  |   |  \/ /_/ \  ___/|  | \/
    /_______  /__||__|  \___  /   |__|___|  /\____ |\___  >__|   
            \/              \/            \/      \/    \/       

        """)

        print("\nWelcome to DirFinder")
        print("1- Start scan")
        print("2- Exit")

        opt = int(input("\n> "))

        if opt == 1:
            clear()
            site = input("\nURL: ").strip()
            wd = input("Wordlist: ")
            dirFinder(site, wd)
            print("\n[STOP] Scan completed!")
            input("Press any key to return to home...")
        
        elif opt == 2:
            break
        
        else:
            print("Please select a valid option!")
            input("...")
        
if __name__ == "__main__":
    main()
