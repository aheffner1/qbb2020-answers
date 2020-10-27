#! /usr/bin/env python 3

import sys
import pandas as pd
import numpy as np

# filenames
ref_file = '/Users/cmdb/qbb2020-answers/week6-hw/mm10_refseq_genes_chr6_50M_60M.bed'
E4_file = '/Users/cmdb/qbb2020-answers/week6-hw/SRR3083926_1.chr6_bismark_bt2_pe.sorted.bedGraph'
E5_file = '/Users/cmdb/qbb2020-answers/week6-hw/SRR3083929_1.chr6_bismark_bt2_pe.sorted.bedGraph'

# read files into dataframes
header1 = ['0', 'gene_id', 'chr', '3', 'start', 'stop', '6', '7', '8', '9', '10', '11', 'gene_name', '13', '14', '15']
header2 = ['chr', 'start', 'stop', 'methyl_percent']
ref = pd.read_csv(ref_file, sep = '\t', header=None, names = header1, skiprows=1)
E4 = pd.read_csv(E4_file, sep = '\t', header=None, names = header2, skiprows=1)
E5 = pd.read_csv(E5_file, sep = '\t', header=None, names = header2, skiprows=1)

# For each gene, find the fold change in mean methylation signal from E4 to E5.5 cells. 
methyl_dict = {}

for ref_key, ref_values in ref.iterrows():
    
    gene = ref_values['gene_name']
    ref_start = ref_values['start']
    ref_stop = ref_values['stop']

    # find methylation sites within gene for E4
    E4_in_gene = E4[(E4['start']<ref_stop) & (E4['start']>ref_start)]
    
    # if the mean methylation for a gene in E4 is zero, skip it.
    if E4_in_gene['methyl_percent'].sum() == 0: 
        continue

    # take mean of E4 methylation within gene 
    E4_me_per = ((E4_in_gene['stop'] - E4_in_gene['start'])*E4_in_gene['methyl_percent']).sum()
    # find methylation sites within gene for E5.5
    E5_in_gene = E5[(E5['start']<ref_stop) & (E5['start']>ref_start)]
    # take mean of E5 methylation within gene 
    E5_me_per = ((E5_in_gene['stop'] - E5_in_gene['start'])*E5_in_gene['methyl_percent']).sum()
    # find fold change of E5.5 to E4
    E5_E4_me = E5_me_per/E4_me_per
    methyl_dict[gene] = E5_E4_me

# add to ref dataframe
methyl = pd.DataFrame.from_dict(methyl_dict, orient = 'index', columns = ['E5_E4_fold_methyl_change'])

pd.set_option("display.max_rows", None, "display.max_columns", None)
print(methyl)

