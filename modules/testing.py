import urllib.request, json 
import modules.files as files

def pullData():
    with urllib.request.urlopen("https://itunes.apple.com/us/rss/topalbums/limit=200/json") as url:
        data = json.load(url)
        #print(json.dumps(data,indent=4))
    return data