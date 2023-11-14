import os, json
import urllib.request
import sonic_sync.storages.file as file
from datetime import datetime

# Raw data pulled from source should be stored in each python module until called for by main.py.
# The only data that should exit this function should be in the standard format of
# URLs available/examples: https://itunes.apple.com/us/rss/topalbums/limit=200/json https://itunes.apple.com/us/rss/topalbums/limit=200/xml https://itunes.apple.com/us/rss/topalbums/limit=10/genre=21/xml
#To-Do: specify standard data-format

#data object, should include a timestamp when data is stored with pull data

def pullData(count: int = 200):
    # Pull Data from remote source & store in local object
    # Check current data object before pulling data and do not pull if data has been pulled within the last 6 hours
    with urllib.request.urlopen(f"https://itunes.apple.com/us/rss/topalbums/limit={count}/json") as url:
        data = json.load(url)
    return data

# Example of Entry in returned Data
#
""" {
    "feed": {
        "author": {
            "name": {
                "label": "iTunes Store"
            },
            "uri": {
                "label": "http://www.apple.com/itunes/"
            }
        },
        "entry": [
            {
                "im:name": {
                    "label": "Lover"
                },
                "im:image": [
                    {
                        "label": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/49/3d/ab/493dab54-f920-9043-6181-80993b8116c9/19UMGIM53909.rgb.jpg/55x55bb.png",
                        "attributes": {
                            "height": "55"
                        }
                    },
                    {
                        "label": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/49/3d/ab/493dab54-f920-9043-6181-80993b8116c9/19UMGIM53909.rgb.jpg/60x60bb.png",
                        "attributes": {
                            "height": "60"
                        }
                    },
                    {
                        "label": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/49/3d/ab/493dab54-f920-9043-6181-80993b8116c9/19UMGIM53909.rgb.jpg/170x170bb.png",
                        "attributes": {
                            "height": "170"
                        }
                    }
                ],
                "im:itemCount": {
                    "label": "18"
                },
                "im:price": {
                    "label": "$11.99",
                    "attributes": {
                        "amount": "11.99",
                        "currency": "USD"
                    }
                },
                "im:contentType": {
                    "im:contentType": {
                        "attributes": {
                            "term": "Album",
                            "label": "Album"
                        }
                    },
                    "attributes": {
                        "term": "Music",
                        "label": "Music"
                    }
                },
                "rights": {
                    "label": "\u2117 2019 Taylor Swift"
                },
                "title": {
                    "label": "Lover - Taylor Swift"
                },
                "link": {
                    "attributes": {
                        "rel": "alternate",
                        "type": "text/html",
                        "href": "https://music.apple.com/us/album/lover/1468058165?uo=2"
                    }
                },
                "id": {
                    "label": "https://music.apple.com/us/album/lover/1468058165?uo=2",
                    "attributes": {
                        "im:id": "1468058165"
                    }
                },
                "im:artist": {
                    "label": "Taylor Swift",
                    "attributes": {
                        "href": "https://music.apple.com/us/artist/taylor-swift/159260351?uo=2"
                    }
                },
                "category": {
                    "attributes": {
                        "im:id": "14",
                        "term": "Pop",
                        "scheme": "https://music.apple.com/us/genre/music-pop/id14?uo=2",
                        "label": "Pop"
                    }
                },
                "im:releaseDate": {
                    "label": "2019-08-23T00:00:00-07:00",
                    "attributes": {
                        "label": "August 23, 2019"
                    }
                }
            }, """

""" def returnData(date=datetime.now().strftime('%y%m%d'),name='itunes'):
    if date == '':
        print("return all data given matchin file name not date")
    else:

    allData = []
    # Return data in standard format
    for items in file.listDataFiles(['%s-itunes'%(date)]):
        print(items)
        
    return """

def writeData(data):
    # Write current data object to file in standard format
    file.saveDatedFile(data,'itunesAlbums','json')
    return