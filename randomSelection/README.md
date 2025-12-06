This folder contains the files involving the data method of random selection. randomSelect.py selects a percentage within the train_prefix folder to be used for training the embedding model. This file can be run with the following command: 

python randomSelect.py 50

where the number after 'randomSelect.py,' in this case is 50, refers to the percentage of data that will randomly be selected from the input data folder.

minimizePairs.py selects a percentage within the TCREpitopePairs.csv to be used in training the prediction model. It selects a total of 7% of the data, keeping the 1 to 1 ratio of binding and nonbinding pairs. This ratio can be changed within the code itself. pairs7.csv is the result of running minimizePairs.py on TCREpitopePairs.csv.

The 'models' folders contains the .out files consisting of the 10 total iterations of model training (5 for epitope split and 5 for TCR split).
