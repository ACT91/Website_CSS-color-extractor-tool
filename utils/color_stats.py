from colorama import Fore

def color_statistics(extractor):
    """Color statistics and analysis"""
    print(f"\n{Fore.MAGENTA}COLOR STATISTICS & ANALYSIS")
    print("-" * 40)
    
    url = input(f"{Fore.YELLOW}Enter website URL: {Fore.WHITE}")
    if not url:
        return
    
    colors = extractor.extract_colors(url)
    if not colors:
        print(f"{Fore.RED}X No colors found!")
        return
    
    # Analyze colors
    hex_colors = [c for c in colors if c.startswith('#')]
    rgb_colors = [c for c in colors if c.startswith('rgb')]
    hsl_colors = [c for c in colors if c.startswith('hsl')]
    
    print(f"\n{Fore.CYAN}COLOR ANALYSIS:")
    print(f"{Fore.WHITE}Total colors: {Fore.GREEN}{len(colors)}")
    print(f"{Fore.WHITE}HEX colors: {Fore.YELLOW}{len(hex_colors)}")
    print(f"{Fore.WHITE}RGB colors: {Fore.BLUE}{len(rgb_colors)}")
    print(f"{Fore.WHITE}HSL colors: {Fore.MAGENTA}{len(hsl_colors)}")
    
    # Most common color types
    if hex_colors:
        print(f"\n{Fore.YELLOW}HEX Colors:")
        for color in hex_colors[:10]:  # Show first 10
            print(f"  {color}")
    
    input(f"\n{Fore.CYAN}Press Enter to continue...")