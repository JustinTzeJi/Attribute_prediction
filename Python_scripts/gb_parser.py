import argparse
import Bio 
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import os
import pandas as pd
import subprocess
import re

def argument_parser(version=None):

    parser = argparse.ArgumentParser()
    parser.add_argument('-of', '--output_fna', required=True, 
                        help='Output File name')
    parser.add_argument('-ou', '--output_upstream', required=True, 
                        help='Output File name')
    parser.add_argument('-op', '--output_protein', required=True, 
                        help='Output File name')
    parser.add_argument('-i', '--input_file', required=True, 
                        help='Input File Name')  
    return parser

if __name__ == '__main__':
    parser = argument_parser()
    options = parser.parse_args()

    input = options.input_file
    output_fna = options.output_fna
    output_upstream = options.output_upstream
    output_protein = options.output_protein

    #for seq file construction
    fna = []
    protein = []
    upstream = []

    #parsing
    record = SeqIO.parse(open(input), "gb")
    for seq_record in record:
        max_length = len(seq_record.seq) #for reverse strands

        #retrieve nucleotide and protein sequences from each CDS
        for feature in seq_record.features:
            if feature.type == "CDS":
                #nucleotide sequence
                #obtain gene coordinates
                mystart = feature.location.start.position
                myend = feature.location.end.position 

                #obtain gene locus (studies generally use the old locus tags)
                locus_key = 'old_locus_tag'

                if locus_key in feature.qualifiers:
                    locus = ''.join(feature.qualifiers[locus_key])
                else:
                    locus = ''.join(feature.qualifiers['locus_tag'])

                #obtain gene strand info, reverse complement the antisense strand
                if feature.strand == -1:
                    this_start = mystart
                    this_end = myend
                    if this_end + 150 <= max_length:
                        this_end = myend + 150 #append upstream gene
                    gene_seq_upstream = seq_record.seq[this_start:this_end].reverse_complement()
                    dna_seq = seq_record.seq[mystart:myend].reverse_complement()
                else:
                    this_start = mystart
                    this_end = myend
                    if this_start - 150 >= 0:
                        this_start = mystart - 150 #append upstream gene
                    gene_seq_upstream = seq_record.seq[this_start:this_end]
                    dna_seq = seq_record.seq[mystart:myend]
                
                #creating seq records and appending to list
                gene_rec_upstream = SeqRecord(gene_seq_upstream, id="%s" % (locus))
                gene_rec_fna = SeqRecord(dna_seq, id="%s" % (locus))
                upstream.append(gene_rec_upstream)
                fna.append(gene_rec_fna) 
            
                ######protein sequence######################################################
                translation_key = 'translation'
                slices = 0

                if translation_key in feature.qualifiers:
                    translated_seq = Seq(''.join(feature.qualifiers['translation']))
                    if len(translated_seq) > 1000:
                        ##slicing seq >1000 nt to 1000 nt in a list. If TF is found break from loop
                        translated_seq_list = [translated_seq[i:i+1000] for i in range(len(translated_seq)-999)]
                        for seq in translated_seq_list:
                            slices += 1
                            protein_rec = SeqRecord(seq, id=locus, description = "%s" %slices)
                            protein.append(protein_rec)
                    protein_rec = SeqRecord(translated_seq, id=locus, description = "%s" %slices)
                    protein.append(protein_rec)
                else:
                    translated_seq = Seq('MMMMMMMM')
                    protein_rec = SeqRecord(seq, id=locus, description = "%s" %slices)
                    protein.append(protein_rec)            

    SeqIO.write(fna, open(output_fna, "w"), "fasta")
    SeqIO.write(protein, open(output_protein, "w"), "fasta")
    SeqIO.write(upstream, open(output_upstream, "w"), "fasta")