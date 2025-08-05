#!/usr/bin/env python3
import os
from colorama import Fore, init
from extract_colors import CSSColorExtractor
from utils.display import animated_title, show_menu
from utils.single_extract import extract_single_website
from utils.batch_extract import batch_extract
from utils.palette_generator import color_palette_generator
from utils.color_stats import color_statistics
from utils.swatch_exporter import export_html_swatches
from utils.settings import settings_menu

# Initialize colorama
init(autoreset=True)

class ColorExtractorGUI:
    def __init__(self):
        self.extractor = CSSColorExtractor()
        self.output_dir = "Extracted Colours"
        self.ensure_output_dir()
        
    def ensure_output_dir(self):
        """Create output directory if it doesn't exist"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def run(self):
        """Main application loop"""
        while True:
            animated_title()
            show_menu()
            
            choice = input(f"{Fore.YELLOW}Select option (0-6): {Fore.WHITE}")
            
            if choice == '0':
                print(f"\n{Fore.GREEN}Thanks for using CSS Color Extractor!")
                print(f"{Fore.CYAN}Follow ACT91 on GitHub: https://github.com/ACT91")
                break
            elif choice == '1':
                extract_single_website(self.extractor, self.output_dir)
            elif choice == '2':
                batch_extract(self.extractor, self.output_dir)
            elif choice == '3':
                color_palette_generator(self.extractor, self.output_dir)
            elif choice == '4':
                color_statistics(self.extractor)
            elif choice == '5':
                export_html_swatches(self.extractor, self.output_dir)
            elif choice == '6':
                settings_menu(self.extractor)
            else:
                print(f"{Fore.RED}X Invalid option!")

if __name__ == "__main__":
    app = ColorExtractorGUI()
    app.run()