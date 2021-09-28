import os
import random
# import basic python packages
import numpy as np
import pandas as pd

# import torch packages
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader

from .deeptfactor.process_data import read_fasta_data
from .deeptfactor.data_loader import EnzymeDataset
from .deeptfactor.utils import argument_parser
from .deeptfactor.models import DeepTFactor



def deeptf(fasta_file):

    checkpt_file = '/home/justin/Master/Attribute_prediction/Python_scripts/packages/deeptfactorpkg/trained_model/DeepTFactor_ckpt.pt'
    device = 'cuda'
    num_cpu = 4
    batch_size = 128

    protein_data_file = fasta_file
    df = pd.DataFrame(columns = ['Gene Locus', 'Score', 'TF'])

    torch.set_num_threads(num_cpu)

    protein_seqs, seq_ids, slices = read_fasta_data(protein_data_file)
    pseudo_labels = np.zeros((len(protein_seqs)))
    proteinDataset = EnzymeDataset(protein_seqs, pseudo_labels)
    proteinDataloader = DataLoader(proteinDataset, batch_size=batch_size, shuffle=False)


    model = DeepTFactor(out_features=[1])
    model = model.to(device)

    ckpt = torch.load(f'{checkpt_file}', map_location=device)
    model.load_state_dict(ckpt['model'])
    cutoff = 0.5

    y_pred = torch.zeros([len(seq_ids), 1])
    with torch.no_grad():
        model.eval()
        cnt = 0
        for x, _ in proteinDataloader:
            x = x.type(torch.FloatTensor)
            x_length = x.shape[0]
            output = model(x.to(device))
            prediction = output.cpu()
            y_pred[cnt:cnt+x_length] = prediction
            cnt += x_length

    scores = y_pred[:,0]
    # with open(f'{output_dir}/prediction_result.txt', 'w') as fp:
    #     fp.write('sequence_ID\tprediction\tscore\n')
    for seq_id, score, slice in zip(seq_ids, scores, slices):
        if score > cutoff:
            tf = 1
        else:
            tf = 0
        score_int = torch.IntTensor.item(score)
        df = df.append({'Gene Locus': seq_id, 'Score': score_int, 'TF': tf},ignore_index= True)
            # fp.write(f'{seq_id}\t{tf}\t{score:0.4f}\n')
    return df


