# EMOD_finalproject

Classification Result:

Model: Linear SVM

0 means decrease, 1 means increase

[cur + pre day content scores]

1.
Source: yahoo.com

Score type: content_scores

                precision    recall  f1-score   support
          0       0.50      0.22      0.31         9
          1       0.36      0.67      0.47         6
    avg / total   0.45      0.40      0.37        15
Accuracy Score: 0.4

2.
Source: businessinsider.com

Score type: content_scores

             precision    recall  f1-score   support
          0       0.50      0.43      0.46         7
          1       0.43      0.50      0.46         6
    avg / total   0.47      0.46      0.46        13
Accuracy Score: 0.46153846153846156

3.
Source: marketwatch.com

Score type: content_scores

             precision    recall  f1-score   support
          0       0.00      0.00      0.00        11
          1       0.39      1.00      0.56         7
    avg / total   0.15      0.39      0.22        18
Accuracy Score: 0.3888888888888889

[title_score + firstP_score + content_score as 3 features ]

1.
Source: yahoo.com

Score type: content_scores

             precision    recall  f1-score   support
          0       1.00      0.11      0.20         9
          1       0.56      1.00      0.71        10
    avg / total   0.77      0.58      0.47        19
Accuracy Score: 0.5789473684210527

2.
Source: businessinsider.com

Score type: content_scores

             precision    recall  f1-score   support
          0       0.33      0.22      0.27         9
          1       0.36      0.50      0.42         8
    avg / total   0.35      0.35      0.34        17
Accuracy Score: 0.35294117647058826

3.
Source: marketwatch.com

Score type: content_scores

             precision    recall  f1-score   support
          0       0.00      0.00      0.00        11
          1       0.45      0.82      0.58        11
    avg / total   0.23      0.41      0.29        22
Accuracy Score: 0.4090909090909091

[Use all data to predict 4/11- 4/18 stock prices from all 4 companies]

Features: title_score+ firstP_score + content_score, all the scores come from averaging across all news sources.


                precision    recall  f1-score   support
          0       0.50      0.08      0.14        12
          1       0.50      0.92      0.65        12
    avg / total   0.50      0.50      0.39        24
Accuracy Score: 0.5