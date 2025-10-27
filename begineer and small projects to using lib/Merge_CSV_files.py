
# option 1 for using built-in csv lib
import csv

def merge_csv(csv_list,output_file):
    field_name=[]
    for file in csv_list:
        with open(file,'r',encoding="utf-8") as input_csv:
            field_Id=csv.DictReader(input_csv).fieldnames
            field_name.extend(f for f in field_Id if f not in field_name )
    with open(output_file,'w',encoding="utf-8", newline='') as output_csv:
                writter=csv.DictWriter(output_csv,field_name)
                writter.writeheader()
                for file in csv_list:
                      with open(file,'r',encoding="utf-8") as input_csv:
                            reader=csv.DictReader(input_csv)
                            for row in reader:
                                  writter.writerow(row)
merge_csv(["data1.csv", "data2.csv"], "merged.csv")

"""
Imports csv → for reading & writing CSV files.

Finds all columns → reads headers from every file, adds unique ones.

Creates merged CSV → writes all collected headers first.

Copies data rows → from each file into the new CSV.

Runs function → merges data1.csv & data2.csv into merged.csv.
"""
#option 2  Pandas Code
import pandas as pd

def merge_csv_pd(csv_list, output_file):
    data = [pd.read_csv(f) for f in csv_list]   # Read all CSV files
    merged = pd.concat(data, ignore_index=True) # Merge them all
    merged.to_csv(output_file, index=False)     # Save to one CSV file

# Example
merge_csv_pd(["data1.csv", "data2.csv"], "merged.csv")


"""
🧠 Simple Points (Short Explanation)

Imports pandas → used for handling CSV easily.

Reads all CSVs → into DataFrames.

Merges them → combines columns, fills missing with blanks.

Writes final CSV → saves merged data to one file.


✅ Output:
Combines all rows & columns → missing values become blank cells.
Easy, short, clean, and fast.
"""