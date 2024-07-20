from colorama import Fore, Style
import requests
import json

text = """
⠀          

    31                                         
⠀⠀

"""

print(text)
print(Style.DIM + Fore.GREEN + "[+] " + Fore.WHITE + "bla bla bla")

webhook_url = ""

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
