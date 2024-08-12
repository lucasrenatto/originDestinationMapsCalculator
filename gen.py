import pandas as pd
import googlemaps

# Google Maps API Key
api_key = 'YOUR GOOGLE KEY'
gmaps = googlemaps.Client(key=api_key)

file_path = 'yourFilePath.xlsx'
data = pd.read_excel(file_path)


def calculate_distance_time(origin, destination):
    try:
        result = gmaps.distance_matrix(origin, destination, mode='driving')
        distance = result['rows'][0]['elements'][0]['distance']['text']
        duration = result['rows'][0]['elements'][0]['duration']['text']
        return distance, duration
    except Exception as e:
        print(f"Error calculating distance for {origin}: {e}")
        return None, None

for index, row in data.iterrows():
    origin = f"{row['City']}, {row['State']}"
    destination = row['Address']
    distance, duration = calculate_distance_time(origin, destination)
    
    data.at[index, 'Distance'] = distance
    data.at[index, 'Time'] = duration


new_file_path = 'result.xlsx'
data.to_excel(new_file_path, index=False)

print(f"File successfully generated: {new_file_path}")