# CSS Color Extractor Tool

**Made by ACT91** | [GitHub Profile](https://github.com/ACT91)

A powerful Python tool that extracts all color values from websites with an interactive colorful interface!

## Features

### Core Extraction
- Extract colors from external CSS files
- Extract from inline `<style>` blocks  
- Extract from inline `style` attributes
- Handles relative CSS paths automatically
- Optional Selenium fallback for JS-rendered sites

### Enhanced Features
- **Interactive colorful menu interface**
- **Batch extraction from multiple URLs**
- **Color palette generator (HTML)**
- **Color statistics & analysis**
- **Export color swatches as HTML**
- **Settings & configuration**
- **Save to .txt, .json, or HTML formats**

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/ACT91/Website_CSS-color-extractor-tool.git
cd Website_CSS-color-extractor-tool
```

### Step 2: Install Dependencies

**Windows:**
```bash
pip install -r requirements.txt
```

**Linux/Unix:**
```bash
./install.sh
```

**Termux (Android):**
```bash
./termux_setup.sh
```

## Quick Start

### Launch Interactive Mode

**Windows:**
```bash
python css-color-extractor.py
# Or double-click run.bat
```

**Linux/Unix/Termux:**
```bash
./run.sh
# Or: python3 css-color-extractor.py
```

### Command Line Mode (Original)
```bash
python extract_colors.py https://example.com -o colors.json
```

## Interactive Menu Options

1. **Extract Colors from Website** - Single URL extraction
2. **Batch Extract** - Multiple URLs at once
3. **Color Palette Generator** - Create HTML color palettes
4. **Color Statistics** - Analyze color usage patterns
5. **Export HTML Swatches** - Beautiful color swatch pages
6. **Settings** - Configure Selenium & view GitHub

## Cross-Platform Support

- **Windows** - Full support with .bat launcher
- **Linux** - All distributions supported
- **Termux (Android)** - Optimized for mobile terminals
- **Universal** - Works on any Python-supported platform

## Screenshots

The tool features:
- **Animated colorful title**
- **Color-coded menu options**
- **Visual color display**
- **Multiple export formats**

## Example Output

```
Found 15 unique colors:
  #000000    rgb(255,0,0)    hsl(120,100%,50%)
  #ffffff    rgba(0,0,0,0.5) #ff6b6b
```

## File Structure

```
Website_CSS-color-extractor-tool/
├── css-color-extractor.py      # Main interactive application
├── extract_colors.py           # Core extraction engine
├── requirements.txt            # Python dependencies
├── run.bat                     # Windows launcher
├── run.sh                      # Linux/Unix launcher
├── install.sh                  # Linux installation script
├── termux_setup.sh            # Termux setup script
├── utils/                     # Utility modules
│   ├── display.py             # UI components
│   ├── single_extract.py      # Single website extraction
│   ├── batch_extract.py       # Batch processing
│   ├── palette_generator.py   # HTML palette generation
│   ├── color_stats.py         # Color analysis
│   ├── swatch_exporter.py     # HTML swatch export
│   └── settings.py            # Settings menu
└── Extracted Colours/         # Output directory (auto-created)
```

## Usage Examples

### Basic Extraction
```bash
python css-color-extractor.py
# Select option 1, enter URL: https://github.com
```

### Batch Processing
```bash
python css-color-extractor.py
# Select option 2, enter multiple URLs
```

### Command Line
```bash
python extract_colors.py https://stackoverflow.com -o colors.txt
python extract_colors.py https://example.com -s -o colors.json
```

## Requirements

- Python 3.6+
- requests
- beautifulsoup4
- colorama
- selenium (optional, for JS-heavy sites)

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is open source. Feel free to use and modify.

## Connect with ACT91

- **GitHub**: [https://github.com/ACT91](https://github.com/ACT91)
- **Repository**: [https://github.com/ACT91/Website_CSS-color-extractor-tool](https://github.com/ACT91/Website_CSS-color-extractor-tool)
- **Follow for more awesome tools!**

## Support

If you find this tool useful, please consider:
- Starring the repository
- Following ACT91 on GitHub
- Sharing with others who might find it useful