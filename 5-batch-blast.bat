@ECHO OFF
FOR %%f IN (%cd%\*.fasta) DO (
ECHO %%~ff

blastp -remote -db nr -query %%~ff -outfmt 5 -out %%~nf.xml
)
