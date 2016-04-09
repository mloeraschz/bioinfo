from Bio import Entrez
import sys
Entrez.email = "email"
# Bajador de PDFs de PMC: LOW THROUGHPUT (MENOS DE 20 IDs)
handle = Entrez.esearch(db='pmc',term='synthetic biology', reldate=60,retmax=10,datetype='pdat')
record = Entrez.read(handle)
print(record['IdList'])

ids = record['IdList']
import time
for e in ids:
    time.sleep(10)
    # efetch para cada e
    # grabar un archivo diferente para cada e
    url = "http://www.ncbi.nlm.nih.gov/pmc/articles/PMC"+e+"/pdf"
    filename = "PMC"+e+".pdf"
    from urllib import FancyURLopener
    class FakeMozilla(FancyURLopener):
        version = "Mozilla/5.0 (Windows; U; Windows NT 5.2; rv:1.9.2)Gecko/20100101 Firefox/3.6"
    FakeMozilla().retrieve(url, filename)

    #fetch_handle = Entrez.efetch(db="pmc",id=e,rettype= 'pdf', retmode="pdf")
    #data = fetch_handle.read()
    

    #with open('%s.pdf'%e,'w') as output:
        #output.write(data)
