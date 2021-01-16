from Bio import SeqIO
from Bio import Entrez
genbanklist = []
fastalengths = {}
with open('rosalind_frmt.txt') as file:
  for line in file:
    genbanklist = line.split(' ')
Entrez.email = "ghill@gwu.edu"
handle = Entrez.efetch(db="nucleotide", id=genbanklist, rettype="fasta")
record = list (SeqIO.parse(handle, "fasta")) #we get the list of SeqIO objects in FASTA format
shortest = 0
length = 0

for x in range(0, len(record)):
    rec = record[x].seq
    lengthC = len(rec)
    if x == 0:
        length = lengthC
    else:
        if lengthC < length:
            shortest = x
            length = lengthC

print ('>', record[shortest].description, sep='')
print (record[shortest].seq)