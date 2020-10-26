First downloaded files 

	SRR3083926_1.chr6.fastq		SRR3083926_2.chr6.fastq
	SRR3083929_1.chr6.fastq 	SRR3083929_2.chr6.fastq

Looked at files with less 
	
	looks normal

Use fastqc to look at the quality of these fastq files - 
fastqc SRR3083926_1.chr6.fastq

	the sequence is depleted of Cs due to the bisulfite treatment
	the percentage of Ts is high indicating this is the forward strand post PCR

Download chromosome 6 reference genome and move to its own directory called ref
mkdir ref/

Make bisulfite reference of chromosome 6
bismark_genome_preparation ref/

