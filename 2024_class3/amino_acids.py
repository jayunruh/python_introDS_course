AMINO_ACID_CODES = [
    "A",
    "R",
    "N",
    "D",
    "C",
    "E",
    "Q",
    "G",
    "H",
    "I",
    "L",
    "K",
    "M",
    "F",
    "P",
    "S",
    "T",
    "W",
    "Y",
    "V",
]
AMINO_ACID_NAMES = [
    "Alanine",
    "Arginine",
    "Asparagine",
    "Aspartic acid",
    "Cysteine",
    "Glutamic acid",
    "Glutamine",
    "Glycine",
    "Histidine",
    "Isoleucine",
    "Leucine",
    "Lysine",
    "Methionine",
    "Phenylalanine",
    "Proline",
    "Serine",
    "Threonine",
    "Tryptophan",
    "Tyrosine",
    "Valine",
]

AMINO_ACID_CODONS = [
    ["GCT", "GCC", "GCA", "GCG"],  # Alanine
    ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"],  # Arginine
    ["AAT", "AAC"],  # Asparagine
    ["GAT", "GAC"],  # Aspartic acid
    ["TGT", "TGC"],  # Cysteine
    ["GAA", "GAG"],  # Glutamic acid
    ["CAA", "CAG"],  # Glutamine
    ["GGT", "GGC", "GGA", "GGG"],  # Glycine
    ["CAT", "CAC"],  # Histidine
    ["ATT", "ATC", "ATA"],  # Isoleucine
    ["TTA", "TTG", "CTT", "CTC", "CTA", "CTG"],  # Leucine
    ["AAA", "AAG"],  # Lysine
    ["ATG"],  # Methionine
    ["TTT", "TTC"],  # Phenylalanine
    ["CCT", "CCC", "CCA", "CCG"],  # Proline
    ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"],  # Serine
    ["ACT", "ACC", "ACA", "ACG"],  # Threonine
    ["TGG"],  # Tryptophan
    ["TAT", "TAC"],  # Tyrosine
    ["GTT", "GTC", "GTA", "GTG"],  # Valine
]

AMINO_ACID_WEIGHTS = {
    "A": 89.1,
    "R": 174.2,
    "N": 132.1,
    "D": 133.1,
    "C": 121.2,
    "E": 147.1,
    "Q": 146.2,
    "G": 75.1,
    "H": 155.2,
    "I": 131.2,
    "L": 131.2,
    "K": 146.2,
    "M": 149.2,
    "F": 165.2,
    "P": 115.1,
    "S": 105.1,
    "T": 119.1,
    "W": 204.2,
    "Y": 181.2,
    "V": 117.1,
}
