import cv2
import numpy as np
import os

def remove_green_areas(image):
    """Remove green areas from an image using HSV color filtering."""
    # Convert the image to HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define range of green color in HSV
    lower_green = np.array([35, 40, 40])  # Lower bound for green hue
    upper_green = np.array([85, 255, 255])  # Upper bound for green hue
    
    # Create a mask to filter out green colors
    mask = cv2.inRange(hsv_image, lower_green, upper_green)
    
    # Invert the mask to keep non-green areas
    mask_inv = cv2.bitwise_not(mask)
    
    # Apply the mask to the original image
    non_green_image = cv2.bitwise_and(image, image, mask=mask_inv)
    
    return non_green_image

def kmeans_clustering(image, k=5):
    """Use K-means clustering to find dominant colors in the non-green areas of the image."""
    # Reshape the image to a 2D array of pixels
    pixel_data = image.reshape((-1, 3))  # Reshape to a list of pixels
    pixel_data = np.float32(pixel_data)  # Convert to float32 for K-means
    
    # Remove zero pixels (which are black due to masking)
    pixel_data = pixel_data[np.any(pixel_data > 0, axis=1)]
    
    if pixel_data.size == 0:
        return None  # No pixels to process (edge case for all-green images)
    
    # Define criteria and apply K-means clustering
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, centers = cv2.kmeans(pixel_data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    
    # Convert centers to uint8 (valid RGB values)
    dominant_colors = np.uint8(centers)
    
    # Count the number of pixels in each cluster
    label_counts = np.bincount(labels.flatten())
    
    # Sort the colors by their frequency
    sorted_indices = np.argsort(label_counts)[::-1]
    sorted_colors = dominant_colors[sorted_indices]
    
    return sorted_colors

def create_color_visualization(colors, save_path):
    """Create a simple image visualizing the dominant colors."""
    if colors is None:
        print("No dominant colors found.")
        return
    
    color_block_height = 100  # Height for each color block
    image_width = 300         # Width of the final image
    num_colors = len(colors)
    
    # Create a blank image (each color block will have the same height)
    visualization = np.zeros((color_block_height * num_colors, image_width, 3), dtype=np.uint8)
    
    # Fill the image with rectangles of each color
    for i, color in enumerate(colors):
        start_y = i * color_block_height
        end_y = start_y + color_block_height
        visualization[start_y:end_y, :] = color
    
    # Save the image
    cv2.imwrite(save_path, visualization)

# Example usage
desktop_path = os.path.join(os.path.expanduser("~"), 'Desktop')

# Folder paths
test_images_folder = os.path.join(desktop_path, 'TestImages')
color_visualization_folder = os.path.join(desktop_path, 'ColorVisualizations')

# Make sure the ColorVisualizations folder exists
os.makedirs(color_visualization_folder, exist_ok=True)

# Loop through all images in the TestImages folder
for image_filename in os.listdir(test_images_folder):
    if image_filename.endswith(('.jpg', '.png', '.jpeg')):  # Process image files
        image_path = os.path.join(test_images_folder, image_filename)
        
        # Load the image
        image = cv2.imread(image_path)
        
        # Remove green areas from the image
        non_green_image = remove_green_areas(image)
        
        # Find the dominant colors
        dominant_colors = kmeans_clustering(non_green_image, k=5)
        
        # Print the dominant colors
        if dominant_colors is not None:
            print(f"Dominant colors for {image_filename}:")
            for i, color in enumerate(dominant_colors):
                print(f"Dominant Color {i + 1}: RGB {color.tolist()}")

            # Save the color visualization
            color_visualization_path = os.path.join(color_visualization_folder, f'{os.path.splitext(image_filename)[0]}_colors.png')
            create_color_visualization(dominant_colors, color_visualization_path)
            print(f"Color visualization saved as: {color_visualization_path}")
        else:
            print(f"No non-green colors found for {image_filename}.")
