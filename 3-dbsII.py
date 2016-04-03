## TEMA 2.2. Bio.Entrez (esearch)

## El método Bio.Entrez.esearch() permite hacer búsquedas dentro de las
## bases de datos de Entrez.

## Por ejemplo, hagamos una búsqueda en PubMed:

from Bio import Entrez
Entrez.email = "bio.mloera@gmail.com" # No olvides escribir tu email
handle = Entrez.esearch(db='pubmed',term='synthetic biology', reldate=60,retmax=100,datetype='pdat')
record = Entrez.read(handle)
print(record.keys())
print(record['IdList'])
print(record['Count'])

# db = base de datos a utilizar
# term = término a buscar
# retmax = número de resultados para almacenar (default es 20). Si se quiere
# trabajar con más de 100,000 resultados, hay hacerlo con más de
# una búsqueda.
# datetype = hay diferentes opciones para la fecha "mdat" es la fecha de modificación
#           "pdat" es la fecha de publicación, "edat" es la fecha Entrez.
# reldate = entero x que limita la búsqueda a los ítems publicados en los últimos
#           x días de la fecha especificada en datetype
# mindate = fecha mínima para datetype (debe usarse en conjunto con maxtype)
# max date = fecha máxima para dateype (debe usarse en conjunto con maxtype)


handle = Entrez.esearch(db='pmc',term='synthetic biology[title] AND free fulltext[filter]',retmax=100,datetype='pdat',mindate='2014',maxdate='2016')
record = Entrez.read(handle)
print(record.keys())
print(record['IdList'])
print(record['Count'])

## RETO: Intenta hacer lo mismo con otras bases de datos. Por ejemplo:

handle = Entrez.esearch(db='protein',term='CRY AND Bacillus[Orgn]',retmax=100)
record = Entrez.read(handle)
print(record.keys())
print(record['IdList'])
print(record['Count'])

## Intenta haciendo más búsquedas. Es importante que te familiarices con este
## método porque la lista de IDs que generamos nos va a servir para
## bajar los record completos usando el método .efetch().


