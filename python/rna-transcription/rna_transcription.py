def to_rna(dna_strand):
    dna_strand = dna_strand.upper()
    dna_choices = "GCTA"
    rna_strand = ""
    for char in dna_strand:
        if char not in dna_choices:
            raise ValueError('Invalid input')
        if char == 'G':
            rna_strand += "C"
        elif char =='C':
            rna_strand += "G"
        elif char =='T':
            rna_strand += "A"
        elif char =='A':
            rna_strand += "U"
    return rna_strand
