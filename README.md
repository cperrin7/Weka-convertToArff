# Weka-convertToArff
code for converting to .arff files for the Weka machine learning GUI

This is just something I wrote to convert most csv files to .arff for Weka. Data needs to be clean; all non-numeric values should be text (factors) and not numbers (0,1) and take out any missing values. 

To run (in command prompt etc.):
1. download the conversion file
2. cd to the directory your conversion file is saved
3. python csvtoarff.py "yourfilepath\yourfilename.csv"
4. it will save an .arff file by the same name and in the same folder as the csv you wanted to convert
