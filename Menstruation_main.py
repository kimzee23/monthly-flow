from menstruration_app import UserAccount
from datetime import  datetime, timedelta

def main():
    while True:
        try:
            name = input("Kindly enter your name: ")
            age = int(input("Kindly enter your age: "))
            cycle_length = int(input("Enter your cycle length(e.g.. 28): "))
            period_length = int(input("Enter your period length (3-5): "))
            last_period_date = input("Enter your last period date (yyyy-mm-dd): ")

            userAccount = UserAccount(name, age, cycle_length, period_length, last_period_date)
            break
        except (ValueError, TypeError) as e:
            print(f"Error: {e}. Invalid input please try again.")
    while True:
        print("""\n  The Menstruation Health Checker
                    1. View next period date
                    2. view safe and unsafe (fertile) days
                    3. view pregnancy symptoms
                    4. view menstruation symptoms
                    5. View safe sex tools & tips
                    6. Exit Menstruation HealthChecker 
        """)
        option = input("Enter your option: ")
        match option:
            case "1":
                print(f"\n Next period date: {userAccount.get_next_period_day().strftime('%m/%d/%Y')}")
            case "2":
                print(f"\n safe and unsafe (fertile) days: {userAccount.get_safe_and_unsafe_days()}")
            case "3":
               userAccount.show_pregnancy_symptoms()
            case "4":
                userAccount.show_Mensturation_symptoms()
            case "5":
                userAccount.show_safe_sex_tools()
            case "6":
                print("\n Bye!!, Odabo, stay safe")
                break
            case _:
                print("Invalid choice choice. Enter a number between 1 and 5")

if __name__ == "__main__":
    main()

