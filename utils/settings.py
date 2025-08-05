from colorama import Fore

def settings_menu(extractor):
    """Settings menu"""
    print(f"\n{Fore.RED}SETTINGS")
    print("-" * 40)
    print(f"{Fore.WHITE}1. Toggle Selenium support: {Fore.GREEN if extractor.use_selenium else Fore.RED}{'ON' if extractor.use_selenium else 'OFF'}")
    print(f"{Fore.WHITE}2. View GitHub Profile")
    print(f"{Fore.WHITE}0. Back to main menu")
    
    choice = input(f"\n{Fore.YELLOW}Select option: {Fore.WHITE}")
    
    if choice == '1':
        extractor.use_selenium = not extractor.use_selenium
        status = "enabled" if extractor.use_selenium else "disabled"
        print(f"{Fore.GREEN}✓ Selenium support {status}")
    elif choice == '2':
        print(f"\n{Fore.CYAN}GitHub: {Fore.GREEN}https://github.com/ACT91")
        print(f"{Fore.YELLOW}Follow for more awesome tools!")
    
    input(f"\n{Fore.CYAN}Press Enter to continue...")