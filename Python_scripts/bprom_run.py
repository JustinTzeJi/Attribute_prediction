import pandas as pd
import argparse
import subprocess
import Bio 
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

def argument_parser(version=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_file', required=True, 
                        help='Input Fasta with upstream') 
    parser.add_argument('-o', '--output_file', required=True, 
                        help='Output csv') 
    return parser

def bprom(gene_outpath, bprom_out):
    
    subprocess.run("export TSS_DATA=/home/justin/Master/Attribute_prediction/Promoter/Bprom/bprom_run/data ; /home/justin/Master/Attribute_prediction/Promoter/Bprom/bprom_run/bprom %s %s" % (gene_outpath, bprom_out), shell=True)

if __name__ == '__main__':
    parser = argument_parser()
    options = parser.parse_args()

    input = options.input_file
    output = options.output_file
    bprom_tmp = '/home/justin/Master/Attribute_prediction/Promoter/Bprom/tmp/tmp_in.fasta'
    bprom_out = '/home/justin/Master/Attribute_prediction/Promoter/Bprom/tmp/tmp_out.txt'
    df = pd.DataFrame(columns = ['Gene Locus', 'Promoter'])
    for record in SeqIO.parse(input, "fasta"):
        locus = record.id
        gene_seq = record.seq

        gene_rec = SeqRecord(gene_seq, id = locus)
        SeqIO.write(gene_rec, open(bprom_tmp, "w"), "fasta")

        bprom(gene_outpath=bprom_tmp, bprom_out=bprom_out)


        with open(bprom_out, 'r') as handle:
            promoter_str = int(handle.read().splitlines()[3].split('-', 1)[1].strip())
            # print (promoter_str)
            if promoter_str > 0:
                promoter = promoter_str
            elif promoter_str == 0:
                promoter = promoter_str
            else:
                promoter = 'No result from BPROM'
            df = df.append({'Gene Locus': locus, 'Promoter': promoter}, ignore_index=True)
    
    df.to_csv(output, index = False)



