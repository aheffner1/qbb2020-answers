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
        target_kmers[kmer].setdefault(seq_id, [])
        target_kmers[kmer][seq_id].append(i)

#3. Loop through each query match key to any in target



for kmer in query_kmers:
    if kmer not in target_kmers:
        continue
# matching kmers - key = kmer value is list with start of query and start of targets
    start_query = query_kmers[kmer]

    for seq_id in target_kmers[kmer]:
        start_target = target_kmers[kmer][seq_id]
        print(seq_id, start_target, start_query, kmer)

#target_sequence_name    target_start    query_start k-mer

if __name__ == "__main__":
    reader = FASTAReader(sys.stdin)