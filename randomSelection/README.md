This folder contains the code to randomly select a percentage of data points within the train_prefix folder.
Random selection is used as the baseline results to compare and see if other data selection methods perform
better in the downstream prediction task.


Changes will need to be made in randomSelect.py to ensure that the input paths and output paths match local directories. After making those changes, randomSelect.py can be run with the following command:

python randomSelect.py 50

where the number after 'randomSelect.py,' in this case is 50, refers to the percentage of data that will randomly be selected from the input data folder.
