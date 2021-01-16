from Bio import Align
from Bio.Align import substitution_matrices
from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
seqlist = []
for seq_record in SeqIO.parse("rosalind_edta.txt", "fasta"):
   seqlist += [seq_record.seq]
query = seqlist[0]; target = seqlist[1]
aligner = Align.PairwiseAligner()
matrix = substitution_matrices.load("PAM250")
aligner.substitution_matrix = matrix
aligner.mode = 'local'
aligner.open_gap_score = -5
aligner.extend_gap_score = -5
score = aligner.score(query, target)
print(score)
pam250 = substitution_matrices.load("PAM250")
alignments = pairwise2.align.localds(query, target, pam250, -5, -5)
print(pairwise2.format_alignment(*alignments[0]))