# define the function to find the cut site of the restriction enzyme
def find_cut_site(dna_sequence, Recognised_Sequence):
    position = dna_sequence.find(Recognised_Sequence)  # Find the position of the recognised sequence
    if position != -1:
        return position + 1
    else:
        return "The recognised sequence was not found in the DNA sequence."

# Example DNA sequence
dna_sequence1 = "ATGCGTATACGCGTACGTACGTAGCTAGCTAGCTAGCTAGC"
Recognised_Sequence = "ATGC"
valid_nucleotides = {'A', 'T', 'G', 'C'}

# check if the input is valid
for nucleotide in dna_sequence1:
    if nucleotide not in valid_nucleotides:
        raise ValueError("Error: DNA sequence contains invalid characters. Only A, T, G, C are allowed.")

# print the result of the example
example = find_cut_site(dna_sequence1, Recognised_Sequence)
print(f"The cut site is: {example}")

# ask for user input
dna_sequence = input("Enter your DNA sequence: ")
Recognised_Sequence = input("Enter the sequence recognised by the restriction enzyme: ")

# check if the input is valid
valid_nucleotides = {'A', 'T', 'G', 'C'}
for nucleotide in dna_sequence:
    if nucleotide not in valid_nucleotides:
        raise ValueError("Error: DNA sequence contains invalid characters. Only A, T, G, C are allowed.")

# call the function and print the result
cut_site = find_cut_site(dna_sequence, Recognised_Sequence)
print(f"The cut site is: {cut_site}")
