from Bio import SeqIO
import re

patternS = re.compile("^[!-I]+$")
patternX = re.compile("^[;-h]+$")
patternI = re.compile("^[@-h]+$")
patternJ = re.compile("^[C-i]+$")
patternL = re.compile("^[!-j]+$")

qualityTypeArray = {"SP": True, "SS": True, "I1.3": True, "I1.5": True, "I1.8": True}

for seq_record in SeqIO.parse("reads_for_analysis.fastq", "fastq"):
    qualityString = seq_record.format("fastq").splitlines()[3]
    if not patternS.match(qualityString):
        qualityTypeArray["SP"] = False
    if not patternX.match(qualityString):
        qualityTypeArray["SS"] = False
    if not patternI.match(qualityString):
        qualityTypeArray["I1.3"] = False
    if not patternJ.match(qualityString):
        qualityTypeArray["I1.5"] = False
    if not patternL.match(qualityString):
        qualityTypeArray["I1.8"] = False

if qualityTypeArray["SP"] == True:
    print("Kokybės kodavimas: Sanger Phred+33")
if qualityTypeArray["SS"] == True:
    print("Kokybės kodavimas: Solexa Solexa+64")
if qualityTypeArray["I1.3"] == True:
    print("Kokybės kodavimas: Illumina 1.3+ Phred+64")
if qualityTypeArray["I1.5"] == True:
    print("Kokybės kodavimas: Illumina 1.5+ Phred+64")
if qualityTypeArray["I1.8"] == True:
    print("Kokybės kodavimas: Illumina 1.8+ Phred+33")