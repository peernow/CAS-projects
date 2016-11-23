
# coding: utf-8

# In[1]:

#-----------------BEGIN HEADERS-----------------
import numpy as np
#import matplotlib.pyplot as plt
from scipy import stats
import csv
import scipy
np.set_printoptions(threshold=np.nan)
import contextlib
import pdb
import glob
from PIL import Image

@contextlib.contextmanager

def printoptions(*args, **kwargs):
  original = np.get_printoptions()
  np.set_printoptions(*args, **kwargs)
  yield
  np.set_printoptions(**original)
#-----------------END HEADERS-----------------
mynames = []
mynames.append(glob.glob("test1/*.jpg"))
mynames = np.array(mynames)

with open('test_l_40_22.csv', 'wb') as csvfile:
  mywriter = csv.writer(csvfile, delimiter=',')
  for i in range(len(mynames)):
    for j in range(len(mynames[i])):
      print("Progress: " + str((float(i)/float(len(mynames)))*100.0) + "%, " + str((float(j)/float(len(mynames[i])))*100.0) + "%; i,j: " + str(i) + ", " + str(j))
      im = Image.open(mynames[i][j])
      im = im.convert('L') #1 = B&W, L = grey
      #print(im.size)
      im = im.resize((40,22),Image.ANTIALIAS) #300,160, 150, 80
      #im.show()
      #exit()
      mycsv = np.ravel(np.array(im.getdata()))
      #print(np.shape(mycsv))
      #exit()
      mywriter.writerow(mycsv)
      del(mycsv)
      im.close()
