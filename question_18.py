from Bio import Align
from Bio.Align import substitution_matrices
from Bio import SeqIO
seqlist = []
for seq_record in SeqIO.parse("rosalind_edta.txt", "fasta"):
   seqlist += [str(seq_record.seq)]
query = seqlist[0]; target = seqlist[1]
aligner = Align.PairwiseAligner()
matrix = substitution_matrices.load("BLOSUM62")
aligner.substitution_matrix = matrix
aligner.open_gap_score = -5
alignment = aligner.align(query, target)
score = aligner.score(query, target)
print(score)