from PIL import Image, ImageEnhance

def adjust_brightness_contrast(image, brightness_factor, contrast_factor):
    """
    Adjust the brightness and contrast of a PIL image.

    Args:
    - image: PIL image object.
    - brightness_factor: Brightness adjustment factor (1.0 is unchanged).
    - contrast_factor: Contrast adjustment factor (1.0 is unchanged).

    Returns:
    - PIL image object with adjusted brightness and contrast.
    """
    # Create brightness enhancer
    brightness = ImageEnhance.Brightness(image)
    # Adjust brightness
    image_with_brightness = brightness.enhance(brightness_factor)
    
    # Create contrast enhancer
    contrast = ImageEnhance.Contrast(image_with_brightness)
    # Adjust contrast
    image_with_brightness_and_contrast = contrast.enhance(contrast_factor)
    
    return image_with_brightness_and_contrast

# image_path = "/Users/ishika/Desktop/Facial_Recognition/Users/Akhil/1.15.jpg"
# face_image = Image.open(image_path)

# # Adjust brightness by increasing by 3x and contrast by increasing by 2x
# adjusted_image = adjust_brightness_contrast(face_image, 3, 2)

# # Display the adjusted image
# adjusted_image.show()
