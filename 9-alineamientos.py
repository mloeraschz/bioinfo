from Bio import AlignIO
from Bio.Seq import Seq
from Bio import Alphabet
from Bio.Alphabet import IUPAC, Gapped
from Bio.SeqRecord import SeqRecord


handle = AlignIO.parse('clustalw_output.aln','clustal')



# Parseando un archivo .aln y haciendo zoom en una
# zona del alineamiento

zoom = [] # En esta lista van a ir nuestras secuencias


for ali in handle:
	
	# Esta es la region en la que queremos hacer
	# zoom
	
	print(ali[:,30:50])
	print(ali.get_alignment_length())
	
	# Ahora vamos a tratar de obtener la secuencia
	# de cada elemento por separado


	for (index,elemento) in enumerate(ali):
		print(elemento.id)
		print(elemento.seq[30:50])
		sec = str(elemento.seq[30:50])
		if '-' in sec:
			pass
		else:
			zoom.append(Seq(sec,IUPAC.protein))
		
print(zoom)
from Bio import motifs

m = motifs.create(zoom)
print(m.counts)
print(m.counts['V'])
print(m.consensus)

## Ahora vamos a intentar con secuencias nucleotídicas. En este tipo de secuencias
## es posible aplicar el método .degenerate_consensus.

secs = [Seq('ATTATATG'),Seq('ATTTTATG'),Seq('ATTAAATG'),Seq('ATTATATG'),Seq('ATGGCATG'),Seq('ATTGTATG'),Seq('ATAGAGTG'),Seq('CCATATAG'),Seq('ATTATATG'),Seq('ATTATATC')]

m = motifs.create(secs)
print(m.counts)
print(m.consensus)
print(m.degenerate_consensus)


