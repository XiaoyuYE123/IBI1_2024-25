def restriction_enzyme_analysis():
    DNA_sequence = input("Enter a DNA sequence: ").upper()
    if not all(base in "ACGT" for base in DNA_sequence):
        print("Invalid DNA sequence. Please use only A, C, G, and T.")
        return
    else:
        restriction_enzymes = {
            "EcoRI": "GAATTC",
            "HindIII": "AAGCTT",
            "BamHI": "GGATCC"
            }
        for enzyme, site in restriction_enzymes.items():
            print(f"Analyzing {enzyme}...")
            if site in DNA_sequence:
                print(f"{enzyme} recognition site found at position {DNA_sequence.index(site)}")
            else:
                print(f"{enzyme} recognition site not found")
restriction_enzyme_analysis()