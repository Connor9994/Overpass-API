import requests

def get_nearby_fish_stores(latitude, longitude, meters):
    # Query Builder/Tester
    # https://overpass-turbo.eu/

    # Search Parameters/Syntax
    # https://wiki.openstreetmap.org/wiki/Overpass_turbo/Wizard

    # Types of Shops (Not an Exhaustive List, Some Stores use "Fish"/"Fishmonger" instead of "Fishing" for instance)
    # https://wiki.openstreetmap.org/wiki/Map_features#Shop

    overpass_query = f"""
    [out:json];
    (
      node[shop=pet](around:{meters}, {latitude}, {longitude});
      node[shop=aquarium](around:{meters}, {latitude}, {longitude});
      node[shop~fish](around:{meters}, {latitude}, {longitude}); // Finds any shop w/ "fish" anywhere in the description
      node[shop=seafood](around:{meters}, {latitude}, {longitude});
      node[product~fish](around:{meters}, {latitude}, {longitude});
    );
    out body;
    """
    # Make a POST request to Overpass API
    response = requests.get('http://overpass-api.de/api/interpreter', params={'data': overpass_query})
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()  # Return the response in JSON format
    else:
        print("Error:", response.status_code)
        return None

def write_to_file(data, filename):
    with open(filename, 'a') as file:  # Open in append mode
        for element in data['elements']:
            tags = element.get('tags', {})
            latitude = element['lat']
            longitude = element['lon']
            name = tags.get('name') or tags.get('contact:name')
            phone = tags.get('phone') or tags.get('contact:phone')
            email = tags.get('email') or tags.get('contact:email') 
            website = tags.get('website') or tags.get('contact:website')
            twitter = tags.get('twitter') or tags.get('contact:twitter')
            facebook = tags.get('facebook') or tags.get('contact:facebook') 
            instagram = tags.get('instagram') or tags.get('contact:instagram')
            youtube = tags.get('youtube') or tags.get('contact:youtube')
            
            output = []
            # Preparing the output string
            if name:
                output.append(f"Name: {name}\n")
            if phone:
                output.append(f"Phone: {phone}\n")
            if email:
                output.append(f"Email: {email}\n")
            if website:
                output.append(f"Website: {website}\n")
            if twitter:
                output.append(f"Twitter: {twitter}\n")
            if facebook:
                output.append(f"Facebook: {facebook}\n")
            if youtube:
                output.append(f"Youtube: {youtube}\n")
            if instagram:
                output.append(f"Instagram: {instagram}\n")
            if latitude and longitude:
                output.append(f"Location: {latitude}, {longitude}\n")
            output.append("\n")
            try:
                file.write("".join(output))
            except Exception as e:
                print("Failed to output because of: " + str(e))

# https://www.latlong.net/
latitude = 45.512230
longitude = -122.658722
meters = 16000 # 10 Miles

data = get_nearby_fish_stores(latitude, longitude, meters)

if data:
    write_to_file(data, 'stores.txt')
    print("Data appended to stores.txt")