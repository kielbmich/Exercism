translation = {
    "AUG" : "Methionine", 
    "UUU" : "Phenylalanine", 
    "UUC" : "Phenylalanine",
    "UUA" :	"Leucine",
    "UUG" : "Leucine",
    "UCU" : "Serine",
    "UCC" : "Serine",
    "UCA" : "Serine", 
    "UCG" : "Serine",
    "UAU" : "Tyrosine",
    "UAC" : "Tyrosine",
    "UGU" : "Cysteine",
    "UGC" : "Cysteine",
    "UGG" : "Tryptophan",
}

STOP  = ["UAA", "UAG", "UGA"]

def proteins(strand):
    out = []
    for i in range(0, len(strand) - 1, 3):
        codon = strand[i:i+3]
        if codon in translation:
            out.append(translation[codon])
        if codon in STOP:
            break
    return out