import os

def main():
    print("Welcome to Zsploits ScriptHub!") 
    print("No Keys, Ads")
    print("Available categories:")
    print("1. Admin scripts")
    print("2. Exploits")
    print("3. GUI scripts") 
    print("4. Trolling Scripts")
    print("5. Exit")

    while True:
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print("Admin scripts:")
            print("1. Infinite Yield - https://infyiff.github.io/")
            print("2. CMD-X - https://forum.wearedevs.net/t/18841")
            print("3. Fates Admin - https://controlc.com/e09d1126")  
            print("More Coming Soon...")
        elif choice == "2":
            print("Exploits:") 
            # Add more exploit links here 
            print("1. Fluxis - https://fluxteam.net/") 
            print("2. Vega X - https://www.vegax.gg/") 
            print("3. Delta - https://deltaexploits.com/") 
            print("More Coming Soon...")
        elif choice == "3":
            print("GUI scripts:")
            # Add more GUI script links here 
            print("1. Blox Fruits - https://scriptpastebin.com/10847/") 
            print("2. Pet Simulater - https://scriptpastebin.com/10787/") 
            print("3. Punch Wall Simulater - https://scriptpastebin.com/10834/") 
            print("4. King Legacy - https://scriptpastebin.com/11200/") 
            print("5. Anime Warriors Simulater 2 - https://scriptpastebin.com/11166/")  
            print("More Coming Soon...")   
        elif choice == "4": 
            print("Trolling Scripts:") 
            print("1. LostPoint ScriptHub - https://controlc.com/18fe6699") 
            print("2. Universal Trolling Gui - https://rbxscript.com/scripts-copy/UniversalTrollingGui-yNbOA") 
            print("3. Fe-Trolling-GUI - https://github.com/YssHacker/Fe-Trolling-GUI/blob/main/mainscript2") 
            print("4. Troll Script - https://pastebin.com/94YBYXbX") 
            print("5. Kyris Hub - https://pastebin.com/bceJdQer") 
            print("More Coming Soon...")
        elif choice == "5":
            print("Thank you for using Zsploits ScriptHub!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
