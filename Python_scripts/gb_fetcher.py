import argparse
from Bio import Entrez

def argument_parser(version=None):

    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output_file', required=True, 
                        help='Output File name')
    parser.add_argument('-i', '--acc_id', required=True, 
                        help='Accession ID')
    parser.add_argument('-e', '--entrez_email', required=True,
                        help='Entrez Email')    
    return parser

if __name__ == '__main__':
    parser = argument_parser()
    options = parser.parse_args()

    acc_id = options.acc_id
    output = options.output_file
    Entrez.email = options.entrez_email

    print("Fetching " + acc_id + ".gb")

    handle = Entrez.efetch(db= 'nuccore', id = acc_id, rettype = "gbwithparts", retmode = "text")

    ##with open(output, 'w') as out_handle:
    ##    out_handle.write(handle.read())
    
    print(acc_id + ".gb saved")