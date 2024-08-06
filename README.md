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
