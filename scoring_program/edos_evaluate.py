#!/usr/bin/env python

# load required packages
import sys
import os
import pandas as pd
from sklearn.metrics import f1_score

sys.stdout.write("Starting scoring program. \n\n") # participants can read these messages in the stdout.txt and errors in the stderr.txt for their submission

# load input and output directories, which are passed as arguments as per the metadata file
input_dir = sys.argv[1]
output_dir = sys.argv[2]

# from the input directory, load the submission and gold standard data directories as specified by CodaLab 
submission_dir = os.path.join(input_dir, 'res')
gold_dir = os.path.join(input_dir, 'ref')

# validate submission and gold standard data directories
if not os.path.isdir(submission_dir):
    sys.exit("Submission directory doesn't exist")
if not os.path.isdir(gold_dir):
    sys.exit("Test data directory  doesn't exist")

# create output directory
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

sys.stdout.write("File directories are valid. \n")

# load submission
sys.stdout.write(str(os.listdir(submission_dir)))
sys.stdout.write("\n")
submission_df = pd.read_csv(os.path.join(submission_dir, os.listdir(submission_dir)[0])) # the first file in the submission zip is expected to be the submission csv
sys.stdout.write("Loaded submission. \n")

# load gold standard data
gold_df = pd.read_csv(os.path.join(gold_dir, os.listdir(gold_dir)[0])) # the first file in the gold standard zip is expected to be the gold standard csv
sys.stdout.write("Loaded gold standard data. \n\n")

# validate submission:
# correct columns exist
if "rewire_id" not in submission_df.columns:
    sys.exit('ERROR: Submission is missing Rewire ID column.')
if "label_pred" not in submission_df.columns:
    sys.exit('ERROR: Submission is missing label_pred column.')
# length matches gold standard data
if (len(submission_df) != len(gold_df)):
    sys.exit('ERROR: Number of entries in submission does not match number of entries in gold standard data. Are you submitting to the right task?')
# valid labels
unique_submission_labels = submission_df['label_pred'].unique()
unique_gold_labels = gold_df['label'].unique()
for i in unique_submission_labels:
    if i not in unique_gold_labels:
        sys.exit('ERROR: The column label_pred contains invalid label strings. Please see the Submission page for more information.')


sys.stdout.write("Submission contains correct column names (rewire_id and label_pred). \n")
sys.stdout.write("Number of entries in submission matches number of entries in gold standard data. \n")
sys.stdout.write("Predicted labels are all valid strings. \n\n")

# sort submission and gold standard data by Rewire ID, so that labels match predictions
submission_df = submission_df.sort_values("rewire_id")
gold_df = gold_df.sort_values("rewire_id")

sys.stdout.write("\nLabels in gold standard data:")
sys.stdout.write(str(sorted(pd.unique(gold_df.label))))
sys.stdout.write("\n\n")

sys.stdout.write("\nLabels in submission:")
sys.stdout.write(str(sorted(pd.unique(submission_df.label_pred))))
sys.stdout.write("\n\n")

# calculate macro F1 score for the submission relative to the gold standard data
if len(pd.unique(gold_df.label))>2:
    f1 = f1_score(y_true = gold_df["label"], y_pred = submission_df["label_pred"], average="macro")
elif len(pd.unique(gold_df.label))==2:
    f1 = f1_score(y_true = gold_df["label"], y_pred = submission_df["label_pred"], pos_label=None, average="macro")
    # need to set pos_label to none because of quirk in sklearn 0.17, which is the version running on CodaLab..
    # https://scikit-learn.org/0.17/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score

# write macro F1 score to a "scores.txt" file as required by CodaLab
with open(os.path.join(output_dir, 'scores.txt'), 'wb') as output_file:
    output_file.write("MacroF1: {}".format(f1))

sys.stdout.write("Submission evaluated successfully. \n")
sys.stdout.write("Macro F1:")
sys.stdout.write(str(f1))