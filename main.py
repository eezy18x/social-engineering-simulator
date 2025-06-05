# main.py

import os
import time
import webbrowser

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print(r"""
  _____       _          _   _               _             
 / ____|     | |        | | (_)             | |            
| (___   ___ | |__   ___| |_ _  ___  _ __   | |_ ___  _ __ 
 \___ \ / _ \| '_ \ / _ \ __| |/ _ \| '_ \  | __/ _ \| '__|
 ____) | (_) | |_) |  __/ |_| | (_) | | | | | || (_) | |   
|_____/ \___/|_.__/ \___|\__|_|\___/|_| |_|  \__\___/|_|   
                                                          
[+] Social Engineering Attack Simulator (Ethical Use)
    """)

def main_menu():
    while True:
        clear()
        banner()
        print("Select an option:\n")
        print("1. Simulate Phishing Email")
        print("2. Fake Login Page Simulation")
        print("3. Suspicious Pop-up Message")
        print("4. Awareness Tips")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            simulate_phishing()
        elif choice == '2':
            simulate_login_page()
        elif choice == '3':
            simulate_popup()
        elif choice == '4':
            awareness_tips()
        elif choice == '5':
            print("\nExiting... Stay safe!")
            time.sleep(1)
            break
        else:
            input("Invalid choice! Press Enter to continue...")

def simulate_phishing():
    clear()
    print("\n[!] Simulating a phishing email...\n")
    print("From: support@google.com")
    print("Subject: Suspicious login attempt\n")
    print("Dear user,\n\nWe noticed a suspicious login attempt on your Google account.")
    print("Please verify your account here:\n")
    print("http://localhost:5000 (clickable if copied to browser)\n")
    input("Start server with: python3 phishing_server/app.py\nThen press Enter to return to menu.")


def simulate_login_page():
    clear()
    print("\n[!] Launching fake Gmail login page (simulation only)...")
    path = os.path.abspath("attacks/fake_gmail.html")
    webbrowser.open(f"file://{path}")
    input("\n(Press Enter to return to menu)")

def simulate_popup():
    clear()
    print("\n[!] Simulated pop-up alert:\n")
    print("[ALERT] Your system is infected! Click here to clean it now! (simulation)")
    input("\n(Press Enter to return to menu)")

def awareness_tips():
    clear()
    print("\n[💡] Cybersecurity Awareness Tips\n")
    print("- Don't click on suspicious or shortened links.")
    print("- Always check sender email addresses.")
    print("- Use multi-factor authentication (MFA).")
    print("- Avoid using the same password everywhere.")
    print("- Report suspicious emails to your security team.")
    input("\n(Press Enter to return to menu)")

if __name__ == "__main__":
    main_menu()
