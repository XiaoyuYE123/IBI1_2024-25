import re

# store the splice donor/acceptor combination in a variable
# and check if it is valid
splice_type = input("Enter splice donor/acceptor combination (GTAG, GCAG, ATAC): ").upper()

valid_splice = {"GTAG", "GCAG", "ATAC"}
if splice_type not in valid_splice:
    print("Invalid splice combination. Please enter GTAG, GCAG, or ATAC.")
    exit()

output_filename = f"{splice_type}_spliced_genes.fa"

# read the fasta file and split it into blocks
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', "r") as f:
    input_file = f.read()

input_file = re.split(r'\n>', input_file)
if not input_file[0].startswith('>'):
    input_file[0] = '>' + input_file[0]

# extract their sequences which match the input splice donor
with open(output_filename, "w") as output:
    for block in input_file:
        lines = block.strip().split('\n')
        header_line = lines[0]
        if not header_line.startswith('>'):
            header_line = '>' + header_line
        sequence = ''.join(lines[1:]).upper()

        # extract the gene names from the header line
        gene_match = re.match(r'^>(\S+)', header_line)
        if gene_match:
            gene_name = gene_match.group(1)  
        else:
            gene_name = "Unknown"

        # match the splice donor/acceptor combination in the sequence
        if splice_type in sequence:
            tata_matches = re.findall(r'TATA[AT]A[AT]', sequence)
            tata_count = len(tata_matches)
            
            if tata_count > 0:
                # fasta 格式输出：>gene_name_TATAcount\nsequence
                output.write(f">{gene_name}_the number of TATA box instances is {tata_count}\n{sequence}\n")
