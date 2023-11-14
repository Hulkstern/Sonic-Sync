#example get request: https://api.music.apple.com/v1/catalog/us/charts?types=albums&limit=200
import sonic_sync.storages.file as file
from datetime import datetime
from sonic_sync.common.settings import CONFIG_LOCATION

#import requests
#import jwt
#import time
import configparser
import applemusicpy
import json

config = configparser.ConfigParser()
config.read(CONFIG_LOCATION)

# Your Apple Music developer credentials
KEY_ID = config.get('Credentials','KEY_ID')
TEAM_ID = config.get('Credentials','TEAM_ID')
PRIVATE_KEY_PATH = config.get('Credentials','PRIVATE_KEY_PATH')
STOREFRONT_ID = config.get('Credentials','STOREFRONT_ID')  # For example, "us" for United States
auth_key = open(PRIVATE_KEY_PATH, "r").read()

am = applemusicpy.AppleMusic(auth_key,KEY_ID,TEAM_ID)

def pullData(count: int = 200):
    return am.charts(storefront=STOREFRONT_ID,types=["albums"],chart="most-played",limit=str(count))

def pullAlbumData(albumID):
    return am.album(albumID,storefront=STOREFRONT_ID)

def parseData(data=pullData(),skipPartialsAndSingles: bool = True):
    #results = am.charts(storefront=STOREFRONT_ID,types=["albums"],chart="most-played",limit="200")
    #print(json.dumps(results,indent=4))
    output = []
    for index, entry in enumerate(data["results"]["albums"][0]['data']):
        cleanedData = entry['attributes']
        cleanedData['chartPos']=index+1
        cleanedData['addFields']={
            
        }
        
        if not ("contentRating" in cleanedData):
            cleanedData['contentRating']="clean"
        
        if (skipPartialsAndSingles!=True):
            output.append(cleanedData)
        elif (cleanedData['isComplete']==True and cleanedData['isSingle']==False):
            output.append(cleanedData)
        else:
            print("[WARN] Something unexpected happened while parsing data")
    return output

def displayData(data=parseData()):
    for index, cleanedData in enumerate(data):
        print("==================")
        print(f"True Chart Position: \"{cleanedData['chartPos']}\"")
        print(f"Name: \"{cleanedData['name']}\"")
        print(f"Artist: \"{cleanedData['artistName']}\"")
        print(f"Track(s): \"{cleanedData['trackCount']}\"")
        print(f"genre: \"{cleanedData['genreNames'][0]}\"")
        print(f"Released: \"{cleanedData['releaseDate']}\"")
        print(f"Record Label: \"{cleanedData['recordLabel']}\"")
        print(f"URL: \"{cleanedData['url']}\"")
        print(f"UPC: \"{cleanedData['upc']}\"")
        print(f"Rating: \"{cleanedData['contentRating']}\"")
        print()

def writeData(data=pullData()):
    file.saveDatedFile(data,'appleMusicAlbums','json')
    return

"""
# Apple Music API endpoint for fetching charts data
API_ENDPOINT = f"https://api.music.apple.com/v1/catalog/{STOREFRONT_ID}/charts"

# Generate JWT token for authentication
def generate_token():
    auth_key = open(PRIVATE_KEY_PATH, "r").read()

    headers = {
        "alg": "ES256",
        "kid": KEY_ID,
        "typ": "JWT"
    }
    current_time = int(time.time())
    payload = {
        "iss": TEAM_ID,
        "iat": int(current_time),
        "exp": int(time.time() + 1200),  # Token expiration time (in seconds)
        "aud": "appstoreconnect-v1"
    }
    
    token = jwt.encode(payload, auth_key, algorithm="ES256", headers=headers)
    return token
    
# Make API request to fetch top 100 albums
def fetch_top_albums():
    token = generate_token()
    headers = {
        "Authorization": "Bearer " + token
    }
    print(STOREFRONT_ID)
    #response = requests.get(API_ENDPOINT.format(storefront=STOREFRONT_ID), headers=headers)
    response = requests.get(f"{API_ENDPOINT}?types=albums&chart=most-played&limit=200", headers=headers)
    print(response.status_code)
    if response.status_code == 200:
        print(response.text)
        return response.json()#["results"]["albums"]["data"][0]["attributes"]["results"]
    else:
        print(f"Response Body: {response.json()}")
        return None

# Main function to print top 100 albums
def main():
    top_albums = fetch_top_albums()
    if top_albums:
        for index, album in enumerate(top_albums, start=1):
            #print(f"{index}. {album['name']} by {album['artistName']}")
            print()
    else:
        print("Failed to fetch top albums.")

#if __name__ == "__main__":
#    main()
 """


