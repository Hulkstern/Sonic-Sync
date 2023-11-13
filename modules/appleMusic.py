#example get request: https://api.music.apple.com/v1/catalog/us/charts?types=albums&limit=200

import requests
import jwt
import time

# Apple Music API endpoint for fetching charts data
API_ENDPOINT = "https://api.music.apple.com/v1/catalog/{storefront}/charts"

# Your Apple Music developer credentials
TEAM_ID = "YOUR_TEAM_ID"
KEY_ID = "YOUR_KEY_ID"
PRIVATE_KEY_PATH = "path/to/your/private-key.p8"
STOREFRONT_ID = "us"  # For example, "us" for United States

# Generate JWT token for authentication
def generate_token():
    auth_key = open(PRIVATE_KEY_PATH, "r").read()
    headers = {
        "alg": "ES256",
        "kid": KEY_ID
    }
    payload = {
        "iss": TEAM_ID,
        "exp": time.time() + 1800,  # Token expiration time (in seconds)
        "aud": "appstoreconnect-v1"
    }
    token = jwt.encode(payload, auth_key, algorithm="ES256", headers=headers)
    return token.decode("utf-8")

# Make API request to fetch top 100 albums
def fetch_top_albums():
    token = generate_token()
    headers = {
        "Authorization": "Bearer " + token
    }
    response = requests.get(API_ENDPOINT.format(storefront=STOREFRONT_ID), headers=headers)
    if response.status_code == 200:
        return response.json()["data"][0]["attributes"]["results"]
    else:
        return None

# Main function to print top 100 albums
def main():
    top_albums = fetch_top_albums()
    if top_albums:
        for index, album in enumerate(top_albums, start=1):
            print(f"{index}. {album['name']} by {album['artistName']}")
    else:
        print("Failed to fetch top albums.")

if __name__ == "__main__":
    main()
