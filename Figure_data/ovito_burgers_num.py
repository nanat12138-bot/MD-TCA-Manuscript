from ovito.io import import_file
from ovito.modifiers import DislocationAnalysisModifier
import pandas as pd


im_file = r"D:\input"##
pipeline = import_file(im_file)
export_file = r"D:\output.csv"##

# DXA
dxa = DislocationAnalysisModifier()
pipeline.modifiers.append(dxa)

data = pipeline.compute()

dislocations = data.dislocations.lines

rows = []
print("Found %i dislocation lines" % len(data.dislocations.lines))
for line in dislocations:
    #print("Dislocation %i: length=%f, Burgers vector=%s" % (line.id, line.length, line.true_burgers_vector))
    #print(line.points)

    rows.append({
        "ID": line.id,
        "length": line.length,
        "Burgers vectors": str(line.true_burgers_vector),
        })

# output
df = pd.DataFrame(rows)
df.to_csv(export_file, index=False)

print(df)