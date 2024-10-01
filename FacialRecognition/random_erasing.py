from PIL import Image
import numpy as np
import random

def apply_random_erasing(PIL_img, p=1, sl=0.02, sh=0.4, r1=0.3, r2=3.3):
    """
    Apply random erasing to a PIL image.

    Args:
    - PIL_img: PIL image object (grayscale).
    - p: Probability of applying random erasing.
    - sl: Minimum proportion of erased area.
    - sh: Maximum proportion of erased area.
    - r1: Minimum aspect ratio of erased area.
    - r2: Maximum aspect ratio of erased area.

    Returns:
    - PIL image object with random erasing applied.
    """
    # Convert PIL image to numpy array
    img_np = np.array(PIL_img)
    
    # Randomly decide whether to apply random erasing
    if random.random() < p:
        # Calculate the dimensions of the random erasing rectangle
        H, W = img_np.shape
        area = H * W
        target_area = random.uniform(sl, sh) * area
        aspect_ratio = random.uniform(r1, r2)
        h = int(round(np.sqrt(target_area * aspect_ratio)))
        w = int(round(np.sqrt(target_area / aspect_ratio)))
        
        # Randomly choose the position of the erasing rectangle
        x = random.randint(0, abs(W - w))
        y = random.randint(0, abs(H - h))
        
        # Apply random erasing
        img_np[y:y+h, x:x+w] = random.randint(0, 255)
    
    # Convert numpy array back to PIL image
    erased_img = Image.fromarray(img_np)

    return erased_img


# imagePath = "/Users/ishika/Desktop/Facial_Recognition/Users/Akhil/1.15.jpg" 
# PIL_img = Image.open(imagePath).convert('L')  # Convert to grayscale
# erased_img = apply_random_erasing(PIL_img)
# erased_img.show()  # Display the image with random erasing
