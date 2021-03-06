from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO
from os import listdir
from os.path import isfile, join
import os
import sys

query = 'C:\\ubicacion' ## aquí escribe la ubicación de tus xmls

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

## RETO 0: haz blastp para el archivo fasta de proteinas
## RETO 1: filtra los xmls de tal manera que solamente se impriman los hits con Evalue <= 1E-15
## RETO 2: genera un reporte en formato csv para cada
## proteina, donde haya columnas para: Query name, Hit ID y Evalue
# -*- encoding: utf-8 -*-
from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO
from os import listdir
from os.path import isfile, join

import os
import sys

query = 'C:\\Users\\Alumno\\Desktop\\Python_bioinfo\\1er_sesion\\fastas' ## aquí escribe la ubicación de tus xmls


xmls = [ join(query,f) for f in listdir(query) if join(query,f).endswith('.xml')]

print(xmls)


for xml in xmls:
	try:
		resultHandle=open(xml,"r")
		blast_record=NCBIXML.parse(resultHandle)
	
		for record in blast_record:
			for hit in record.alignments:
				for hsp in hit.hsps:
					evalue = hsp.expect
					print(evalue)
					if evalue <= float(1e-15):

						outline = record.query +','+hit.hit_id+','+str(hsp.expect)+'\n'
							
						
						with open('%s.csv'%record.query[:12],'a') as output:
							
							print(outline)
							output.writelines(outline)
			
				

	except (TypeError,ValueError):
		pass
	resultHandle.close()




## RETO 3: Automatiza este script usando la biblioteca sys, para que el usuario pueda correrlo desde la línea de comandos
