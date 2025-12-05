import numpy as np
import pandas as pd
import random

SEED = 42
np.random.seed(SEED)
random.seed(SEED)

motifs_dict = {
        'Human': ['GGGCGGG', 'TATAAA', 'CCAAT'],
        'Bacteria': ['TTGACA', 'TATAAT', 'AGGAGG'],
        'Plant': ['CACGTG', 'TTGACC', 'ACGTG', 'TGTCTC'],
        'Virus': ['AATAAA', 'TATAA', 'AGCAAA','CAGT','TGTT']
    }

def reset_dataset():
    df_original = pd.read_csv("utils/dna_dataset_original.csv")
    df_shuffled = df_original.sample(frac=1, random_state=SEED).reset_index(drop=True)
    df_shuffled.to_csv("utils/dna_dataset.csv", index=False)

def generate_sequence(label, length=400, num_motifs=8, mutation_rate=0.2):

    # Random starting DNA
    seq = ''.join(np.random.choice(['A','C','G','T'], size=length))

    motifs = motifs_dict[label]

    for _ in range(num_motifs):
        # Pick one motif 
        motif = list(random.choice(motifs))

        # Mutate motif
        for i in range(len(motif)):
            if np.random.rand() < mutation_rate:
                motif[i] = random.choice(['A','C','G','T'])

        motif = ''.join(motif)

        # Insert motif at random place
        pos = np.random.randint(0, length - len(motif))
        seq = seq[:pos] + motif + seq[pos + len(motif):]

    return seq

data = []
for label in ['Human', 'Bacteria', 'Plant', 'Virus']:
    for _ in range(2000):
        data.append({
            'Sequence': generate_sequence(label),
            'Class_Label': label
        })

df = pd.DataFrame(data)

df_shuffled = df.sample(frac=1, random_state=SEED).reset_index(drop=True)

df_shuffled.to_csv("utils/dna_dataset.csv", index=False)

print("Dataset generated with seed =", SEED)