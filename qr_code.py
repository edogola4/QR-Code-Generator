import qrcode
import os
from PIL import Image, ImageDraw, ImageFont

def create_modern_qr_code(url, output_file="modern_qr_code.png", color="#2980b9", add_logo=False):
    """
    Creates a modern-looking QR code linking to the provided URL
    
    Parameters:
    url (str): The URL to encode in the QR code
    output_file (str): The filename to save the QR code as
    color (str): Hex color code for the QR code
    add_logo (bool): Whether to add a logo to the center of the QR code
    
    Returns:
    str: Path to the generated QR code image
    """
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file) if os.path.dirname(output_file) else '.', exist_ok=True)
    
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction for logo
        box_size=10,
        border=4,
    )
    
    # Add data
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create QR code image with specified color
    img = qr.make_image(fill_color=color, back_color="white")
    
    # Add logo if requested
    if add_logo:
        # Create a simple "B" logo
        logo_size = img.size[0] // 4
        logo = Image.new('RGBA', (logo_size, logo_size), (255, 255, 255, 0))
        draw = ImageDraw.Draw(logo)
        draw.ellipse((0, 0, logo_size, logo_size), fill=(41, 128, 185, 255))
        
        # Try to add a "B" for Brandon
        try:
            # Try to load a font
            font = ImageFont.truetype("Arial.ttf", logo_size // 2)
        except:
            try:
                # Try a different font path for macOS
                font = ImageFont.truetype("/Library/Fonts/Arial.ttf", logo_size // 2)
            except:
                try:
                    # Try another common font path
                    font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", logo_size // 2)
                except:
                    # If all font loading fails, use default
                    font = ImageFont.load_default()
        
        # Add the "B" to the logo
        text_width, text_height = draw.textsize("B", font=font) if hasattr(draw, 'textsize') else (logo_size // 2, logo_size // 2)
        draw.text(
            ((logo_size - text_width) // 2, (logo_size - text_height) // 2), 
            "B", 
            fill=(255, 255, 255, 255), 
            font=font
        )
        
        # Calculate position to center the logo
        box = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)
        
        # Convert QR code to RGBA if it isn't already
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # Add white background for logo
        circle_bg = Image.new('RGBA', img.size, (0, 0, 0, 0))
        draw_bg = ImageDraw.Draw(circle_bg)
        center_size = logo_size + 10
        center_pos = ((img.size[0] - center_size) // 2, (img.size[1] - center_size) // 2)
        draw_bg.ellipse(
            (center_pos[0], center_pos[1], center_pos[0] + center_size, center_pos[1] + center_size), 
            fill=(255, 255, 255, 255)
        )
        img = Image.alpha_composite(img, circle_bg)
            
        # Paste the logo
        img.paste(logo, box, logo)
    
    # Save the QR code
    img.save(output_file)
    print(f"Modern QR code created and saved as {output_file}")
    
    return output_file

def create_branded_qr_with_text(url, output_file="branded_qr_code.png", brand_name="Brandon", 
                              color="#2980b9", add_text=True, 
                              slogan="Scan to visit my website!"):
    """
    Creates a branded QR code with text
    
    Parameters:
    url (str): The URL to encode in the QR code
    output_file (str): The filename to save the QR code as
    brand_name (str): Name to display on the QR code
    color (str): Hex color code for the QR code
    add_text (bool): Whether to add text below the QR code
    slogan (str): Text to add below the QR code
    
    Returns:
    str: Path to the generated QR code image
    """
    # Create temporary QR code
    temp_file = "temp_qr.png"
    create_modern_qr_code(url, temp_file, color, add_logo=True)
    
    # Open the QR code
    qr_img = Image.open(temp_file)
    
    if add_text:
        # Create a larger canvas for QR code + text
        width, height = qr_img.size
        canvas = Image.new('RGBA', (width, int(height * 1.3)), (255, 255, 255, 255))
        
        # Paste QR code at the top
        canvas.paste(qr_img, (0, 0))
        
        # Add text
        draw = ImageDraw.Draw(canvas)
        
        try:
            # Try to load a font
            title_font = ImageFont.truetype("Arial.ttf", 30)
            slogan_font = ImageFont.truetype("Arial.ttf", 20)
        except:
            try:
                # Try a different font path for macOS
                title_font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 30)
                slogan_font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 20)
            except:
                try:
                    # Try another common font path
                    title_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 30)
                    slogan_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 20)
                except:
                    # If all font loading fails, use default
                    title_font = ImageFont.load_default()
                    slogan_font = ImageFont.load_default()
        
        # Add brand name - handling different PIL versions
        if hasattr(draw, 'textlength'):
            title_width = draw.textlength(brand_name, font=title_font)
            slogan_width = draw.textlength(slogan, font=slogan_font)
        else:
            title_width, _ = draw.textsize(brand_name, font=title_font)
            slogan_width, _ = draw.textsize(slogan, font=slogan_font)
        
        # Draw the text
        draw.text(((width - title_width) // 2, height + 10), brand_name, fill=(0, 0, 0, 255), font=title_font)
        draw.text(((width - slogan_width) // 2, height + 50), slogan, fill=(100, 100, 100, 255), font=slogan_font)
        
        # Save the final image
        canvas.save(output_file)
    else:
        # Just save the QR code if no text is needed
        qr_img.save(output_file)
    
    # Clean up the temporary file
    if os.path.exists(temp_file):
        os.remove(temp_file)
    
    print(f"Branded QR code created and saved as {output_file}")
    return output_file

if __name__ == "__main__":
    # Your website URL
    website_url = "https://brandon-2i82.vercel.app/"
    
    # Create a simple modern QR code
    create_modern_qr_code(
        website_url, 
        "output/modern_qr.png", 
        color="#3498db"  # Blue QR code
    )
    
    # Create a QR code with a different color
    create_modern_qr_code(
        website_url, 
        "output/blue_qr.png", 
        color="#2c3e50"  # Dark blue QR code
    )
    
    # Create a branded QR code with text
    create_branded_qr_with_text(
        website_url, 
        "output/branded_qr.png", 
        brand_name="Brandon", 
        color="#3498db",
        slogan="Scan to visit my portfolio!"
    )
    
    print("QR codes generated successfully! Check the output directory.")