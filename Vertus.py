import time
import requests
import random
import urllib.parse
import os
from colorama import Fore, Style, init

init(autoreset=True)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def art():
    print("\033[1;91m" + r"""     

 /$$   /$$                                                  
| $$  /$$/                                                  
| $$ /$$/   /$$$$$$   /$$$$$$  /$$   /$$ /$$   /$$  /$$$$$$ 
| $$$$$/   |____  $$ /$$__  $$| $$  | $$| $$  | $$ |____  $$
| $$  $$    /$$$$$$$| $$  \ $$| $$  | $$| $$  | $$  /$$$$$$$
| $$\  $$  /$$__  $$| $$  | $$| $$  | $$| $$  | $$ /$$__  $$
| $$ \  $$|  $$$$$$$|  $$$$$$$|  $$$$$$/|  $$$$$$$|  $$$$$$$
|__/  \__/ \_______/ \____  $$ \______/  \____  $$ \_______/
                     /$$  \ $$           /$$  | $$          
                    |  $$$$$$/          |  $$$$$$/          
                     \______/            \______/           
""" + "\033[0m" + "\033[1;92m" + r"""                                    
 ____  _     _                       _
/ ___|| |__ (_)_ __   ___  _ __ ___ (_)_   _  __ _
\___ \| '_ \| | '_ \ / _ \| '_ ` _ \| | | | |/ _` |
 ___) | | | | | | | | (_) | | | | | | | |_| | (_| |
|____/|_| |_|_|_| |_|\___/|_| |_| |_|_|\__, |\__,_|
                                       |___/
""" + "\033[0m\n\033[1;96m---------------------------------------\033[0m\n\033[1;93mScript created by: Kaguya Shinomiya\033[0m\n\033[1;92mJoin Telegram: \nhttps://t.me/Pumpbtcxyz\033[0m\n\033[1;91mVisit my GitHub: \nhttps://github.com/Kaguya1st\033[0m\n\033[1;96m---------------------------------------\033[0m\n\033[1;38;2;139;69;19;48;2;173;216;230m-------------[Vertus Bot]-------------\033[0m\n\033[1;96m---------------------------------------\033[0m")

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        print(f"{Fore.CYAN + Style.BRIGHT}Wait {hours:02}:{mins:02}:{secs:02}", end='\r')
        time.sleep(1)
        seconds -= 1
    print("Wait 00:00:00          ", end='\r')

def load_tokens(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def get_headers(token):
    return {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": f"Bearer {token}",
        "content-type": "application/json",
        "sec-ch-ua": "\"Chromium\";v=\"111\", \"Not(A:Brand\";v=\"8\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site"
    }

def login(token):
    url = "https://api.thevertus.app/users/get-data"
    headers = get_headers(token)
    body = {}

    try:
        response = requests.post(url, headers=headers, json=body, allow_redirects=True)
        response.raise_for_status()
        data = response.json()
        balance = int(data.get("user").get("balance"))/10**18
        farm_b = data.get("user").get("vertStorage")/10**18
        pph = data.get("user").get("valuePerHour")/10**18
        eo = data.get("user").get("earnedOffline")/10**18
        print(Fore.GREEN + Style.BRIGHT + f"Vert Balance: {balance:.3f} | Earned Offline: {eo:.4f}")
        print(Fore.GREEN + Style.BRIGHT + f"Farm Balance: {farm_b:.5f} | PPH: {pph:.4f}")
    
    except requests.exceptions.RequestException as e:
        print(Fore.RED + Style.BRIGHT + f"Request failed: {e}")

def daily_bonus(token):
    url = "https://api.thevertus.app/users/claim-daily"
    headers = get_headers(token)
    body = {}

    try:
        response = requests.post(url, headers=headers, json=body, allow_redirects=True)
        response.raise_for_status()
        data = response.json()
        
        success = data.get("success")
        n_balance = data.get("balance") / 10**18 if data.get("balance") is not None else 0
        massage = data.get("msg", "")
        reward = data.get("claimed") / 10**18 if data.get("claimed") is not None else 0
        day = data.get("consecutiveDays", 0)
        
        if success:
            print(Fore.GREEN + Style.BRIGHT + f"Day {day} Daily Bonus {reward} Claimed Successfully")
            print(Fore.GREEN + Style.BRIGHT + f"New Balance: {n_balance}")
        else:
            print(Fore.YELLOW + Style.BRIGHT + f"{massage}")
    
    except requests.exceptions.RequestException as e:
        print(Fore.RED + Style.BRIGHT + f"Request failed: {e}")

def ads(token):
    url_1 = "https://api.thevertus.app/missions/check-adsgram"
    headers = get_headers(token)
    body = {}

    try:
        response = requests.post(url_1, headers=headers, json=body, allow_redirects=True)
        response.raise_for_status()
        data = response.json()
        isSuccess = data.get("isSuccess")
        massage = data.get("msg")

        if isSuccess:
            print(Fore.CYAN + Style.BRIGHT + "Ads Reward Claiming.....")
            time.sleep(30)
            url_2 = "https://api.thevertus.app/missions/complete-adsgram"
            body_2 = {}
            response_2 = requests.post(url_2, headers=headers, json=body_2, allow_redirects=True)
            response_2.raise_for_status()
            data_2 = response_2.json()
            
            isSuccess = data_2.get("isSuccess")
            new_balance = data_2.get("newBalance") / 10**18 if data_2.get("newBalance") is not None else 0
            total_claim = data_2.get("completion")
            
            if isSuccess:
                new_balance = f"{new_balance:.3f}"  # Format balance with 3 decimal places
                print(Fore.GREEN + Style.BRIGHT + "Ads Reward Claimed Successfully")
                print(Fore.GREEN + Style.BRIGHT + f"New Balance: {new_balance} | Total Claim: {total_claim} times")
            else:
                print(Fore.YELLOW + Style.BRIGHT + f"{data_2}")
                      
        else:
            print(Fore.YELLOW + Style.BRIGHT + f"{massage}")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + Style.BRIGHT + f"Request failed: {e}")        

