import re

# read the fasta file
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', "r") as f:
    input_file = f.read()

# split the input file into blocks
input_file = re.split(r'\n>', input_file)
if not input_file[0].startswith('>'):
    input_file[0] = '>' + input_file[0]

# create a new fasta file to store the results
# split the string and store the output in list
# store the mRNA names and their mRNA sequences seperately
with open("tata_genes.fa", "w") as output:
    for block in input_file:
        lines = block.strip().split('\n')
        header_line = lines[0]
        if not header_line.startswith('>'):
            header_line = '>' + header_line
        # store the sequence in a string
        sequence = ''.join(lines[1:]).upper()
        # extract gene name
        gene_match = re.match(r'^>(\S+)', header_line)
        if gene_match:
            gene_name = gene_match.group(1)
        else:
            gene_name = "Unknown"
        # match TATA box in the sequence
        matches = re.findall(r'TATA[AT]A[AT]', sequence)
        if matches:
            output.write(f">{gene_name}\n{sequence}\n")
