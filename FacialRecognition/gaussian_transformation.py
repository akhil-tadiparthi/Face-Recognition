import numpy as np
from PIL import Image
from scipy.ndimage import map_coordinates
from scipy.ndimage.filters import gaussian_filter

def gaussian_transformation(image, alpha, sigma, random_state=None):
    """
    Apply Gaussian transformations to a PIL image.

    Args:
    - image: PIL image object.
    - alpha: Scaling factor for the deformation field.
    - sigma: Standard deviation of the Gaussian filter used to smooth the deformation field.
    - random_state: Random seed for reproducibility.

    Returns:
    - PIL image object with Gaussian transformations applied.
    """
    if random_state is None:
        random_state = np.random.RandomState(None)

    # Convert image to numpy array
    image_array = np.array(image)

    # Generate random deformation field
    shape = image_array.shape
    dx = gaussian_filter((random_state.rand(*shape) * 2 - 1), sigma, mode="constant", cval=0) * alpha
    dy = gaussian_filter((random_state.rand(*shape) * 2 - 1), sigma, mode="constant", cval=0) * alpha

    # Apply deformation field to image
    x, y = np.meshgrid(np.arange(shape[1]), np.arange(shape[0]))
    indices = np.reshape(y+dy, (-1, 1)), np.reshape(x+dx, (-1, 1))
    distorted_image_array = map_coordinates(image_array, indices, order=1, mode="reflect")
    distorted_image_array = distorted_image_array.reshape(shape)

    # Convert distorted image array back to PIL image
    distorted_image = Image.fromarray(distorted_image_array.astype(np.uint8))

    return distorted_image

# imagePath = "/Users/ishika/Desktop/Facial_Recognition/Users/Akhil/1.15.jpg" 
# face_image = Image.open(imagePath)

# # Apply Gaussian transformations with alpha=50 and sigma=5
# distorted_face_image = gaussian_transformation(face_image, alpha=50, sigma=5)

# # Display the distorted face image
# distorted_face_image.show()
