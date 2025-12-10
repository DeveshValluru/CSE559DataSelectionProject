import os
from tqdm import tqdm
import numpy as np

folder = "/scratch/abunn12/CSE559_Final_data/unlabeled_data/train/train_prefix"
new_folder = "/scratch/abunn12/CSE559_Final_data/unlabeled_data/length_variety"

seqs = []
lengths = []

for filename in tqdm(os.listdir(folder)):
    with open(os.path.join(folder, filename), 'r') as f:
        seqs.extend([line.strip().split(" ") for line in f.readlines()])

lengths = [len(seq) for seq in seqs]


# This will (conceptually) take all the sequences and take data points away from the most common length until there is only keep_ratio of the data left
# It actually first calculates the amount it needs to cap each bin at to arrive at 60% and then does a random selection of this amount for every bin that exceeds the cap.
def flatten_distribution(seqs, lengths, keep_ratio=0.6):
    target = int(len(lengths) * keep_ratio)
    min_len = min(lengths)
    max_len = max(lengths)

    bin_edges = np.arange(min_len, max_len + 2)
    bin_counts, _ = np.histogram(lengths, bins=bin_edges)

    argsorted_bins = bin_counts.argsort()[::-1]
    
    n_capped_bins = 1
    while True:
        N = bin_counts[argsorted_bins[n_capped_bins]] * n_capped_bins + bin_counts[argsorted_bins[n_capped_bins:]].sum()
        if N < target:
            break
        n_capped_bins += 1
    
    cap_amount = (target - bin_counts[argsorted_bins[n_capped_bins:]].sum()) // n_capped_bins
    
    bin_indices = np.digitize(lengths, bin_edges[:-1]) - 1
    bin_indices = np.clip(bin_indices, 0, len(bin_counts) - 1)
    
    keep_mask = np.ones(len(lengths), dtype=bool)
    
    for i in range(n_capped_bins):
        bin_idx = argsorted_bins[i]
        binned_pts = np.where(bin_indices == bin_idx)[0]
        
        if len(binned_pts) > cap_amount:
            keep_indices = np.random.choice(binned_pts, cap_amount, replace=False)
            remove_indices = np.setdiff1d(binned_pts, keep_indices)
            keep_mask[remove_indices] = False
    
    return [seqs[i] for i in range(len(seqs)) if keep_mask[i]]


new_seqs = flatten_distribution(seqs, lengths, keep_ratio=0.6)
new_lengths = [len(i) for i in new_seqs]


os.mkdir(new_folder)

# Write the sequences to txt files (6 at a time to match train?  Not really sure why they are grouped by 6 though)
for i in range(len(new_seqs)//6):
    with open(f"{new_folder}/{i}.txt", "w") as f:
        f.write("\n".join([" ".join(seq) for seq in new_seqs[i*6:(i+1)*6]]) + "\n")

