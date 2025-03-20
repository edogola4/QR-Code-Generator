import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def create_qr_code(data, error_correction_level='M'):
    """
    Create a QR code from scratch
    
    Parameters:
    data (str): The data to encode in the QR code
    error_correction_level (str): Error correction level ('L', 'M', 'Q', 'H')
    
    Returns:
    numpy.ndarray: QR code matrix
    """
    # Step 1: Data analysis and mode selection
    mode = analyze_data(data)
    
    # Step 2: Data encoding
    encoded_data = encode_data(data, mode)
    
    # Step 3: Error correction coding
    error_corrected_data = add_error_correction(encoded_data, error_correction_level)
    
    # Step 4: Structure final message
    final_message = structure_final_message(error_corrected_data, mode, error_correction_level)
    
    # Step 5: Module placement in matrix
    qr_matrix = place_modules(final_message)
    
    # Step 6: Data masking
    masked_matrix = apply_best_mask(qr_matrix)
    
    # Step 7: Add format and version information
    final_qr = add_format_info(masked_matrix, error_correction_level)
    
    return final_qr

def analyze_data(data):
    """Determine the best encoding mode for the data"""
    # For simplicity, we'll use the Byte mode, which works for most text
    return "BYTE"

def encode_data(data, mode):
    """Encode the data in binary according to QR code specifications"""
    if mode == "BYTE":
        # Convert each character to its ASCII value and then to binary
        binary_data = ""
        for char in data:
            # Get ASCII value, convert to binary, ensure 8 bits
            binary_char = format(ord(char), '08b')
            binary_data += binary_char
        
        # Add mode indicator (0100 for Byte mode)
        mode_indicator = "0100"
        
        # Determine length of data and convert to binary
        # For small QR codes, this is typically 8 bits
        character_count = format(len(data), '08b')
        
        # Combine all parts
        encoded_data = mode_indicator + character_count + binary_data
        return encoded_data
    else:
        return "0000"  # Placeholder

def add_error_correction(data, level):
    """Add error correction codewords based on Reed-Solomon algorithm"""
    # This is a simplified placeholder
    # In a real implementation, you would use Reed-Solomon error correction
    return data + "0" * 50  # Add some padding as a placeholder

def structure_final_message(data, mode, error_level):
    """Structure the final message with padding"""
    # Add terminator if needed
    if len(data) % 8 != 0:
        data += "0" * (8 - (len(data) % 8))
    
    # Add padding to fill the QR code capacity
    while len(data) % 8 != 0:
        data += "0"
    
    # Add padding bytes if necessary
    padding_bytes = ["11101100", "00010001"]  # Alternating padding bytes
    padding_index = 0
    
    # For demonstration, we'll add some padding bytes
    # In a real implementation, you would calculate the required capacity
    while len(data) < 152:  # Arbitrary length for demonstration
        data += padding_bytes[padding_index]
        padding_index = (padding_index + 1) % 2
    
    return data

def place_modules(data):
    """Place modules (pixels) in the QR code matrix according to the pattern"""
    # For demonstration, we'll create a simple 21x21 QR code (Version 1)
    size = 21
    matrix = np.ones((size, size), dtype=int)  # White background
    
    # Add finder patterns (the three large squares in corners)
    add_finder_pattern(matrix, 0, 0)
    add_finder_pattern(matrix, 0, size - 7)
    add_finder_pattern(matrix, size - 7, 0)
    
    # Add alignment pattern for larger QR codes
    # Version 1 doesn't need an alignment pattern
    
    # Add timing patterns (alternating black/white lines)
    for i in range(8, size - 8):
        matrix[6, i] = 0 if i % 2 == 0 else 1  # Horizontal timing pattern
        matrix[i, 6] = 0 if i % 2 == 0 else 1  # Vertical timing pattern
    
    # Reserve format information area
    for i in range(9):
        matrix[i, 8] = 1  # Vertical format info
        matrix[8, i] = 1  # Horizontal format info
    
    for i in range(size - 8, size):
        matrix[8, i] = 1  # Bottom format info
    
    for i in range(size - 7, size):
        matrix[i, 8] = 1  # Right format info
    
    # Dark module
    matrix[size - 8, 8] = 0
    
    # Place data bits according to the zigzag pattern
    # This is a simplified placeholder
    # In a real implementation, you would follow the specific placement rules
    
    return matrix

def add_finder_pattern(matrix, row, col):
    """Add a finder pattern at the specified position"""
    # Outer black square
    for i in range(7):
        for j in range(7):
            if i == 0 or i == 6 or j == 0 or j == 6:
                matrix[row + i, col + j] = 0
    
    # Middle white square
    for i in range(1, 6):
        for j in range(1, 6):
            if i == 1 or i == 5 or j == 1 or j == 5:
                matrix[row + i, col + j] = 1
    
    # Inner black square
    for i in range(2, 5):
        for j in range(2, 5):
            matrix[row + i, col + j] = 0

def apply_best_mask(matrix):
    """Apply the best mask pattern to minimize penalty scores"""
    # For simplicity, we'll just return the original matrix
    # In a real implementation, you would evaluate different mask patterns
    return matrix

def add_format_info(matrix, error_level):
    """Add format information to the QR code"""
    # For simplicity, we'll just return the original matrix
    # In a real implementation, you would add the appropriate format information
    return matrix

def display_qr_code(matrix):
    """Display the QR code using matplotlib"""
    plt.figure(figsize=(8, 8))
    plt.imshow(matrix, cmap='binary')
    plt.axis('off')
    plt.tight_layout()
    plt.show()

def save_qr_code(matrix, filename="qr_code.png"):
    """Save the QR code as an image file"""
    plt.figure(figsize=(8, 8))
    plt.imshow(matrix, cmap='binary')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()
    
    # Resize to make it more practical
    img = Image.open(filename)
    img = img.resize((300, 300), Image.NEAREST)
    img.save(filename)
    print(f"QR code saved as {filename}")
    
# Example usage:
if __name__ == "__main__":
    data_to_encode = "Hello, World!"
    qr = create_qr_code(data_to_encode)
    display_qr_code(qr)
    save_qr_code(qr)