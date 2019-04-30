# EMOD_finalproject

/All Data:
  1. Origin Data: origin news article data from Google News API
  2. Data_sentiment: data with sentiment score in it.
  3. Prediction: test data from Apr 11 to Apr 26.
  4. Stock Data: stock price data from four companies.
  5. process_result: processed csv files which are used to calculate correlation coefficient and to build prediction models.
/Code:
  1. classification.py: train classification models over all domains.
  2. correlation.py: calculate correlation coefficient and train classification models over separate news sources.
  3. dataprocessing1.ipynb: aggregate news sentiment with stock price data in the same csv file.
  4. dataprocessing2.ipynb: aggregate three types of text corpus with all three domains into one csv file.
  5. getGraphCSV.py: process data for data visualization.
  6. labelStock.py: label the stock price data with label 0 and 1.
  7. sentimentality.py: parse all the urls we get from google news API and calculate sentiment score for each article.
/graphs: All visualizations we created in Tableau 

Classification:Regression Results.pdf: records of all results of regression and classification models.
correlation.xlsx: The correlation coefficient of news sentiment and stock prices from different features.