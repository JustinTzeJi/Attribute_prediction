import numpy as np
from Bio import SeqIO
from sklearn.model_selection import train_test_split


    
def read_fasta_data(fasta_file, len_criteria=1000):
    result = []
    seq_ids = []
    seq_slices = []
    fp = open(fasta_file, 'r')
    for seq_record in SeqIO.parse(fp, 'fasta'):
        seq = seq_record.seq
        seq_id = seq_record.id
        seq_slice = seq_record.description
        if len(seq) <= len_criteria:
            seq += '_' * (len_criteria-len(seq))
            result.append(str(seq))
            seq_ids.append(seq_id)
            seq_slices.append(seq_slice)
    fp.close()
    return result, seq_ids, seq_slices