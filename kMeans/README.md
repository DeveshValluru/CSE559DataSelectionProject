This folder contains the python files used to select a percentage of data using k-means clustering. There are two files in this folder.
The first file is testK.py. This file runs k-means on different k values and plots the resulting clusters. This is to determine the best k
value to cluster the training data. The second is file is minimizeParallel.py. This runs k-means on the optimal k value, plots the clusters,
and selects a percentage of data (based on clustering assignment) to minimize the dataset. To run these files, the paths must be updated to
the local directories and run with the following commands. The percentage of data selected can also be changed within the files.

python testK.py

python minimizeParallel.py
