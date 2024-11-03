import pandas as pd
import requests
import os
from config import API_KEY, SE_ID # Secure keys

# Global variables
NUM_IMAGES = 3

# Function to search images using Google Custom Search API
def search_images(species_name):
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': species_name,      # The plant species to search for
        'searchType': 'image',  # We want images only
        'key': API_KEY,         # Your API key
        'cx': SE_ID,            # Your search engine ID
        'num': NUM_IMAGES       # Number of images to return
    }
    
    try:
        response = requests.get(search_url, params=params)
        if response.status_code == 200:
            results = response.json()
            image_urls = [item['link'] for item in results.get('items', [])]
            return image_urls
        else:
            print(f"Request failed for {species_name}: {response.status_code} Client Error: {response.text}")
            print("# ERROR: HTTP response code not 200 - {}".format(response.status_code))
            print("# ERROR: For species - {}".format(species_name))
            print("# ERROR: Client message:\n{}".format(response.text))
            return []
    except Exception as e:
        print("# ERROR: Request response failed due to:\n{}\n".format(e))

# Function to download the image and save it
def download_image(url, species_name, index, folder='PlantImages'):
    # Create the folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # Set the file name and path
    file_name = f"{species_name}_{index}.jpg"
    file_path = os.path.join(folder, file_name)
    
    # Download the image
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {file_name}")
    else:
        print(f"Failed to download {url}")

# Main function to loop through species list and download images
def download_images_for_species_list(species_list):
    total_requests = 0
    for species in species_list:
        try:
            print(f"Searching images for: {species}")
            image_urls = search_images(species)
            if (len(image_urls) == 0):
                print("# ERROR: No image URLs returned for species: {}".format(species))
            
            total_requests += 1
            
            for index, url in enumerate(image_urls):
                print(f"Image URL: {url}")
                download_image(url, species, index + 1)
        except Exception as e:
            print(f"Error with species {species}: {e}")

    print(f"Total number of search requests = {total_requests}")

# Load the Excel file and extract species names
def load_species_list(file_path):
    excel_file = pd.read_excel(file_path)
    species_list = excel_file['Species'].tolist()  # Make sure this column name matches your Excel sheet
    return species_list

if __name__ == '__main__':
    species_inventory = "C:\\Users\\PeePee PooPoo\\Desktop\\PlantInventory\\species_inventory.xlsx"
    species_list = load_species_list(species_inventory)
    download_images_for_species_list(species_list)
