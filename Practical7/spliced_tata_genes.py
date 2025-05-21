import re
# store the splice donor/acceptor combination in a variable
# and check if it is valid
splice_type = input("Enter splice donor/acceptor combination (GTAG, GCAG, ATAC): ").upper()
valid_splice = {"GTAG", "GCAG", "ATAC"}
if splice_type not in valid_splice:
    print("Invalid splice combination. Please enter GTAG, GCAG, or ATAC.")
    exit()

# split the splice donor/acceptor combination into donor and acceptor
donor = splice_type[0:2]
acceptor = splice_type[2:4]

output_filename = f"{splice_type}_spliced_genes.fa"

# read the fasta file and split it into blocks
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', "r") as input_file, open(output_filename, "w") as output_file:
    # set the variables
    name = None
    sequence = []

    for line in input_file:
        # Remove whitespace at the beginning and end of a line
        line = line.strip()

        # judge if the line is a line describe the information of the gene or a line of gene sequence
        if line.startswith('>'):
            seq_str = ''.join(sequence)

            # re.search to find if there are TATA boxes and donor and acceptor simultaneously in the gene
            if re.search(r'TATA[AT]A[AT]', seq_str) and re.search(rf'{donor}.+{acceptor}', seq_str):
                # count the number of TATA box in the gene eligible
                count = len(re.findall(r'TATA[AT]A[AT]', seq_str))

                # write the gene to the output file
                # using regular expressions to get the gene’s name
                gene_name_match = re.search(r'gene:([^\s]+)', line)
                name = gene_name_match.group(1)
                output_file.write(f"{name} TATA_count:{count}\n{seq_str}\n")

            # after adding a gene with TATA box, reset the variables for next gene
            sequence = []
            name = None

        # if the line is DNA sequence, append this line to the sequence
        else:
            sequence.append(line)