#!/usr/bin/env python3
"""
Simple script to combine multiple PDB files into a single multi-model PDB file
for visualization in PyMOL.
"""

import os
import glob

# Output file name
output_file = "combined_models.pdb"

# Find all PDB files in the current directory
pdb_files = sorted(glob.glob("*.pdb"))

if not pdb_files:
    print("Error: No PDB files found in current directory")
    exit(1)

# Combine PDB files into one multi-model PDB
with open(output_file, 'w') as outfile:
    for i, pdb_file in enumerate(pdb_files):
        model_num = i + 1
        
        # Write model header
        outfile.write(f"MODEL     {model_num}\n")
        outfile.write(f"REMARK   1 MODEL NAME: {os.path.basename(pdb_file)}\n")
        
        # Copy PDB content, skipping existing MODEL/ENDMDL lines
        with open(pdb_file, 'r') as infile:
            for line in infile:
                if not (line.startswith("MODEL") or line.startswith("ENDMDL")):
                    outfile.write(line)
        
        outfile.write("ENDMDL\n")

print(f"Combined {len(pdb_files)} models into {output_file}")
print(f"You can now open {output_file} in PyMOL")