# reuters-topic-classification
## Preprocess data
The preprocessing code requires python 2.7 so create a specific enviroment for that:

conda create -n reuters-topic-classification-preprocess python=2.7 --no-default-packages
conda activate reuters-topic-classification-preprocess
cd preprocess
pip install requirements.txt
python preprocess.py

This should download and write the dataset to a file readable easily by python 3 (dataset/dataset.pkl)

## Running notebook
Upload dataset/dataset.pkl and topic-classification.ipynb file to your Google Drive
Open notebook in Google Colab
Select GPU runtime
Run the cells under "Install dependencies" and then restart runtime
Upload the dataset to the colab notebook (see comments)
Run the rest of the cells

## Results
Using 66 most common topics and the "lewissplit" training/test set split, a _ model gave this result after _ epoch of training:
