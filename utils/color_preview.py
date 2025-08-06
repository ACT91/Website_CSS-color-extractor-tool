import os
import json
from colorama import Fore

def preview_colors(output_dir):
    """Preview colors from extracted files"""
    print(f"\n{Fore.BLUE}PREVIEW COLORS (From Extracted Color [.txt / .json])")
    print("-" * 40)
    
    # Check if Extracted Colours folder exists
    if not os.path.exists(output_dir):
        print(f"{Fore.RED}X No extracted colors folder found!")
        return
    
    # List available files
    files = [f for f in os.listdir(output_dir) if f.endswith(('.txt', '.json'))]
    if not files:
        print(f"{Fore.RED}X No color files found in {output_dir}")
        return
    
    print(f"{Fore.CYAN}Available files:")
    for file in files:
        print(f"  {file}")
    
    filename = input(f"\n{Fore.YELLOW}Enter filename: {Fore.WHITE}")
    if not filename:
        return
    
    filepath = os.path.join(output_dir, filename)
    if not os.path.exists(filepath):
        print(f"{Fore.RED}X File not found: {filename}")
        return
    
    # Read colors from file
    colors = read_colors_from_file(filepath)
    if not colors:
        print(f"{Fore.RED}X No colors found in file!")
        return
    
    print(f"\n{Fore.GREEN}✓ Found {len(colors)} colors in {filename}")
    
    # Generate HTML preview
    html_content = generate_preview_html(colors, filename)
    
    # Create Previewed Colors folder
    preview_dir = "Previewed Colors"
    if not os.path.exists(preview_dir):
        os.makedirs(preview_dir)
    
    # Save HTML preview
    base_name = os.path.splitext(filename)[0]
    preview_filename = f"{base_name}.html"
    preview_path = os.path.join(preview_dir, preview_filename)
    
    with open(preview_path, 'w') as f:
        f.write(html_content)
    
    print(f"{Fore.GREEN}✓ Color preview saved to {preview_path}")
    input(f"\n{Fore.CYAN}Press Enter to continue...")

def read_colors_from_file(filepath):
    """Read colors from .txt or .json file"""
    colors = []
    
    try:
        if filepath.endswith('.json'):
            with open(filepath, 'r') as f:
                data = json.load(f)
                if isinstance(data, list):
                    colors = data
                elif isinstance(data, dict):
                    # Handle batch results format
                    for url_colors in data.values():
                        colors.extend(url_colors)
        else:  # .txt file
            with open(filepath, 'r') as f:
                colors = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"{Fore.RED}Error reading file: {e}")
    
    return colors

def generate_preview_html(colors, source_filename):
    """Generate HTML preview of colors"""
    html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Color Preview - {source_filename}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
        }}
        .header {{
            text-align: center;
            margin-bottom: 30px;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .header h1 {{
            color: #333;
            margin: 0;
            font-size: 2.5em;
        }}
        .header p {{
            color: #666;
            margin: 10px 0 0 0;
            font-size: 1.1em;
        }}
        .color-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }}
        .color-card {{
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }}
        .color-card:hover {{
            transform: translateY(-5px);
        }}
        .color-display {{
            height: 120px;
            position: relative;
            border-bottom: 1px solid #eee;
        }}
        .color-info {{
            padding: 15px;
            text-align: center;
        }}
        .color-value {{
            font-family: 'Courier New', monospace;
            font-size: 16px;
            font-weight: bold;
            color: #333;
            margin: 0;
            word-break: break-all;
        }}
        .color-type {{
            font-size: 12px;
            color: #888;
            margin-top: 5px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        .footer {{
            text-align: center;
            margin-top: 40px;
            padding: 20px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .footer p {{
            margin: 5px 0;
            color: #666;
        }}
        .footer a {{
            color: #007bff;
            text-decoration: none;
        }}
        .footer a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Color Preview</h1>
        <p>Extracted from: <strong>{source_filename}</strong></p>
        <p>Total Colors: <strong>{len(colors)}</strong></p>
    </div>
    
    <div class="color-grid">
"""
    
    for i, color in enumerate(colors, 1):
        # Determine color type
        if color.startswith('#'):
            color_type = 'HEX'
        elif color.startswith('rgb'):
            color_type = 'RGB/RGBA'
        elif color.startswith('hsl'):
            color_type = 'HSL/HSLA'
        else:
            color_type = 'OTHER'
        
        # Only display colors that browsers can render
        display_color = color if (color.startswith('#') or color.startswith('rgb') or color.startswith('hsl')) else '#cccccc'
        
        html += f"""
        <div class="color-card">
            <div class="color-display" style="background-color: {display_color};"></div>
            <div class="color-info">
                <p class="color-value">{color}</p>
                <p class="color-type">{color_type}</p>
            </div>
        </div>
"""
    
    html += f"""
    </div>
    
    <div class="footer">
        <p><em>Generated by CSS Color Extractor - Made by ACT91</em></p>
        <p><a href="https://github.com/ACT91" target="_blank">GitHub: https://github.com/ACT91</a></p>
        <p>Don't forget to leave a star on this project!</p>
    </div>
</body>
</html>"""
    
    return html