import os, json
import sonic_sync.common.setup as setup
import sonic_sync.common.testing as testing
import sonic_sync.service.iTunes as itunes
import sonic_sync.service.appleMusic as aMusic
import sonic_sync.service.spotify as spotify
import sonic_sync.storages.file as file

# STANDARD DATA MODEL
# 
#
#
#
#

def pullData():
    itunes.writeData(itunes.pullData())
    aMusic.writeData(aMusic.pullData())


#=================
#  MAIN METHOD
#=================
def run():
    setup.init()
    aMusic.displayData()
    pullData()



#aMusic.main()

#print(json.dumps(itunes.pullData(),indent=4))

#print(files.listDataFiles(['itunes']))


#files.saveDatedFile(testing.pullData(),"itunesAlbums","json")

#files.saveFile("itunesAlbums","json")