import os
import json
from colorama import Fore

def batch_extract(extractor, output_dir):
    """Batch extract from multiple URLs"""
    print(f"\n{Fore.YELLOW}BATCH EXTRACT FROM MULTIPLE URLS")
    print("-" * 40)
    
    urls = []
    print(f"{Fore.CYAN}Enter URLs (empty line to finish):")
    while True:
        url = input(f"{Fore.WHITE}URL: ")
        if not url:
            break
        urls.append(url)
    
    if not urls:
        print(f"{Fore.RED}X No URLs provided!")
        return
    
    all_colors = set()
    results = {}
    
    for i, url in enumerate(urls, 1):
        print(f"\n{Fore.CYAN}Processing {i}/{len(urls)}: {url}")
        colors = extractor.extract_colors(url)
        results[url] = colors
        all_colors.update(colors)
    
    print(f"\n{Fore.GREEN}✓ Batch extraction complete!")
    print(f"{Fore.YELLOW}Total unique colors: {len(all_colors)}")
    
    # Save batch results
    batch_file = os.path.join(output_dir, 'batch_results.json')
    with open(batch_file, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"{Fore.GREEN}Results saved to {batch_file}")
    
    input(f"\n{Fore.CYAN}Press Enter to continue...")