# importing necessary libraries
from Bio import SeqIO
# defines a function to load the BLOSUM62 matrix from a file
# The function reads the matrix from a text file and stores it in a dictionary
def load_matrix():
    # open the BLOSUM62 matrix file 
    with open(r"E:\2024_2025\IBI\IBI1_2024-25\IBI1_2024-25\Practical13\BLOSUM62.txt", "r") as f:
        # read the lines and split them into a list
        lines = f.readlines()
    # create a dictionary to store the BLOSUM62 matrix
    blosum = {}
    # parse the first line to get the labels
    labels = lines[0].strip().split()
    # iterate through the remaining lines to fill the dictionary
    for i, line in enumerate(lines[1:]):
        parts = line.strip().split()
        # row_label is the current amino acid label
        row_label = parts[0]
        # initialize an empty dictionary for the current row
        # and set the row_label as the key
        blosum[row_label] = {}
        # fill the dictionary with scores for each label
        for j, score in enumerate(parts[1:]):
            blosum[row_label][labels[j]] = int(score)
    return blosum
# The function takes two sequences and the BLOSUM62 matrix as input
# It calculates the alignment score and percentage identity between the two sequences
# The function uses the BLOSUM62 matrix to score the alignment
def pairwise_blosum_alignment(seq1, seq2, blosum):
    # set the initial score to 0
    # and the identity count to 0
    score = 0
    identity_count = 0
    alignment = []
    # check if the sequences are of equal length
    for a1, a2 in zip(seq1, seq2):
        s = blosum.get(a1, {}).get(a2, 0)
        score += s
        if a1 == a2:
            # if the amino acid is the same in both sequences,
            # increment the identity count and append a vertical bar to the alignment
            identity_count += 1
            alignment.append('|')
        else:
            # if the amino acid is different, append a space to the alignment
            alignment.append(' ')
    # calculate the percentage identity
        identity_percentage = (identity_count / len(seq1)) * 100
    return score, identity_percentage, alignment
# The function prints the sequences, their names, the alignment scores, and the total score
# It also prints the percentage identity between the two sequences  
def print_result(seq1_name, seq1, seq2_name, seq2, score, alignment=None):
    print(f">{seq1_name}\n{seq1}")
    print(f">{seq2_name}\n{seq2}")
    if alignment:
        print("Alignment scores:", alignment)
    print("Total score:", score)
# The main function loads the sequences from FASTA files, calculates the alignment score and percentage identity, and prints the results
# It uses the BLOSUM62 matrix for scoring
# The sequences are read from FASTA files using the SeqIO module from Biopython
# The function also handles the case where the sequences are of different lengths
if __name__ == "__main__":
    seq1_name = "human_SOD2"
    seq2_name = "mouse_SOD2"
    seq1 = str(next(SeqIO.parse('mouse_SOD2.fasta', "fasta")).seq)
    seq2 = str(next(SeqIO.parse('human_SOD2.fasta', "fasta")).seq)
    blosum = load_matrix()
    score, percentage_identity, alignment = pairwise_blosum_alignment(seq1, seq2, blosum)
    print_result(seq1_name, seq1, seq2_name, seq2, score, alignment)
    print("Percentage identity:", percentage_identity)