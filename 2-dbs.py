## TEMA 2: Bio.Entrez (einfo)

## Biopython contiene métodos para acceder a las bases de datos Entrez del
## NCBI(PubMed,Nucleotide, Protein, etc.)

## El output generado es un archivo XML.

## Sin embargo, para evitar que se restrinja el acceso a las bases de datos
## de NCBI, hay que poner atención a los requisitos mencionados:

## 1. Para cualquier serie más de 100 búsquedas, hacerlas durante el fin de
## semana, o fuera de los tiempos pico de Estados Unidos.

## 2. Usar http://eutils.ncbi.nlm.nih.gov no la página estándar. Biopython
## usa esa página de manera automática.

## 3. No hacer más de una búsqueda cada tres segundos. Esto lo hace Biopython
## de manera automática.

## 4. Usar el parámetro de email para que NCBI pueda contactarte si ocurre
## algún problema.

## 5. Si usas Biopython dentro de un software más grande, especificarlo en
## el parámetro "tool".

## 6. Para búsquedas grandes, el NCBI recomienda usar la opción de historial
## de sesion (la string WebEnv).


## Vamos a empezar obteniendo info acerca de las bases de datos:

from Bio import Entrez
Entrez.email = "bio.mloera@gmail.com"
handle = Entrez.einfo()
result = handle.read()
print(result)

## Para interpretar este XML, podemos usar el siguiente código:
handle = Entrez.einfo()
record = Entrez.read(handle)
print(record.keys())
print(record['DbList'])

## El resultado es un diccionario que puede ser explorado. Vamos a imprimir
## la informacion de la db "pubmed".

handle = Entrez.einfo(db='pubmed')
record = Entrez.read(handle)
print(record['DbInfo'])

## Explora qué más informacion hay en 'DbInfo':

print(record['DbInfo'].keys())

## Con este código puedes acceder a los campos que se pueden utilizar con
## ESearch para limitar la búsqueda (por ejemplo, "UANL[AFFL]" limita la
## la búsqueda a entradas afiliadas a la UANL, y "Perez[AUTH]" limita la búsqueda
## a entradas asociadas a un autor con el apellido "Perez").

for field in record["DbInfo"]["FieldList"]:
    print("%(Name)s, %(FullName)s, %(Description)s" % field)

## RETO: Intenta hacer el paso anterior con otra base de datos. Ejemplo:

handle = Entrez.einfo(db='protein')
record = Entrez.read(handle)
print(record['DbInfo'])

for field in record["DbInfo"]["FieldList"]:
    print("%(Name)s, %(FullName)s, %(Description)s" % field)

#Referencia: http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc2
