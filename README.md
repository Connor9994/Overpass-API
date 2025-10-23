# Nearby Fish (/etc) Store Finder

![GitHub stars](https://img.shields.io/github/stars/Connor9994/Overpass-API?style=social) ![GitHub forks](https://img.shields.io/github/forks/Connor9994/Overpass-API?style=social) ![GitHub issues](https://img.shields.io/github/issues/Connor9994/Overpass-API) 

## Overview

This Python script utilizes the Overpass API to find nearby fish, coral, and aquarium stores based on their geographical coordinates. The script allows you to specify a radius in meters to search for various types of shops related to fish.

![image](https://github.com/user-attachments/assets/39b08d56-4ebb-4c27-8f69-ea3048a9f72b)


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
   
   Example below is 10 miles surounding Portland, Oregon
   
   ```python
   # https://www.latlong.net/
   latitude = 45.512230
   longitude = -122.658722
   meters = 16000  # Set the desired search radius in meters
   ```

   Query for this script is:
   
   ```
    [out:json];
    (
      node[shop=pet](around:{meters}, {latitude}, {longitude});
      node[shop=aquarium](around:{meters}, {latitude}, {longitude});
      node[shop~fish](around:{meters}, {latitude}, {longitude}); // Finds any shop w/ "fish" anywhere in the description
      node[shop=seafood](around:{meters}, {latitude}, {longitude});
      node[product~fish](around:{meters}, {latitude}, {longitude});
    );
    out body;
   ```

   And can be modified according to/with these sources

   [Query Builder/Tester](https://overpass-turbo.eu/)

   [Search Parameters/Syntax](https://wiki.openstreetmap.org/wiki/Overpass_turbo/Wizard)

   [Types of Shops](https://wiki.openstreetmap.org/wiki/Map_features#Shop) (Not an Exhaustive List, Some Stores use Fish/Fishmonger instead of "Fishing" for instance)

   [ChatGPT, write me an Overpass API Query to find my local Gamestops](https://platform.openai.com/playground/p/4qgIBvFcHodXtUrwBqsPky72?model=undefined&mode=chat)
   
   <img src="https://github.com/user-attachments/assets/36509630-ef00-4efd-aa8c-cf105a715267" width="500" height="300">


3. **Run the script**:

   Execute the script to find nearby fish stores and append the data to a text file called `stores.txt`.

   ```bash
   python nearby_fish_stores.py
   ```

4. **Check the results**:

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
   ~~~

def write_to_file(data, filename):
   ~~~

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

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.
