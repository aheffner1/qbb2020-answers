#!/bin/bash

for SAMPLE in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63

do
	samtools sort -o ${SAMPLE}.BAM ${SAMPLE}.sam
done
