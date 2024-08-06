# Nearby Fish Stores Finder

## Overview

This Python script utilizes the Overpass API to find nearby fish, coral, and aquarium stores based on their geographical coordinates. The script allows you to specify a radius in meters to search for various types of shops related to fish.

## Features

- Query the Overpass API for nearby stores.
- Support for multiple types of shops (pet, aquarium, seafood, etc.).
- Retrieve various attributes such as name, phone, email, social media links, and location.
- Append results to a text file for easy access.

## Requirements

- Python 3.x
- Requests library

## Installation

1. **Clone this repository**:

   ```bash
   git clone https://github.com/connor9994/Overpass-API.git
   cd Overpass-API
   ```

2. **Install the required dependencies**:
   
   If you haven't already installed the `requests` library, do so using pip:

   ```bash
   pip install requests
   ```

## Usage

1. **Set the latitude, longitude, and search radius**:
   Modify the following variables in the script:

   ```python
   latitude = 45.512230
   longitude = -122.658722
   meters = 16000  # Set the desired search radius in meters
   ```

2. **Run the script**:

   Execute the script to find nearby fish stores and append the data to a text file called `stores.txt`.

   ```bash
   python nearby_fish_stores.py
   ```

3. **Check the results**:

   After running the script, the results will be appended to `stores.txt`. Each entry includes:

   - Name
   - Phone number
   - Email address
   - Website
   - Social Media Links (Twitter, Facebook, Instagram, YouTube)
   - Location (latitude and longitude)

## Example Script

Here is a brief overview of the script functionality:

```python
import requests

def get_nearby_fish_stores(latitude, longitude, meters):
    # Overpass API query to find nearby fish stores
    overpass_query = f"""
    [out:json];
    (
        node[shop=pet](around:{meters}, {latitude}, {longitude});
        node[shop=aquarium](around:{meters}, {latitude}, {longitude});
        node[shop~fish](around:{meters}, {latitude}, {longitude});
        node[shop=seafood](around:{meters}, {latitude}, {longitude});
        node[product~fish](around:{meters}, {latitude}, {longitude});
    );
    out body;
    """
    # Make a POST request to Overpass API
    response = requests.get('http://overpass-api.de/api/interpreter', params={'data': overpass_query})
   
    # Check for successful response
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None

def write_to_file(data, filename):
    with open(filename, 'a') as file:
        for element in data['elements']:
            tags = element.get('tags', {})
            latitude = element['lat']
            longitude = element['lon']
            name = tags.get('name') or tags.get('contact:name')
            phone = tags.get('phone') or tags.get('contact:phone')
            # Add more tags here as needed...
            # Prepare and write output...

# Example usage:
latitude = 45.512230
longitude = -122.658722
meters = 16000  # 10 Miles
data = get_nearby_fish_stores(latitude, longitude, meters)
if data:
    write_to_file(data, 'stores.txt')
    print("Data appended to stores.txt")
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to modify this template further based on your specific needs or preferences!
