from bot import BasicBot
import getpass

def get_credentials():
    print("Enter your Binance Testnet API credentials.")
    api_key = getpass.getpass("API Key: ")
    api_secret = getpass.getpass("API Secret: ")
    return api_key, api_secret

def main():
    api_key, api_secret = get_credentials()
    bot = BasicBot(api_key, api_secret)
    print("Welcome to Binance Testnet Trading Bot!")

    while True:
        print("1. Place Market Order")
        print("2. Place Limit Order")
        print("0. Exit")
        choice = input("Choose [1/2/0]: ")

        if choice == '0':
            print("Exiting. Good luck!")
            break

        symbol = input("Enter symbol (e.g., BTCUSDT): ")
        side = input("Buy or Sell [BUY/SELL]: ").upper()
        quantity = float(input("Enter quantity: "))

        if choice == '1':
            result = bot.place_order(symbol, side, 'MARKET', quantity)
        elif choice == '2':
            price = float(input("Enter limit price: "))
            result = bot.place_order(symbol, side, 'LIMIT', quantity, price)
        else:
            print("Invalid option.")
            continue

        print("Result:", result)

if __name__ == "__main__":
    main()