def get_task(token):
    get_task_url = "https://api.thevertus.app/missions/get"
    headers = get_headers(token)
    body = {"isPremium": False, "languageCode": "en"}
    id_list = []
    task_title = []

    try:
        response = requests.post(get_task_url, headers=headers, json=body, allow_redirects=True)
        response.raise_for_status()
        data = response.json()

        groups = data.get('groups', [])
        for group in groups:
            for mission_list in group.get('missions', []):
                for mission in mission_list:
                    id_list.append(mission.get('_id'))
                    task_title.append(mission.get('title'))

        sponsors = data.get('sponsors', [])
        for sponsor_list in sponsors:
            for sponsor in sponsor_list:
                id_list.append(sponsor.get('_id'))
                task_title.append(sponsor.get('title'))

        sponsors2 = data.get('sponsors2', [])
        if isinstance(sponsors2, list):
            for sponsor2 in sponsors2:
                if isinstance(sponsor2, dict):
                    id_list.append(sponsor2.get('_id'))
                    task_title.append(sponsor2.get('title'))
                else:
                    print(Fore.YELLOW + Style.BRIGHT + f"Unexpected type in sponsors2: {type(sponsor2)}")
        else:
            print(Fore.YELLOW + Style.BRIGHT + f"Unexpected type for sponsors2: {type(sponsors2)}")

        communitys = data.get('community', [])
        for community_list in communitys:
            for community in community_list:
                id_list.append(community.get('_id'))
                task_title.append(community.get('title'))

        recommendations = data.get('recommendations', {}).get('missions', [])
        for mission in recommendations:
            id_list.append(mission.get('_id'))
            task_title.append(mission.get('title'))

        return id_list, task_title

    except requests.exceptions.RequestException as e:
        print(Fore.RED + Style.BRIGHT + f"Request failed: {e}")
        return [], []

