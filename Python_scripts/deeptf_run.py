import pandas as pd
import torch
import argparse
from packages.deeptfactorpkg.tf_running import deeptf

def argument_parser(version=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_file', required=True, 
                        help='Input Protein Fasta') 
    parser.add_argument('-0', '--output_file', required=True, 
                        help='Output csv') 
    return parser

if __name__ == '__main__':
    parser = argument_parser()
    options = parser.parse_args()

    input = options.input_file
    output = options.output_file

    df = deeptf(input)

    df[df['Score'] == df.groupby('Gene Locus')['Score'].transform('max')].to_csv(output, index = False)