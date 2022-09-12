GENETIC_CODE = {
'UUU':'Phe', 'UUC':'Phe', 'UCU':'Ser', 'UCC':'Ser',
'UAU':'Tyr', 'UAC':'Tyr', 'UGU':'Cys', 'UGC':'Cys',
'UUA':'Leu', 'UCA':'Ser', 'UAA':None, 'UGA':None,
'UUG':'Leu', 'UCG':'Ser', 'UAG':None, 'UGG':'Trp',
'CUU':'Leu', 'CUC':'Leu', 'CCU':'Pro', 'CCC':'Pro',
'CAU':'His', 'CAC':'His', 'CGU':'Arg', 'CGC':'Arg',
'CUA':'Leu', 'CUG':'Leu', 'CCA':'Pro', 'CCG':'Pro',
'CAA':'Gln', 'CAG':'Gln', 'CGA':'Arg', 'CGG':'Arg',
'AUU':'Ile', 'AUC':'Ile', 'ACU':'Thr', 'ACC':'Thr',
'AAU':'Asn', 'AAC':'Asn', 'AGU':'Ser', 'AGC':'Ser',
'AUA':'Ile', 'ACA':'Thr', 'AAA':'Lys', 'AGA':'Arg',
'AUG':'Met', 'ACG':'Thr', 'AAG':'Lys', 'AGG':'Arg',
'GUU':'Val', 'GUC':'Val', 'GCU':'Ala', 'GCC':'Ala',
'GAU':'Asp', 'GAC':'Asp', 'GGU':'Gly', 'GGC':'Gly',
'GUA':'Val', 'GUG':'Val', 'GCA':'Ala', 'GCG':'Ala',
'GAA':'Glu', 'GAG':'Glu', 'GGA':'Gly', 'GGG':'Gly'}

# DNA sequence for translation
seq = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

def translate(seq, GENETIC_CODE):
    seq = seq.upper()
    protein = []
    for i in range(0, len(seq), 3):
        codon = seq[i:i+3]
        if GENETIC_CODE[codon] != None:
            protein.append(GENETIC_CODE[codon])
        else:
            break
    return protein

print(translate(seq, GENETIC_CODE))