import urllib.request, json 
import sonic_sync.storages.file as file
import configparser
from sonic_sync.common.settings import CONFIG_LOCATION

config = configparser.ConfigParser()
config.read(CONFIG_LOCATION)

# Your Apple Music developer credentials
KEY_ID = config.get('Credentials','KEY_ID')
PRIVATE_KEY_PATH = config.get('Credentials','PRIVATE_KEY_PATH')
STOREFRONT_ID = config.get('Credentials','STOREFRONT_ID')  # For example, "us" for United States

def pullData():
    with urllib.request.urlopen("https://itunes.apple.com/us/rss/topalbums/limit=200/json") as url:
        data = json.load(url)
        #print(json.dumps(data,indent=4))
    return data

""" #get my damn public key
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def extract_public_key_from_private(PRIVATE_KEY_PATHin):
    # Read the private key
    private_key_data = open(PRIVATE_KEY_PATHin, "rb").read()

    # Load the private key
    private_key = serialization.load_pem_private_key(
        private_key_data,
        password=None,
        backend=default_backend()
    )

    # Extract the public key
    public_key = private_key.public_key()

    # Serialize the public key to PEM format
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return public_key_pem.decode("utf-8")

# Example usage

public_key = extract_public_key_from_private(PRIVATE_KEY_PATH)
print(public_key) """