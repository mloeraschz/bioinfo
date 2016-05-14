# -*- encoding: utf-8 -*-
from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO
from os import listdir
from os.path import isfile, join
import os
import sys

query = sys.argv[1] ## aquí escribe la ubicación de tus xmls

xmls = [ join(query,f)for f in listdir(query) if isfile(join(query,f)) and f.endswith('.xml') ]

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
                    c1 = record.query
                    c2 = hit.hit_id
                    c3 = str(hsp.expect)
                    with open('blast-hits.csv','a') as output:
                        linea = '%s,%s,%s\n' %(c1,c2,c3)
                        output.write(linea)
                    #print('Identities= %s'%hsp.identities)
                    #print('Gaps= %s'% hsp.gaps)
                    #print('Align length= %s'%hsp.align_length)
                    #print('Query seq= %s'% hsp.query)
                    #print('Query start, Query end= %s,%s' % (hsp.query_start, hsp.query_end))
                    #print('Match seq= %s'% hsp.match)
                    #print('Sbjct seq= %s'% hsp.sbjct)
                    #print('Sbjct start, Sbjct end= %s,%s' % (hsp.sbjct_start, hsp.sbjct_end))
                    break
            
                except ValueError:
                    pass
            break
