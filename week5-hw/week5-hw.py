
PART I: ChIP-seq

DATA/INDEXING

	gunzip chr19.fa.gz g1e.tar.gz
	bowtie2-build chr19.fa chr19
	mkdir bowtie_index/
	mv chr19.* bowtie_index/

MAPPING READS

	for sample in CTCF_ER4 CTCF_G1E input_ER4 input_G1E
	do
	  bowtie2 -x bowtie_index/chr19 -U ${sample}.fastq -S ${sample}.sam -p 6
	  samtools view -bSo ${sample}.bam ${sample}.sam
	  samtools sort ${sample}.bam ${sample}.sorted
	  samtools index ${sample}.sorted
	done

CALLING PEAKS

	macs2 callpeak -t CTCF_ER4.bam -c input_ER4.bam --format=BAM --name=ER4 --gsize=138000000 --tsize=26
	macs2 callpeak -t CTCF_G1E.bam -c input_G1E.bam --format=BAM --name=G1E --gsize=138000000 --tsize=26

DIFFERENTIAL BINDING BETWEEN G1E (before) and ER4 (after)

	bedtools intersect -v -a ER4_summits.bed -b G1E_summits.bed > CTCF_gained.bed 		(lost - only from ER4_peak)
	bedtools intersect -v -a G1E_summits.bed -b ER4_summits.bed > CTCF_lost.bed 		(gained - only from G1E_peak)

NUMBER OF FEATURE OVERLAPPING

	for SAMPLE in G1E ER4
	do
		bedtools intersect -c -a Mus_musculus.GRCm38.94_features.bed -b ${SAMPLE}_summits.bed > counts_annot_${SAMPLE}.bed 
		echo 'promoter' > ${SAMPLE}_counts.bed
		grep 'promoter' counts_annot_${SAMPLE}.bed | cut -f7 | paste -sd+ - | bc >> ${SAMPLE}_counts.bed
		echo 'exon' >> ${SAMPLE}_counts.bed
		grep 'exon' counts_annot_${SAMPLE}.bed | cut -f7 | paste -sd+ - | bc >> ${SAMPLE}_counts.bed
		echo 'intron' >> ${SAMPLE}_counts.bed
		grep 'intron' counts_annot_${SAMPLE}.bed | cut -f7 | paste -sd+ - | bc >> ${SAMPLE}_counts.bed
	done

		ER4 - 
		promoter
		55
		exon
		52
		intron
		298

		G1E - 
		promoter
		43
		exon
		32
		intron
		275


PLOT
 
	01-week-5.ipynb
	Produce a two-panel plot containing two bar plots. The left panel should plot the number of CTCF binding sites 
	in each type of region (exon, intron…) for each cell type. The right panel should plot the number of sites lost and 
	gained during differentiation for each cell type.

PART 2: MOTIF DISCOVERY

	sort -rnk 7 ER4_peaks.narrowPeak | head -100 > ER4_100_narrowpeaks.bed
	bedtools getfasta -fi bowtie_index/chr19.fa -bed ER4_100_narrowpeaks.bed > ER4_100_narrowpeaks.fa
	meme-chip -oc ER4_meme -meme-maxw 20 -db  motif_databases/JASPAR/JASPAR_CORE_2016.meme ER4_100_narrowpeaks.fa

	LOGO is found under -  ER4_meme/meme_out/logo1.png
