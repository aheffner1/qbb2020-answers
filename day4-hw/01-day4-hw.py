#! /usr/bin/env python 3
import sys

from fasta_iterator_class import FASTAReader
query =  FASTAReader(open('droYak2_seq.fa'))
target = FASTAReader(open('subset.fa'))

query_kmers = {}
k = 11     #kmer length

# 1. Read in query sequence 
for seq_id, sequence in query:
    for i in range(0, len(sequence) - k + 1):
        kmer = sequence[i:i + k]
        
        query_kmers.setdefault(kmer, [])
        query_kmers[kmer].append(i)
        
target_kmers = {}
        
#2. Store the target
for seq_id, sequence in target:
    for i in range(0, len(sequence) - k + 1):
        kmer = sequence[i:i + k]
        
        target_kmers.setdefault(kmer, {})
        target_kmers[kmer][seq_id] = i
        
#3. Loop through each query match key to any in target
matching_kmers = {}
for kmer in query_kmers:
    if kmer in target_kmers:
        # matching kmers - key = kmer value is list with start of query and start of targets
        start_target = target_kmers[kmer]
        start_query = query_kmers[kmer]
        matching_kmers.setdefault(kmer, [])
        matching_kmers[kmer] = [start_query, start_target]

for key in matching_kmers:
    print(key, matching_kmers[key])

if
    