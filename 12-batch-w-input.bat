@ECHO OFF

blastp -remote -db nr -query %1 -outfmt 5 -out %~n1.xml
)
