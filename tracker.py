import csv
from datetime import datetime

# Define the CSV file to store the data
CSV_FILE = 'sports_bets.csv'

# User information
USER_NAME = "Jason C. Klein"
USER_EMAIL = "jasonklein1989@gmail.com"

# Initialize CSV if it doesn't exist
def initialize_csv():
    try:
        with open(CSV_FILE, mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Sport', 'Bet Amount', 'Result', 'Profit', 'User', 'Email'])
    except FileExistsError:
        pass  # The file already exists, no need to reinitialize

# Log a new bet
def log_bet(sport, bet_amount, result):
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    profit = bet_amount if result.lower() == 'win' else -bet_amount
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, sport, bet_amount, result, profit, USER_NAME, USER_EMAIL])

# Get a summary of the betting record
def get_summary():
    total_bets = 0
    total_wins = 0
    total_losses = 0
    total_profit = 0
    
    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_bets += 1
            profit = float(row['Profit'])
            total_profit += profit
            if profit > 0:
                total_wins += 1
            else:
                total_losses += 1
    
    return {
        'total_bets': total_bets,
        'total_wins': total_wins,
        'total_losses': total_losses,
        'total_profit': total_profit
    }

# Main interface
def main():
    initialize_csv()

    while True:
        print(f"\nSports Betting Tracker - {USER_NAME}")
        print(f"Contact: {USER_EMAIL}")
        print("1. Log a new bet")
        print("2. Show summary")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            sport = input("Enter the sport: ")
            bet_amount = float(input("Enter the bet amount: "))
            result = input("Enter the result (win/loss): ")
            log_bet(sport, bet_amount, result)
            print("Bet logged successfully!")
        
        elif choice == '2':
            summary = get_summary()
            print(f"\nTotal Bets: {summary['total_bets']}")
            print(f"Total Wins: {summary['total_wins']}")
            print(f"Total Losses: {summary['total_losses']}")
            print(f"Net Profit: ${summary['total_profit']:.2f}")
        
        elif choice == '3':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
