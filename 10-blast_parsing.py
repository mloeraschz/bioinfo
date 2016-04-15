from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO
from os import listdir
from os.path import isfile, join
import os
import sys

query = 'C:\\Users\\Miguel\\Documents\\Master_thesis\\Thesis\\LAB\\mafia-files\\M-M\\ORF_ANALYSIS\\CDD'

xmls = [ join(query,f)for f in listdir(query) if isfile(join(query,f)) ]

for xml in xmls:
	resultHandle=open(xml,"r")
	blast_record=NCBIXML.parse(resultHandle)
	for record in blast_record:
		for hit in record.alignments:
			for hsp in hit.hsps:	
				try:

					#print(hsp)
					print('Name of query= %s' % record.query)
					print('Hit ID= %s'%hit.hit_id)
					print('Evalue= %s' %hsp.expect)
					print('Identities= %s'%hsp.identities)
					print('Gaps= %s'% hsp.gaps)
					print('Align length= %s'%hsp.align_length)
					print('Query seq= %s'% hsp.query)
					print('Query start, Query end= %s,%s' % (hsp.query_start, hsp.query_end))
					print('Match seq= %s'% hsp.match)
					print('Sbjct seq= %s'% hsp.sbjct)
					print('Sbjct start, Sbjct end= %s,%s' % (hsp.sbjct_start, hsp.sbjct_end))
				except TypeError:
					pass

## RETO 0: haz delta_blast para el archivo fasta de proteinas
## RETO 1: filtra los xmls de tal manera que solamente se impriman los hits con Evalue <= 1E-5
## RETO 2: genera un reporte en formato csv para cada
## proteina, donde haya columnas para: Query name, Hit ID y Evalue

