import numpy as np
from Bio import SeqIO
from sklearn.model_selection import train_test_split


    
def parse_fasta_data(translated_seq, locus, len_criteria=1000):
    result = []
    seq_ids = []
    #fp = fasta_file

    seq = translated_seq
    
    if len(seq) <= len_criteria:
        seq += '_' * (len_criteria-len(seq))
        result.append(seq)
        seq_ids.append(locus)

    # for seq_record in SeqIO.parse(fp, 'fasta'):
    #     seq = seq_record.seq
    #     seq_id = seq_record.id
    #     if len(seq) <= len_criteria:
    #         seq += '_' * (len_criteria-len(seq))
    #         result.append(str(seq))
    #         seq_ids.append(seq_id)
    #fp.close()
    return result, seq_ids