import edlib
from Bio import SeqIO
seqlist = []
for seq_record in SeqIO.parse("rosalind_edta.txt", "fasta"):
   seqlist += [str(seq_record.seq)]
query = seqlist[0]; target = seqlist[1]
dist = edlib.align(query, target,task="distance")
print(dist['editDistance'])
# NOTE: `task` has to be "path" in order to get nice alignment.
result = edlib.align(query, target, task = "path")
nice = edlib.getNiceAlignment(result, query, target)
print (nice['query_aligned'])
print (nice['target_aligned'])