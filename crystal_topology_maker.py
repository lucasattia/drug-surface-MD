#!/usr/bin/env python
# coding: utf-8

import os
import re
import numpy as np
import pandas as pd
import scipy
import time

start_time = time.time()

# USER INPUT
filebase = "fen"  # INPUT: topology file name
n = 4050  # INPUT: number of molecules in final crystal
numatoms = 46  # INPUT: number of atoms in each molecule #RUIn
sections = [
    "atoms",
    "bonds",
    "pairs",
    "angles",
    "dihedrals1",
    "dihedrals2",
]  # INPUT: sections
# add more sections if necessary (e.g., virtual sites, exclusions)
modified = [
    1,
    2,
    2,
    3,
    3,
    3,
]  # INPUT: number of columns that will be modified in each section
# e.g. (1 column for atom indices, 2 columns for ai and aj in pairs, etc.)

fd = open(filebase + ".itp", "r")
fdreads = fd.readlines()
outputbase = filebase + "_"


def firstindex(name):
    # function to get the first indices of each section in the list containing lines of the original .itp file
    if name == "atoms" or name == "angles":
        start_index = "[ " + name + " ] \n"
    elif name == "bonds" or name == "pairs":
        start_index = "[ " + name + " ]" + "\n"
    elif name == "dihedrals1":
        start_index = "[ dihedrals ] \n"
    elif name == "dihedrals2":
        start_index = "[ dihedrals ]\n"  # check the original .itp file for these small distinctions
    return fdreads.index(start_index)


indexlist = []
for section in sections:
    index_section = firstindex(section)
    indexlist.append(index_section)

ind_last = [i for i, n in enumerate(fdreads) if n == "\n"][-1]
indexlist.append(ind_last)

# open an individual text file for each section and write the corresponding content
for section in sections:
    outputbase_name = outputbase + section + ".txt"
    dest = open(outputbase_name, "w")
    for i in range(
        indexlist[sections.index(section)] + 2, indexlist[sections.index(section) + 1]
    ):
        dest.write(fdreads[i])
    dest.close()


# start writing the crystal .itp file
topout = open(filebase + "_out.itp", "a")

moleculetypeline = fdreads.index("[ moleculetype ]\n")
for i in range(moleculetypeline, moleculetypeline + 3):
    topout.write(fdreads[i])

topout.write("\n")


# function to write the crystal .itp file
def writeitp(name, columns):
    # parameter "columns" indicates how many columns need to be modified
    a = indexlist[sections.index(name)]
    for i in range(a, a + 2):  # start by writing the title and column names
        topout.write(fdreads[i])
    sectionfile_name = (
        outputbase + name + ".txt"
    )  # open the individual section text file
    # convert into pandas dataframe
    df_name = pd.read_csv(
        sectionfile_name, delim_whitespace=True, skipinitialspace=True, header=None
    ).dropna(axis=1, how="all")
    # get the columns that need to be modified
    columns_list = []
    for column in range(0, columns):
        df_name_column = df_name.iloc[:, column]
        columns_list.append(df_name_column)
    df_rest = df_name.iloc[
        :, columns:
    ]  # "rest" is the rest of the columns that do not need modifications
    df_extend = []
    # modifying the columns (e.g., atom indices, ai,aj,ak in dihedrals, etc.)
    for column in range(0, columns):
        df_column_extend = []
        for j in range(1, n):
            for i in columns_list[column]:
                t = i + numatoms * j
                df_column_extend.append(t)
        df_extend.append(df_column_extend)
    # append the "rest" of the columns "n" times, where n is the number of molecules in the crystal
    df_new_rest = df_rest.iloc[np.tile(np.arange(len(df_rest)), n)]
    df_new_rest.index = range(0, len(df_new_rest))
    # append the modified columns into the dataframe
    for column in range(0, columns):
        df_new_column = columns_list[column].append(pd.Series(df_extend[column]))
        df_new_column.index = range(0, len(df_new_column))
        df_new_rest.insert(0, str(columns + column + 111), df_new_column)
    df_new = df_new_rest.to_string(header=False, index=False)
    topout.write(df_new)
    topout.write("\n\n")


for section in sections:
    writeitp(section, modified[sections.index(section)])
    # remove individual text files, only keep the crystal topology
    os.remove(outputbase + section + ".txt")

print("Process finished --- %s seconds ---" % (time.time() - start_time))
