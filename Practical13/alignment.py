from Bio import SeqIO

def load_matrix():
    with open(r"E:\2024_2025\IBI\IBI1_2024-25\IBI1_2024-25\Practical13\BLOSUM62.txt", "r") as f:
        lines = f.readlines()
    blosum = {}
    labels = lines[0].strip().split()
    for i, line in enumerate(lines[1:]):
        parts = line.strip().split()
        row_label = parts[0]
        blosum[row_label] = {}
        for j, score in enumerate(parts[1:]):
            blosum[row_label][labels[j]] = int(score)
    return blosum

def pairwise_blosum_alignment(seq1, seq2, blosum):
    score = 0
    identity_count = 0
    alignment = []
    for a1, a2 in zip(seq1, seq2):
        s = blosum.get(a1, {}).get(a2, 0)
        score += s
        if a1 == a2:
            identity_count += 1
            alignment.append('|')
        else:
            alignment.append(' ')
        identity_percentage = (identity_count / len(seq1)) * 100
    return score, identity_percentage, alignment

def print_result(seq1_name, seq1, seq2_name, seq2, score, alignment=None):
    print(f">{seq1_name}\n{seq1}")
    print(f">{seq2_name}\n{seq2}")
    if alignment:
        print("Alignment scores:", alignment)
    print("Total score:", score)

if __name__ == "__main__":
    seq1_name = "human_SOD2"
    seq2_name = "mouse_SOD2"
    seq1 = str(next(SeqIO.parse('mouse_SOD2.fasta', "fasta")).seq)
    seq2 = str(next(SeqIO.parse('human_SOD2.fasta', "fasta")).seq)
    blosum = load_matrix()
    score, percentage_identity, alignment = pairwise_blosum_alignment(seq1, seq2, blosum)
    print_result(seq1_name, seq1, seq2_name, seq2, score, alignment)
    print("Percentage identity:", percentage_identity)