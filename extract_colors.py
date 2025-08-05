#!/usr/bin/env python3
import re
import json
import argparse
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup

class CSSColorExtractor:
    def __init__(self, use_selenium=False):
        self.colors = set()
        self.use_selenium = use_selenium
        
        # Color regex patterns
        self.hex_pattern = re.compile(r'#[0-9a-fA-F]{3,8}\b')
        self.rgb_pattern = re.compile(r'rgba?\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*(?:,\s*[\d.]+)?\s*\)')
        self.hsl_pattern = re.compile(r'hsla?\(\s*\d+\s*,\s*\d+%\s*,\s*\d+%\s*(?:,\s*[\d.]+)?\s*\)')
    
    def extract_colors_from_text(self, text):
        """Extract all color values from CSS text"""
        if not text:
            return
            
        # Find HEX colors
        hex_colors = self.hex_pattern.findall(text)
        self.colors.update(hex_colors)
        
        # Find RGB/RGBA colors
        rgb_colors = self.rgb_pattern.findall(text)
        self.colors.update(rgb_colors)
        
        # Find HSL/HSLA colors
        hsl_colors = self.hsl_pattern.findall(text)
        self.colors.update(hsl_colors)
    
    def fetch_css_file(self, url, base_url):
        """Fetch external CSS file content"""
        try:
            css_url = urljoin(base_url, url)
            response = requests.get(css_url, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"Failed to fetch CSS: {css_url} - {e}")
            return ""
    
    def extract_with_requests(self, url):
        """Extract colors using requests + BeautifulSoup"""
        try:
            response = requests.get(url, timeout=15)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract from inline <style> blocks
            for style_tag in soup.find_all('style'):
                self.extract_colors_from_text(style_tag.string)
            
            # Extract from external CSS files
            for link in soup.find_all('link', rel='stylesheet'):
                href = link.get('href')
                if href:
                    css_content = self.fetch_css_file(href, url)
                    self.extract_colors_from_text(css_content)
            
            # Extract from inline style attributes
            for element in soup.find_all(style=True):
                self.extract_colors_from_text(element.get('style'))
                
        except Exception as e:
            print(f"Error with requests method: {e}")
            if self.use_selenium:
                print("Falling back to Selenium...")
                self.extract_with_selenium(url)
    
    def extract_with_selenium(self, url):
        """Fallback: Extract colors using Selenium for JS-rendered content"""
        try:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options
            
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            
            # Additional options for Linux/Android/Termux
            if IS_LINUX or IS_ANDROID or IS_TERMUX:
                options.add_argument('--disable-gpu')
                options.add_argument('--disable-extensions')
                options.add_argument('--disable-plugins')
                options.add_argument('--remote-debugging-port=9222')
            
            driver = webdriver.Chrome(options=options)
            driver.get(url)
            
            # Get page source after JS execution
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            
            # Extract from inline styles
            for style_tag in soup.find_all('style'):
                self.extract_colors_from_text(style_tag.string)
            
            # Extract from style attributes
            for element in soup.find_all(style=True):
                self.extract_colors_from_text(element.get('style'))
            
            # Get computed styles for all elements
            elements = driver.find_elements("xpath", "//*")
            for element in elements:
                try:
                    color = element.value_of_css_property('color')
                    bg_color = element.value_of_css_property('background-color')
                    border_color = element.value_of_css_property('border-color')
                    
                    for prop_color in [color, bg_color, border_color]:
                        if prop_color and prop_color != 'rgba(0, 0, 0, 0)':
                            self.extract_colors_from_text(prop_color)
                except:
                    continue
            
            driver.quit()
            
        except ImportError:
            print("Selenium not installed. Install with: pip install selenium")
        except Exception as e:
            print(f"Selenium extraction failed: {e}")
    
    def extract_colors(self, url):
        """Main method to extract colors from URL"""
        print(f"Extracting colors from: {url}")
        self.colors.clear()
        
        # Validate URL
        parsed = urlparse(url)
        if not parsed.scheme:
            url = 'https://' + url
        
        self.extract_with_requests(url)
        
        # Filter and sort colors
        filtered_colors = sorted([color for color in self.colors if color.strip()])
        return filtered_colors
    
    def save_colors(self, colors, filename):
        """Save colors to file"""
        import os
        import json
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        if filename.endswith('.json'):
            with open(filename, 'w') as f:
                json.dump(colors, f, indent=2)
        else:
            with open(filename, 'w') as f:
                f.write('\n'.join(colors))
        print(f"Colors saved to: {filename}")

def main():
    parser = argparse.ArgumentParser(description='Extract CSS colors from a website')
    parser.add_argument('url', help='Website URL to extract colors from')
    parser.add_argument('-o', '--output', help='Output file (.txt or .json)')
    parser.add_argument('-s', '--selenium', action='store_true', 
                       help='Use Selenium fallback for JS-rendered sites')
    
    args = parser.parse_args()
    
    extractor = CSSColorExtractor(use_selenium=args.selenium)
    colors = extractor.extract_colors(args.url)
    
    if colors:
        print(f"\nFound {len(colors)} unique colors:")
        for color in colors:
            print(f"  {color}")
        
        if args.output:
            extractor.save_colors(colors, args.output)
    else:
        print("No colors found.")

if __name__ == "__main__":
    main()