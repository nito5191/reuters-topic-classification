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
Using 66 most common topics and the "lewissplit" training/test set split, a distilroberta-base model trained with simpletransformers gave this result after 1 epochs of training:

{'LRAP': 0.9184846620014195, 'eval_loss': 0.02149274017546297}
                 precision    recall  f1-score   support

            acq       0.81      0.90      0.86       719
           alum       0.00      0.00      0.00        23
         barley       0.00      0.00      0.00        14
            bop       0.00      0.00      0.00        30
        carcass       0.00      0.00      0.00        18
          cocoa       0.00      0.00      0.00        18
         coffee       0.00      0.00      0.00        28
         copper       0.00      0.00      0.00        18
           corn       0.00      0.00      0.00        56
         cotton       0.00      0.00      0.00        20
            cpi       0.00      0.00      0.00        28
          crude       0.79      0.78      0.78       189
            dlr       0.00      0.00      0.00        44
            dmk       0.00      0.00      0.00         4
           earn       0.67      0.98      0.80      1088
           fuel       0.00      0.00      0.00        10
            gas       0.00      0.00      0.00        17
            gnp       0.00      0.00      0.00        35
           gold       0.00      0.00      0.00        30
          grain       0.83      0.70      0.76       149
           heat       0.00      0.00      0.00         5
            hog       0.00      0.00      0.00         6
        housing       0.00      0.00      0.00         4
         income       0.00      0.00      0.00         7
       interest       0.00      0.00      0.00       133
            ipi       0.00      0.00      0.00        12
     iron-steel       0.00      0.00      0.00        14
           jobs       0.00      0.00      0.00        21
           lead       0.00      0.00      0.00        14
            lei       0.00      0.00      0.00         3
      livestock       0.00      0.00      0.00        24
         lumber       0.00      0.00      0.00         6
      meal-feed       0.00      0.00      0.00        19
       money-fx       0.70      0.50      0.58       180
   money-supply       0.00      0.00      0.00        34
        nat-gas       0.00      0.00      0.00        30
         nickel       0.00      0.00      0.00         1
            oat       0.00      0.00      0.00         6
        oilseed       0.00      0.00      0.00        47
         orange       0.00      0.00      0.00        11
       palm-oil       0.00      0.00      0.00        10
       pet-chem       0.00      0.00      0.00        12
       platinum       0.00      0.00      0.00         7
       rapeseed       0.00      0.00      0.00         9
       reserves       0.00      0.00      0.00        18
         retail       0.00      0.00      0.00         2
           rice       0.00      0.00      0.00        24
         rubber       0.00      0.00      0.00        12
           ship       0.75      0.03      0.06        89
         silver       0.00      0.00      0.00         8
        sorghum       0.00      0.00      0.00        10
       soy-meal       0.00      0.00      0.00        13
        soy-oil       0.00      0.00      0.00        11
        soybean       0.00      0.00      0.00        33
            stg       0.00      0.00      0.00         0
strategic-metal       0.00      0.00      0.00        11
          sugar       0.00      0.00      0.00        36
        sunseed       0.00      0.00      0.00         5
            tea       0.00      0.00      0.00         4
            tin       0.00      0.00      0.00        12
          trade       0.68      0.61      0.64       117
        veg-oil       0.00      0.00      0.00        37
          wheat       0.00      0.00      0.00        71
            wpi       0.00      0.00      0.00        10
            yen       0.00      0.00      0.00        14
           zinc       0.00      0.00      0.00        13

      micro avg       0.73      0.57      0.64      3703
      macro avg       0.08      0.07      0.07      3703
   weighted avg       0.50      0.57      0.52      3703
    samples avg       0.34      0.32      0.33      3703

## Possible improvements
Training for more epochs and using a developemnt data set for evaluation metric during training to stop training at the right time and prevent overfitting.
