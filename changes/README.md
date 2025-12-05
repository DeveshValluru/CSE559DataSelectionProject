For this project, a newer version of tensorflow was used. Due to this, there were changes that needed to be made in the initial files used for baseline catELMo training.
This folder contains the files that required edits to be made, namely training.py and train_elmo.py

For training.py, the following changes had to be made:
- disable eager execution
- change '+=' syntax to assign_add in a specific line

For train_elmo.py, the following changes had to be made:
- change the epochs ran from 10 to 1 (due to time constraints)
- change n_train_tokens to match the percentage of data used in training 
