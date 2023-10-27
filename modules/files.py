import json
from datetime import datetime
from os import path, listdir

def saveDatedFile(data,name,extension="txt",directory="data"):
    currDate=datetime.now().strftime('%y%m%d')
    fileName=("%s-%s.%s"%(currDate,name,extension))
    print("Creating file %s in directory %s/"%(fileName,directory))
    try: # Attempt to create file. if it already exists, run exception code block.
        file = open(path.join(directory,fileName),"x+")
    except:
        for i in range(1,999): # Keep trying to create a new file with an added number label, iterating upon each failure
            fileName=("%s-%s-%03d.%s"%(currDate,name,i,extension))
            try:
                file = open(path.join(directory,fileName),"x+")
                break
            except:
                if i>=999:
                    raise Exception("Could not create file, all files up to 999 exist")
    print("Created file %s in directory %s/"%(fileName,directory))
    print("Writing Data to %s in directory %s/"%(fileName,directory))
    file.write(json.dumps(data))
    file.close() # Write data to file and close before verifying created file contents
    print("Checking written data")
    if not verifySavedFile(data,fileName):
        print(bool(~verifySavedFile(data,fileName)))
        raise Exception("Data in new file does not match source data") # Assuming my code is written correctly there should be no sitation in which the file contents just written do not match the original data
    else:
        print("Data in file %s (in directory %s/) matches source. Continuing"%(fileName,directory)) 
    return
def verifySavedFile(data,fileName,directory="data"):
    file = open(path.join(directory,fileName),"r")
    if file.read() != json.dumps(data):
        return False
    else:
        return True
    
def listDataFiles(selection=[],directory="data"):
    directoryList = listdir(path.join(directory))
    if selection == []:
        return directoryList
    else:
        directoryList[:] = [item for item in directoryList if any(sub in item for sub in selection)]
        return directoryList