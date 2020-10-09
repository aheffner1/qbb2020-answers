#! /usr/bin/env python 3

import sys

from fasta_iterator_class import FASTAReader

dna_align_file = '/Users/cmdb/qbb2020-answers/week4-hw/q-seqdump.txt'
prot_align_file = '/Users/cmdb/qbb2020-answers/week4-hw/aa_align.fa'

dna_list = []; prot_list = []; dna_id_list = []; prot_id_list =[]; 

dna_aligns = FASTAReader(open(dna_align_file))
prot_aligns = FASTAReader(open(prot_align_file))


for dna_seq_id, dna_sequence in dna_aligns:
	dna_list.append(dna_sequence)
	dna_id_list.append(str(dna_seq_id)) 
for prot_seq_id, prot_sequence in prot_aligns:
	prot_list.append(str(prot_sequence))
	prot_id_list.append(prot_seq_id) 

dna_prot_list = []
for idn, dna, prot in zip(dna_id_list, dna_list, prot_list):
	codon_list = []; dna_from_prot = ''; count = 0;
	prot = str(prot)
	for i in range(0, len(dna)-2,3):
		codon = dna[i:i+3]
		codon_list.append(codon)
	for aa in prot: 
		if aa == '-':
			dna_from_prot = dna_from_prot + '---'	
		else: 
			if count < len(codon_list):
				dna_from_prot = dna_from_prot + str(codon_list[count])
				count += 1
	dna_prot_list.append(dna_from_prot)

for seq_id, seq in zip(dna_id_list, dna_prot_list):
	print('>'+seq_id)
	print(seq)	