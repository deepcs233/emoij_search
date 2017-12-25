import os
import pickle

from pHash import pHash
from pHash import diff

root_dir = os.path.join('staticpicture','jpg')
files = os.listdir(root_dir)

database = []

for f in files:
    try:
        filename = os.path.join(root_dir, f)
        g=open(filename)
        print 'Success: ',filename
        hashnum = pHash(filename)
        database.append((filename,hashnum))
    except:
        pass
        print 'Error: ',filename

pickle.dump(database, open('database.pkl','wb'))
