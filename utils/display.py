import os
import time
import platform
from colorama import Fore

# Platform detection
IS_TERMUX = 'com.termux' in os.environ.get('PREFIX', '')
IS_ANDROID = 'ANDROID_ROOT' in os.environ or 'ANDROID_DATA' in os.environ
IS_WINDOWS = platform.system() == 'Windows'

def clear_screen():
    """Cross-platform screen clearing"""
    if IS_WINDOWS:
        os.system('cls')
    else:
        os.system('clear')
        if IS_TERMUX or IS_ANDROID:
            print('\033[2J\033[H', end='')

def animated_title():
    """Display animated ASCII art title with gradient colors"""
    logo = """
\033[91m  ██████  ███████ ███████      \033[92m ██████  ██████  ██       ██████  ██████  
\033[91m ██       ██      ██           \033[92m██      ██    ██ ██      ██    ██ ██   ██ 
\033[91m ██       ███████ ███████      \033[92m██      ██    ██ ██      ██    ██ ██████  
\033[91m ██            ██      ██      \033[92m██      ██    ██ ██      ██    ██ ██   ██ 
\033[91m  ██████  ███████ ███████      \033[92m ██████  ██████  ███████  ██████  ██   ██ 
\033[0m
\033[93m ███████ ██   ██ ████████ ██████   █████   ██████ ████████  ██████  ██████  
\033[93m ██       ██ ██     ██    ██   ██ ██   ██ ██         ██    ██    ██ ██   ██ 
\033[93m █████     ███      ██    ██████  ███████ ██         ██    ██    ██ ██████  
\033[93m ██       ██ ██     ██    ██   ██ ██   ██ ██         ██    ██    ██ ██   ██ 
\033[93m ███████ ██   ██    ██    ██   ██ ██   ██  ██████    ██     ██████  ██   ██ 
\033[0m
\033[96m                        CSS Color Extraction Tool\033[0m
\033[95m                           Made by ACT91\033[0m
\033[94m                     GitHub: https://github.com/ACT91\033[0m
\033[94m              Don't Forget To Leave a Star on this Project\033[0m
"""
    
    iterations = 1 if IS_TERMUX else 2
    
    for i in range(iterations):
        clear_screen()
        print(logo)
        if iterations > 1:
            time.sleep(0.8)

def show_menu():
    """Display main menu options"""
    print(f"{Fore.CYAN}MAIN MENU:")
    print(f"{Fore.WHITE}1. {Fore.GREEN}Extract Colors from Website")
    print(f"{Fore.WHITE}2. {Fore.YELLOW}Batch Extract from Multiple URLs")
    print(f"{Fore.WHITE}3. {Fore.BLUE}Color Palette Generator")
    print(f"{Fore.WHITE}4. {Fore.MAGENTA}Color Statistics & Analysis")
    print(f"{Fore.WHITE}5. {Fore.CYAN}Export Color Swatches (HTML)")
    print(f"{Fore.WHITE}6. {Fore.RED}Settings")
    print(f"{Fore.WHITE}0. {Fore.RED}Exit")
    print("-" * 40)