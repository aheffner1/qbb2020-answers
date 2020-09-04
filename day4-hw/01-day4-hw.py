#! /usr/bin/env python 3

# import sys allows you to import other python scripts and run in command line
import sys

# allows fasta_iterator to be called as FASTAReader in script
from fasta_iterator_class import FASTAReader

# opens and reads 'droYak2_seq.fa' as quary and 'subset.fa' as target
query =  FASTAReader(open('droYak2_seq.fa'))
target = FASTAReader(open('subset.fa'))

# initialize a dictionary to store query kmers as keys and position as values
query_kmers = {}
k = 11     #kmer length

# 1. Read in query sequence 
for seq_id, sequence in query:
    # loops through nucleotide by nucleotide until the last one which has a start position of len(seq) - K + 1.
    for i in range(0, len(sequence) - k + 1):
        # loop through sequence ex. i = 0 kmer = seq[0:11], next loop i = [1:12]
        kmer = sequence[i:i + k]
        # set all dictionary value for all kmers to be a list
        query_kmers.setdefault(kmer, [])
        # append list for current kmer with i the start position of current kmer
        query_kmers[kmer].append(i)

#initialize a second dictionary with target kmers 
target_kmers = {}

#2. Store the target
for seq_id, sequence in target:
    for i in range(0, len(sequence) - k + 1):
        kmer = sequence[i:i + k]
        # now set default dictionary value to be a dictionary key = kmer
        # this way if there are kmers shared between sequences you can store all positions 
        #in one dictionary (saves time and storage)
        target_kmers.setdefault(kmer, {})
        # each target sequence adds a new key to nested dictionary key seq_id and value set to a list
        target_kmers[kmer].setdefault(seq_id, [])
        # append nested dictionary list with current i
        target_kmers[kmer][seq_id].append(i)

#3. Loop through each query match key to any in target
for kmer in query_kmers:
    
    # if kmer is not in target then we don't care about it and continue
    if kmer not in target_kmers:
        continue
        
    # the start of the query for current kmer is start_query
    start_query = query_kmers[kmer]
    
    #loop through each seq_id in nested dictionary at current kmer
    for seq_id in target_kmers[kmer]:   
        #start_target is the start position of the current seq_id and current kmer
        start_target = target_kmers[kmer][seq_id]
        # print in this order target_sequence_name, target_start, query_start, k-mer
        print(seq_id, start_target, start_query, kmer)

#if name is used to run through command line and other python scripts
if __name__ == "__main__":
    reader = FASTAReader(sys.stdin)