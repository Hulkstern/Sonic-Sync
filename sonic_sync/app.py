import os, json
import modules.dirSetup as dirSetup
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

def run():
    dirSetup.init()
    aMusic.displayData()

def pullData():
    itunes.writeData(itunes.pullData())
    aMusic.writeData(aMusic.pullData())





#aMusic.main()

#print(json.dumps(itunes.pullData(),indent=4))

#print(files.listDataFiles(['itunes']))


#files.saveDatedFile(testing.pullData(),"itunesAlbums","json")

#files.saveFile("itunesAlbums","json")