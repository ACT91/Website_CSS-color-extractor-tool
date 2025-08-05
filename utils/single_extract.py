import os
from colorama import Fore

def extract_single_website(extractor, output_dir):
    """Extract colors from single website"""
    print(f"\n{Fore.GREEN}EXTRACT COLORS FROM WEBSITE")
    print("-" * 40)
    
    url = input(f"{Fore.YELLOW}Enter website URL: {Fore.WHITE}")
    if not url:
        print(f"{Fore.RED}X No URL provided!")
        return
    
    use_selenium = input(f"{Fore.YELLOW}Use Selenium for JS sites? (y/n): {Fore.WHITE}").lower() == 'y'
    extractor.use_selenium = use_selenium
    
    print(f"\n{Fore.CYAN}Extracting colors...")
    colors = extractor.extract_colors(url)
    
    if colors:
        print(f"\n{Fore.GREEN}✓ Found {len(colors)} unique colors:")
        display_colors(colors)
        
        save = input(f"\n{Fore.YELLOW}Save results? (y/n): {Fore.WHITE}").lower() == 'y'
        if save:
            filename = input(f"{Fore.YELLOW}Filename (.txt/.json): {Fore.WHITE}")
            if filename:
                filepath = os.path.join(output_dir, filename)
                extractor.save_colors(colors, filepath)
    else:
        print(f"{Fore.RED}X No colors found!")
    
    input(f"\n{Fore.CYAN}Press Enter to continue...")

def display_colors(colors):
    """Display colors with visual representation"""
    for i, color in enumerate(colors):
        if i % 3 == 0:
            print()
        if color.startswith('#'):
            print(f"{Fore.WHITE}  {color:<20}", end="")
        elif 'rgb' in color:
            print(f"{Fore.CYAN}  {color:<20}", end="")
        else:
            print(f"{Fore.YELLOW}  {color:<20}", end="")