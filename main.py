from colorama import Fore, Style
import requests
import json

text = """
⠀          

    __ __                __             _    __            _ __           ________              __            
   / //_/___ _____  ____/ /__  _  __   | |  / /___ _____  (_) /___  __   / ____/ /_  ___  _____/ /_____  _____
  / ,< / __ `/ __ \/ __  / _ \| |/_/   | | / / __ `/ __ \/ / __/ / / /  / /   / __ \/ _ \/ ___/ //_/ _ \/ ___/
 / /| / /_/ / /_/ / /_/ /  __/>  <     | |/ / /_/ / / / / / /_/ /_/ /  / /___/ / / /  __/ /__/ ,< /  __/ /    
/_/ |_\__,_/\____/\__,_/\___/_/|_|     |___/\__,_/_/ /_/_/\__/\__, /   \____/_/ /_/\___/\___/_/|_|\___/_/     
                                                             /____/                                           
⠀⠀

"""

print(text)
print(Style.DIM + Fore.GREEN + "[+] " + Fore.WHITE + "Created by Kaodex")

webhook_url = "https://discord.com/api/webhooks/1221852826964066335/hcYL6YVLeI_AFU2D9dUcpcwWGDe0dsrv0daIe1yDjnSeT9RozeRvM3PCgZzaZXTkPbXs"

def check_url(vanity):
    check = requests.get(f"https://discord.com/api/v9/invites/{vanity}")
    if check.status_code == 404:
        print(Fore.GREEN + "[+] " + Fore.WHITE + f"{vanity} is Claimable!")
        return True
    else:
        print(Fore.RED + "[-] " + Fore.WHITE + f"{vanity} is Taken!")
        return False

def send_discord_message(vanity):
    embed_data = {
        "embeds": [
            {
                "title": f"{vanity} boşta/banlı",
                "color": 65280
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(webhook_url, data=json.dumps(embed_data), headers=headers)

    if response.status_code == 204:
        print(Fore.GREEN + "[+] " + Fore.WHITE + "Discord message sent successfully!")
    else:
        print(Fore.RED + "[-] " + Fore.WHITE + "Failed to send Discord message. Status Code:", response.status_code)

def save_to_file(urls):
    with open("kaydedilen_urls.txt", "a") as file:
        for url in urls:
            file.write(url + "\n")

def main():
    file_path = "urls.txt"
    
    try:
        with open(file_path, "r") as file:
            urls = file.read().splitlines()
    except FileNotFoundError:
        print(Fore.RED + "[-] " + Fore.WHITE + f"{file_path} not found. Please create the file with URLs.")
        return

    claimable_urls = []

    for url in urls:
        if check_url(url):
            claimable_urls.append(url)
            send_discord_message(url)

    if claimable_urls:
        save_to_file(claimable_urls)
        print(Fore.GREEN + "[+] " + Fore.WHITE + "Claimable URLs saved to kaydedilen_urls.txt")

    x = input(Fore.GREEN + "[+] " + Fore.WHITE + "Want to check another? ").lower()
    if x == "yes":
        main()

main()