def comp_task(token, id_list, task_title):
    url = "https://api.thevertus.app/missions/complete"
    headers = get_headers(token)
    
    initial_balance = None
    try:
        response = requests.post("https://api.thevertus.app/users/get-data", headers=headers, json={}, allow_redirects=True)
        response.raise_for_status()
        data = response.json()
        initial_balance = int(data.get("user").get("balance")) / 10**18
    except requests.exceptions.RequestException as e:
        print(Fore.RED + Style.BRIGHT + f"Failed to get initial balance: {e}")
        return
    
    for mission_id, title in zip(id_list, task_title):
        body = {"missionId": mission_id}
        
        try:
            response = requests.post(url, headers=headers, json=body, allow_redirects=True)
            response.raise_for_status()
            data = response.json()
            new_balance = data.get("newBalance") / 10**18
            
            if new_balance > initial_balance:
                print(Fore.GREEN + Style.BRIGHT + f"Task Complete: {title}")
                print(Fore.GREEN + Style.BRIGHT + f"New Balance: {new_balance:.4f}")
            else:
                print(Fore.YELLOW + Style.BRIGHT + f"Task Already Completed: {title}")

        except requests.exceptions.RequestException as e:
            print(Fore.RED + Style.BRIGHT + f"Request failed for missionId {mission_id} ({title}): {e}")
            if response:
                print(Fore.RED + Style.BRIGHT + f"Response content: {response.text}")

def upgrade_farm(token):
    url = "https://api.thevertus.app/users/upgrade"
    headers = get_headers(token)
    body = {"upgrade": "farm"}

    try:
        response = requests.post(url, headers=headers, json=body, allow_redirects=True)
        response.raise_for_status()
        data = response.json()
        
        success = data.get("success")
        message = data.get("msg")
        
        abilities = data.get("abilities", {})
        farm = abilities.get("farm", {})
        farm_lvl = farm.get("level", "Unknown")
        farm_des = farm.get("description", "No description available")
        new_balance = data.get("newBalance")
        
        a_b = new_balance / 10**18 if new_balance is not None else 0
        
        if success:
            print(Fore.GREEN + Style.BRIGHT + "Farm Upgrade Successful")
            print(Fore.GREEN + Style.BRIGHT + f"Farm New Level: {farm_lvl} | Farm Ability: {farm_des}")
            print(Fore.GREEN + Style.BRIGHT + f"Available Balance: {a_b:.3f}")
        else:
            print(Fore.RED + Style.BRIGHT + f"Upgrade Failed: {message}")
    
    except requests.exceptions.RequestException as e:
        print(Fore.RED + Style.BRIGHT + f"Request failed: {e}")

def upgrade_storage(token):
    url = "https://api.thevertus.app/users/upgrade"
    headers = get_headers(token)
    body = {"upgrade": "storage"}

    try:
        response = requests.post(url, headers=headers, json=body, allow_redirects=True)
        response.raise_for_status()
        data = response.json()
        
        success = data.get("success")
        message = data.get("msg")
        
        abilities = data.get("abilities", {})
        storage = abilities.get("storage", {})
        storage_lvl = storage.get("level", "Unknown")
        storage_des = storage.get("description", "No description available")
        new_balance = data.get("newBalance")
        
        a_b = new_balance / 10**18 if new_balance is not None else 0
        
        if success:
            print(Fore.GREEN + Style.BRIGHT + "Storage Upgrade Successful")
            print(Fore.GREEN + Style.BRIGHT + f"Storage New Level: {storage_lvl} | Storage Ability: {storage_des}")
            print(Fore.GREEN + Style.BRIGHT + f"Available Balance: {a_b:.3f}")
        else:
            print(Fore.RED + Style.BRIGHT + f"Upgrade Failed: {message}")
    
    except requests.exceptions.RequestException as e:
        print(Fore.RED + Style.BRIGHT + f"Request failed: {e}")

def upgrade_population(token):
    url = "https://api.thevertus.app/users/upgrade"
    headers = get_headers(token)
    body = {"upgrade": "population"}

    try:
        response = requests.post(url, headers=headers, json=body, allow_redirects=True)
        response.raise_for_status()
        data = response.json()
        
        success = data.get("success")
        message = data.get("msg")
        
        abilities = data.get("abilities", {})
        population = abilities.get("population", {})
        population_lvl = population.get("level", "Unknown")
        population_des = population.get("description", "No description available")
        new_balance = data.get("newBalance")
        
        a_b = new_balance / 10**18 if new_balance is not None else 0
        
        if success:
            print(Fore.GREEN + Style.BRIGHT + "Population Upgrade Successful")
            print(Fore.GREEN + Style.BRIGHT + f"Population New Level: {population_lvl} | Population Ability: {population_des}")
            print(Fore.GREEN + Style.BRIGHT + f"Available Balance: {a_b:.3f}")
        else:
            print(Fore.RED + Style.BRIGHT + f"Upgrade Failed: {message}")
    
    except requests.exceptions.RequestException as e:
        print(Fore.RED + Style.BRIGHT + f"Request failed: {e}")

