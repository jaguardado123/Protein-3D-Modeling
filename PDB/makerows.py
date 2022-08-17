import json

file=open("PDB/rcsb_pdb_ids.txt", "r")
lines = file.readlines()
# print(lines)
pdbs = lines[0].split(',')

i = 1
for pdb in pdbs:
    print(' <tr><td class="pdb" value="' + pdb + '">' + pdb + '</td></tr>')
    if (i == 50):
        break
    i = i + 1