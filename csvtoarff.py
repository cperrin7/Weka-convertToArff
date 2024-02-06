#code to create weka .arff files automatically from csv
#csv must contain headers
#if there are any spaces in your filepath, put it in quotes

#to use via commandline:
#cd to where this python file is
#python csvtoarff.py "yourfilepath\yourfilename.csv"

import pandas as pd
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype
import sys
import os


inputfile = str(sys.argv[1])
#inputfile = r"C:\Users\CKPer\Documents\UF\Lab\ADNIProject\Weka-analysis\NeuropsychData_weka full.csv"
filenamefull = os.path.basename(inputfile)
pathname = os.path.dirname(inputfile)
filename = os.path.splitext(filenamefull)[0]
outputfile = filename+".arff"
outputpath = os.path.join(pathname, outputfile)

#clean the data a bit
csvFile = pd.read_csv(inputfile)
#can't have any spaces in the data at all
for c in csvFile:
    c.replace(" ", "")
for r in range(csvFile.shape[0]):
    for c in csvFile:
        if isinstance(csvFile.loc[r,c], str):
            csvFile.loc[r,c] = csvFile.loc[r,c].replace(" ", "")


f = open(outputpath, "w")#rewrite any existing file
#write the top comments
f.write("%% %s\n\n"%filename)
#write in the column names and types
dataname = "".join(filename.split()[-1:])#get only the last bit of the filename after a space
f.write("@relation %s\n"%dataname)
for col in csvFile.columns:
    if is_numeric_dtype(csvFile[col]):
        f.write("@attribute %s numeric\n"%col)
    else:
        line = "@attribute %s {"%col
        for item in csvFile[col].unique():
            line += "%s, "%item
        line = line[:-2]#take off extra ", "
        line +="}\n"
        f.write(line)

#write in the data
f.write("\n@data\n")
data = ""
for r in range(csvFile.shape[0]):
    line = ""
    for c in csvFile:
        line += "%s,"%csvFile.loc[r,c]
    line = line[:-1]
    line +="\n"
    data += line
f.write(data)
f.close()

print("saved %s to %s"%(outputfile,pathname))
print("done")
