# opening file
f = open("DNAseq.txt", "r")
# defining terms
FASTAcount = 0
gc = 0
at = 0
Nseqcount = 0
FASTAdict = {}
Ndict = {}
# looping through lines in file
for x in f:
  if x.startswith('>'):
    # getting the sequence name
     x = x.replace('>', '')  
     x = x.replace('\n', '')
     FASTAcount = FASTAcount + 1
     FASTAdict[FASTAcount] = x
     # calculating gc content %
     if (gc + at) > 0:
      Nseqcount = Nseqcount + 1
      total = gc + at
      percentage = float(gc / total * 100)
      Ndict[Nseqcount] = percentage
    # resetting gc counts
     gc = at = 0
  else:
    # getting gc counts from DNA sequence lines
    nuc_str = list(x.strip())
    for n in nuc_str:
      if n == 'G' or n == 'C':
        gc += 1.0
      elif n == 'A' or n == 'T':
        at += 1.0
# running gc % calculation again to get last one
Nseqcount = Nseqcount + 1
total = gc + at
percentage = float(gc / total * 100)
Ndict[Nseqcount] = percentage
# acquiring the highest GC content & its name from dictionaries
maxval = max(Ndict, key=Ndict.get)
print (FASTAdict[maxval])
print (Ndict[maxval])