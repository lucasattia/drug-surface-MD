# drug_surface_MD
This repo stores input files and scripts for the paper "Surfactant-polymer complexation and competition on drug crystal surfaces controls crystallinity," by Attia et al. The "structure_files" folder stores the .pdb and .gro input structure files. The "mdp_files" folder stores the .mdp parameter files energy minimization and NVT molecular dynamics. The "index" folder stores the .ndx file with index groups and the files needed to insert excipients in separate layers. The "shell_scripts" folder stores the shells scripts for inserting excipients and running energy minimization and NVT MD. The "itp" folder stores .itp files for the excipient molecules and the .top file for the system. The .itp files for the drug crystal slabs are too large to store on GitHub, and can be shared upon request to the authors.
# Topology Maker Script - README

## Overview

This script is a tool for constructing an `.itp` (Include Topology) file for a large crystal structure for molecular simulation based on data provided in a `.itp` file representing a unit cell. It is specifically designed to handle topologies comprising sections for atoms, bonds, pairs, angles, and two dihedrals. In the script, lines requiring user input are explicitly marked as "INPUT."

## Prerequisites

Before executing the script, please take note of the following preparatory steps:

1. **File Name Adjustment:**
   - Ensure you update the file name of the original `.itp` file within the script to match your specific input file.

2. **Specify Parameters:**
   - Input the required parameters, including:
     - The number of molecules in the final crystal.
     - The number of atoms in each molecule.
     - Modify the "sections" and "modified" lists as needed to match your data.

## Understanding the Script


1. **Location Retrieval:**
   - The `firstindex` function determines the position (either line number or index) of the section titles in the original unit cell `.itp` file. This information is important for accurately extracting and processing the data.

2. **Enumerate Generator:**
   - The `enumerate` generator in the `ind_last` line identifies the final index of each section within the document. Make sure that sections in your file are separated by a single blank line for the script to function correctly.

3. **Temporary Text Files:**
   - During script execution, individual text files are created for each section. These temporary files do not include section titles.

4. **Data Line Selection:**
   - The following expressions are used to retrieve specific lines within each section:
     - `indexlist[sections.index(section)] + 2` obtains the first "data" line in each section (i.e., the first line in the range).
     - `indexlist[sections.index(section) + 1]` determines the last line in each section, stopping just before the index of the next section.

5. **writeitp Function:**
   - The `writeitp` function performs the following tasks:
     - Writes the section names and column names for each section.
     - Identifies the columns requiring modification (e.g., atom indices, ai, aj, ak in dihedrals, etc.).
     - Applies the necessary modifications (e.g., `t = i + numatoms * j`, where `i` iterates through the indices in the modified column, and `j` iterates through the specified number of molecules).
     - Appends the remaining unmodified columns to create a comprehensive dataframe.

## Conclusion

This Topology Maker generates `.itp` files for large crystal structures. You can tailor it to suit your specific project requirements.

Your contributions and feedback are greatly appreciated in further enhancing the functionality and usability of this script. Thank you for choosing this tool for your crystal building needs.

## Citation

If you use this script in your work or find it helpful, we kindly request that you consider citing us. A citation will be added when our manuscript is in press. 

