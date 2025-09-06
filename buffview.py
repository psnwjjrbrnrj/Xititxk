import requests
from colorama import Fore, init

init(autoreset=True)

API_URL = "https://chaysub.vn/api/v2"

def check_balance(api_key):
    data = {"key": api_key, "action": "balance"}
    r = requests.post(API_URL, data=data)
    return r.json()

def create_order(api_key, service, link, quantity):
    data = {
        "key": api_key,
        "action": "add",
        "service": service,
        "link": link,
        "quantity": quantity
    }
    r = requests.post(API_URL, data=data)
    return r.json()

def order_status(api_key, order_id):
    data = {"key": api_key, "action": "status", "order": order_id}
    r = requests.post(API_URL, data=data)
    return r.json()

def main():
    print(Fore.CYAN + "=== TOOL CHAYSUB.VN API V2 ===")

    api_key = input(Fore.YELLOW + "🔑 Nhập API Key của bạn: ")

    while True:
        print(Fore.GREEN + "\n--- MENU ---")
        print("1. Xem số dư")
        print("2. Tạo đơn hàng")
        print("3. Kiểm tra đơn hàng")
        print("4. Thoát")

        choice = input(Fore.CYAN + "Chọn: ")

        if choice == "1":
            result = check_balance(api_key)
            print(Fore.MAGENTA + f"Kết quả: {result}")

        elif choice == "2":
            service = input("Nhập ID dịch vụ: ")
            link = input("Nhập link: ")
            quantity = input("Nhập số lượng: ")
            result = create_order(api_key, service, link, quantity)
            print(Fore.MAGENTA + f"Kết quả: {result}")

        elif choice == "3":
            order_id = input("Nhập Order ID: ")
            result = order_status(api_key, order_id)
            print(Fore.MAGENTA + f"Kết quả: {result}")

        elif choice == "4":
            print("Thoát...")
            break

        else:
            print(Fore.RED + "❌ Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
