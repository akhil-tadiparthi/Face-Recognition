from PIL import Image

def rotate_face_image(image, angle):
    """
    Rotate a face image slightly to simulate variations in head pose.

    Args:
    - image: PIL image object representing the face image.
    - angle: Angle in degrees by which to rotate the image.

    Returns:
    - PIL image object representing the rotated face image.
    """
    # Rotate the image by the specified angle
    rotated_image = image.rotate(angle, expand=True)
    
    return rotated_image

# image_path = "/Users/ishika/Desktop/Facial_Recognition/Users/Akhil/1.15.jpg" 
# face_image = Image.open(image_path)

# # Rotate the face image by 10 degrees
# rotated_face_image = rotate_face_image(face_image, 10)

# # Display the rotated face image
# rotated_face_image.show()
