import os

def get_image_name(image_path):
    # Extract the image file name from the full path
    image_name = os.path.basename(image_path)
    return image_name

# Ask the user for the image file path
image_path = input("Enter the path of the image: ")

# Call the function and get the image name
image_name = get_image_name(image_path)

# Print the result
print(f"The name of the image is: {image_name}")
