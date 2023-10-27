import os, json
import modules.setup as setup
import modules.iTunes as itunes
import modules.appleMusic as aMusic
import modules.spotify as spotify
import modules.testing as testing
import modules.files as files

# STANDARD DATA MODEL
# 
#
#
#
#
 
setup.init()

#print(json.dumps(itunes.pullData(),indent=4))

print(files.listDataFiles(['itunes']))

itunes.writeData(itunes.pullData())
#files.saveDatedFile(testing.pullData(),"itunesAlbums","json")

#files.saveFile("itunesAlbums","json")