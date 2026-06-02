def proteins(strand):
    upper_strand = strand.upper()
    results = []  # start with empty list
    
    # step through the string 3 at a time
    for i in range(0, len(upper_strand), 3):
        codon = upper_strand[i:i+3]  # grab 3 letters starting at i
      
        if codon in ["AUG"]:
            results.append("methionine")
        elif codon in ["UUU", "UUC"]:
            results.append("Phenylalanine")
        elif codon in ["UUA", "UUG"]:
            results.append("Leucine")
        elif codon in ["UCU", "UCC", "UCA", "UCG"]:
            results.append("Serine")
        elif codon in ["UAU", "UAC"]:
            results.append("Tyrosine")
        elif codon in ["UGU", "UGC"]:
            results.append("Cysteine")
        elif codon in ["UGG"]:
            results.append("Tryptophan")
        elif codon in ["UAA", "UAG", "UGA"]:
            results.append("STOP")
        else:
            results.append("wrong codon")  # changed from print
  
    return results  # un-indented to match the for loop

print(proteins("AUGUUUUCUUAAAUG")) 