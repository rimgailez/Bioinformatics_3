from Bio import SeqIO

allReadGCPercentages = []
readCountsByGCPercentage = []

for seq_record in SeqIO.parse("reads_for_analysis.fastq", "fastq"):
    sequence = seq_record.seq
    GCPercentage = (sequence.count("C")+sequence.count("G"))/len(sequence)
    rounded = "{:.2f}".format(GCPercentage)
    allReadGCPercentages.append(rounded)

percentage = 0.00
for i in range(0, 100):
    readCountsByGCPercentage.append({"{:.2f}".format(percentage), allReadGCPercentages.count("{:.2f}".format(percentage))})
    percentage = percentage+0.01

print(readCountsByGCPercentage)