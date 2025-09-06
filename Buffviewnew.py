import os
import requests
import concurrent.futures
from colorama import init, Fore

init(autoreset=True)

API_URL = "https://chaysub.vn/api/v2"
TOKEN_FILE = "api_key.txt"

total_view = 0
success_count = 0
fail_count = 0

def get_api_key():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r", encoding="utf-8") as f:
            return f.read().strip()
    else:
        key = input(Fore.CYAN + " Nhập API Key: ").strip()
        with open(TOKEN_FILE, "w", encoding="utf-8") as f:
            f.write(key)
        return key

def get_services(api_key):
    data = {"key": api_key, "action": "services"}
    resp = requests.post(API_URL, data=data, timeout=30)
    return resp.json() if resp.status_code == 200 else {}

def add_order(api_key, service_id, link, quantity):
    data = {
        "key": api_key,
        "action": "add",
        "service": service_id,
        "link": link,
        "quantity": quantity
    }
    resp = requests.post(API_URL, data=data, timeout=30)
    return resp.status_code, resp.json()

def spam_views(api_key, service_id, link, quantity, threads=10):
    global total_view, success_count, fail_count
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [
            executor.submit(add_order, api_key, service_id, link, quantity)
            for _ in range(threads)
        ]
        for f in futures:
            status, result = f.result()
            if status == 200 and result.get("order"):
                total_view += int(quantity)
                success_count += 1
                print(Fore.GREEN + f"✅ Success | Total view: {total_view}")
            else:
                fail_count += 1
                print(Fore.RED + f"❌ Fail | {result}")

if __name__ == "__main__":
    api_key = get_api_key()
    services = get_services(api_key)
    print("Available services:", services)

    service_id = input(Fore.CYAN + "Enter service ID: ").strip()
    link = input(Fore.CYAN + "Enter link: ").strip()
    quantity = input(Fore.CYAN + "Enter quantity: ").strip()
    threads = int(input(Fore.CYAN + "Threads (default 10): ") or 10)

    while True:
        spam_views(api_key, service_id, link, quantity, threads)