def get_cards(token):
    url = "https://api.thevertus.app/upgrade-cards"
    headers = get_headers(token)
    card_details = []

    try:
        response = requests.get(url, headers=headers, allow_redirects=True)
        response.raise_for_status()
        data = response.json()
        
        for category in ['economyCards', 'militaryCards', 'scienceCards']:
            for card in data.get(category, []):
                card_id = card['_id']
                card_name = card.get('cardName', 'Unknown Name')
                card_details.append((card_id, card_name))
    
    except requests.exceptions.RequestException as e:
        print(Fore.RED + Style.BRIGHT + f"Request failed: {e}")

    return card_details

def post_card_upgrade(card_id, card_name, token):
    url = "https://api.thevertus.app/upgrade-cards/upgrade"
    headers = {'Authorization': f'Bearer {token}'}
    body = {"cardId": card_id}
    
    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        data = response.json()
        
        success = data.get("isSuccess")
        message = data.get("msg")
        
        balance_str = data.get("balance")
        new_pph_str = data.get("newValuePerHour")
        
        # Ensure balance and new_pph are not None and are valid numbers
        if balance_str is not None:
            try:
                a_balance = int(balance_str) / 10**18
            except (ValueError, TypeError):
                a_balance = "Invalid balance value"
        else:
            a_balance = "Balance not provided"
        
        if new_pph_str is not None:
            try:
                new_pph = int(new_pph_str) / 10**18
            except (ValueError, TypeError):
                new_pph = "Invalid new PPH value"
        else:
            new_pph = "New PPH not provided"
        
        if success:
            print(Fore.GREEN + Style.BRIGHT + f"{card_name} Card Upgrade Successful")
            print(Fore.GREEN + Style.BRIGHT + f"Available Balance: {a_balance}")
            print(Fore.GREEN + Style.BRIGHT + f"New PPH: {new_pph}")
        else:
            print(Fore.RED + Style.BRIGHT + f"{message}")
            print(Fore.RED + Style.BRIGHT + f"{card_name} Card Upgrade Failed")
        
    except requests.exceptions.RequestException as e:
        print(Fore.RED + Style.BRIGHT + f"Request failed for card ID {card_id}, Card Name: {card_name}: {e}")

def main():
    clear_terminal()
    art()
    
    run_task = input(Fore.CYAN + "Do you want to complete tasks? (y/n): ").strip().lower()
    run_uf = input(Fore.CYAN + "Do you want to Upgrade Farm? (y/n): ").strip().lower()
    run_us = input(Fore.CYAN + "Do you want to Upgrade Storage? (y/n): ").strip().lower()
    run_up = input(Fore.CYAN + "Do you want to Upgrade Population? (y/n): ").strip().lower()
    run_cards = input(Fore.CYAN + "Do you want to Upgrade Cards? (y/n): ").strip().lower()
    
    clear_terminal()
    art()
    
    while True:
        tokens = load_tokens('data.txt')
        
        if not tokens:
            print(Fore.RED + Style.BRIGHT + "No tokens found.")
            return
    
        for i, token in enumerate(tokens, start=1):
            print(Fore.CYAN + Style.BRIGHT + f"------Account No.{i}------")
            login(token)
            daily_bonus(token)
            ads(token)
            
            if run_task == 'y':
                task_ids, task_titles = get_task(token)
                if task_ids:
                    comp_task(token, task_ids, task_titles)
                else:
                    print(Fore.YELLOW + Style.BRIGHT + "No tasks available.")
                time.sleep(2)
            
            if run_uf == 'y':
                upgrade_farm(token)
            
            if run_us == 'y':
                upgrade_storage(token)
            
            if run_up == 'y':
                upgrade_population(token)
                
            if run_cards == 'y':
                card_details = get_cards(token)
                for card_id, card_name in card_details:
                    post_card_upgrade(card_id, card_name, token)
                            
        countdown_timer(1 * 15 * 60)
        clear_terminal()
        art()

if __name__ == "__main__":
    main()
