# 🌐 My Portfolio Website's QR Code

My sleek, modern QR code that creates stylish QR codes linking to my portfolio website. I think it can also be Perfect for business cards, promotional materials, and digital marketing....

![QR Code Preview](./output/branded_qr.png)

## ✨ Features

- **Stylish QR Codes** - I Choose from rounded corners, circles, or gapped square patterns
- **Custom Colors** - Selected solid colors or beautiful gradients
- **Logo Integration** - Add my personal / brand logo to the center of the QR code
- **Branded Codes** - Include my name and a custom message with the QR code
- **High Scan Reliability** - It Uses high error correction to ensure QR codes scan properly, even with customizations

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. Clone this repository or download the files
2. Navigate to the project directory
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Quick Start

```bash
python modern_qr_generator.py
```

This will generate three different QR codes in the `output` directory, all linking to my portfolio website: https://brandon-2i82.vercel.app/

## 📋 Usage Options

### Basic Usage

```python
from modern_qr_generator import create_modern_qr_code

# Create a simple modern QR code
create_modern_qr_code(
    "https://brandon-2i82.vercel.app/", 
    "output/my_qr_code.png"
)
```

### Custom Styling

```python
# Create a QR code with custom colors and style
create_modern_qr_code(
    "https://brandon-2i82.vercel.app/", 
    "output/custom_qr.png",
    style="circle",                         # Options: "rounded", "circle", "gapped", "default"
    colors=((255, 255, 255), (41, 128, 185))  # (background_color, fill_color)
)
```

### With Branding

```python
from modern_qr_generator import create_branded_qr_with_text

# Create a branded QR code with your name and slogan
create_branded_qr_with_text(
    "https://brandon-2i82.vercel.app/",
    "output/branded_qr.png",
    brand_name="Brandon",
    slogan="Scan to visit my portfolio!"
)
```

## 🎨 Customization Options

### QR Code Styles

- `rounded`: QR code with rounded corners (modern look)
- `circle`: QR code with circular modules
- `gapped`: QR code with space between modules
- `default`: Standard square QR code

### Color Options

- **Solid Color**: Provide a tuple of RGB values for background and fill

  ```
  colors=((255, 255, 255), (41, 128, 185))  # White background, blue fill
  ```

- **Gradient**: Provide more than two colors for a gradient effect
  ```
  colors=((255, 255, 255), (41, 128, 185), (52, 152, 219))  # Gradient blue
  ```

## 📱 Testing Your QR Codes

To verify that your QR codes work:

1. Open your phone's camera app
2. Point it at the generated QR code
3. Follow the link to confirm it goes to your website

## 🔧 Troubleshooting

If your QR code doesn't scan properly:

- Increase the error correction level
- Make sure the logo (if added) isn't too large
- Ensure there's enough contrast between colors
- Try a different module style

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgements

- [qrcode](https://github.com/lincolnloop/python-qrcode) - The Python QR Code library
- [Pillow](https://python-pillow.org/) - Python Imaging Library

---

Made with ❤️ by Brandon..
