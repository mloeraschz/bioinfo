from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram
from Bio import SeqIO
import os

#os.mkdir('figuras')


elemento = SeqIO.parse('contigs.gbf','genbank')

for x in elemento:
    print(x.id)
    #print(x.description)
    #print(x.features)
    for y in x.features:
        print(y.type)
        gd_diagram = GenomeDiagram.Diagram(x.id)
        gd_track_for_features = gd_diagram.new_track(1, name="Annotated Features")
        gd_feature_set = gd_track_for_features.new_set()

        if  y.type != 'gene':
        #Exclude this feature
            continue
        if len(gd_feature_set) % 2 == 0:
            color = colors.HexColor('#01DF01')
        else:
            color = colors.lightblue
        gd_feature_set.add_feature(y, color=color, label=True,sigil="ARROW",arrowshaft_height=1.0)
        gd_diagram.draw(format="linear", orientation="landscape", pagesize='A4',
                    fragments=4, start=0, end=len(x))
        
        gd_diagram.write("figuras/%s.png"%x.name, "PNG",dpi=600)
