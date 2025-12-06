import pandas as pd

# Load full dataset
dat = pd.read_csv('/home/pnluong/catELMo/TCREpitopePairs.csv')

# Separate the two classes
bind1 = dat[dat['binding'] == 1]
bind0 = dat[dat['binding'] == 0]

# Sample 3.5% from each group
sample1 = bind1.sample(frac=0.035, random_state=42)
sample0 = bind0.sample(frac=0.035, random_state=42)

# Combine into one dataframe (7% total)
pairs10 = pd.concat([sample1, sample0], axis=0)

# Shuffle (optional but recommended)
pairs10 = pairs10.sample(frac=1, random_state=42).reset_index(drop=True)

# Save to CSV
pairs10.to_csv('pairs7.csv', index=False)

print("Saved 7% dataset to pairs7.csv")
