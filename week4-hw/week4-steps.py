step 1: 
cat week4_query.fa seqdump.txt > q-seqdump.txt 

transeq -sequence q-seqdump.txt -outseq aa_seqdump.fa

step 2: 
mafft --auto aa_seqdump.fa > aa_align.fa

step 3: 
03-week-4.py
run using
python 03-week-4.py > aligned.fa

step 4: 
jupyter notebook 04-week-4.ipynb
