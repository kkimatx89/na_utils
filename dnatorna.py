"""
convert DNA to RNA
"""

def rna(seq):
    """convert a DNA seq to RNA"""
    #Determine if the original seq was uppercase
    seq_upper = seq.isupper()
    #convert to lowercase
    seq = seq.lower()
    #swap out 't' for 'u'
    seq = seq.replace('t','u')

    if seq_upper:
        return seq.upper()
    else:
        return seq

def reverse_rna_complement(seq):
    """convert a DNA seq into its reverse comp as RNA"""
    #Determine if the original seq was uppercase
    seq_upper = seq.isupper()

    # Reverse seq, then complement
    seq = seq[::-1]
    seq = seq.upper()
    seq = seq.replace('A','u')
    seq = seq.replace('T','a')
    seq = seq.replace('G','c')
    seq = seq.replace('C','g')

    if seq_upper:
        return seq.upper()
    else:
        return seq
