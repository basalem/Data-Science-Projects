
# Detecting Credit Card Fraudulent Transaction 
Author: Mohammed Ba Salem 

Contact: basaleemm@gmail.com

LinkedIn: [https://www.linkedin.com/in/mohammed-basalem/](https://www.linkedin.com/in/mohammed-basalem/)

## Purpose 
The purpose of this project is to build a classification machine learning model able to classify highly unbalance subset of credit card data into a normal or fraud transaction.  

## Dataset 
The dataset contains records for transactions made by European cardholders in September 2013. The history for those transactions goes back for two days records where we have 492 frauds out of 284,807 transactions. The fraud class accounts for 0.17% of all transactions, highly unbalanced! 


![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Credit_Card_Fraud_Detection/Images/Class_Distribution.PNG) 


Here are some information about dataset: 
- All inputs are in form of numerical values. 
- Input features have been transformed as principle components for the purpose of preserving confidentiality of transaction information. Only the Amount (in USD) and Time (in seconds, time elapsed between each transaction) have not been transformed. 
- The column class contains response of every transaction where 0 indicates normal transaction and 1 indicates fraud one. 

## Libraries 
**Python Version**: 3.7.6

**Packages**:  pandas, numpy, sklearn, imblearn, re, matplotlib, seaborn.
 
## Methodology 
### Data Cleaning 
No data pre-processing or cleaning is needed here, data as given clean, transformed and no missing values! 
### Exploratory Data Analysis 
#### Amount of Transactions 
- The normal transactions have a mean of 88.3, maximum of 25,691.16 and minimum of 0. 
- The fraud transactions have a mean of 122.2, maximum of 2,125.87 and minimum of 0. 
- The majority of normal transaction amounts are between $0 and $4,000. 

		
	![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Credit_Card_Fraud_Detection/Images/Normal_Distribtion.PNG)


- The majority of fraud transaction amounts are between $0 and $200. Based on my knowledge, I can explain this as current existed ML model classify ''Tap or Contactless" transaction that exceeds allowed amount (specified by the bank) as **Fraud**. However, I can not make a solid conclusion or feature engineering based on this insight for the following reasons: 
		- Limited amount of contactless transaction are not declared in the data. 
		- Amount of allowed contactless transactions vary from bank to bank and it is more of country based. 
		- The credit card data is not for a single user! It is for multiple people so I can't create any features that 			represent the trend in the transactions. 
		- Interestingly, majority of fraud transactions are lower than $10, in fact, most of the transactions are between **$0 and $1**. This indicates **[One Dollar Scam!](https://www.creditcards.com/credit-card-news/1-dollar-credit-card-scam-1282/)**


	![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Credit_Card_Fraud_Detection/Images/Fraud_Distribution.PNG)	



- Both type of transactions are positively skewed (tail pulls mean to right of median). 

#### Time for Transactions  
- The first day cycle begins at 0 seconds and ends at 86,400 seconds. 
- The second day cycle begins at 86,401 seconds and ends at 172,800 seconds. 
- Time elapsed for normal transaction has a consistent trend over the 2 days. It has a peak around 11:00 am till 7:00 pm. In other words, high density can be observed during working hours, and a fall at beginning and end of the day. 
- The density of time elapsed for fraud transactions is almost high for all intervals during 2 days. In other words, they are active all the time!

	![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Credit_Card_Fraud_Detection/Images/Transaction_Time.PNG)


#### Correlation and Feature Importance
- The amount shows as an important feature and time is not. Thus, I will remove the Time column from input features list during training the model. 

- Unfortunately, we can't do any feature importance or selection due to the fact that all provided features were transformed by PCA, and features are invariant to scale.  

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Credit_Card_Fraud_Detection/Images/All_Correlation.PNG)


![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Credit_Card_Fraud_Detection/Images/Fraud_Correlation.PNG)

### Model Implementation 
 2 different classification algorithms are implemented. Algorithms used are *Logistic Regression* and *RandomForest Classifier* . As the data is highly imbalance, it is necessary to select proper metrics that can return a meaningful accuracy for unbalance classification. Recall, Precision (Confusion Matrix) and Area under Precision-Recall Curve (AUPRC) are select to determine best classifier. 

To make this implementation more interesting, I aim to evaluate models performance at 4 different situations: 

- Classification on Original Data.

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Credit_Card_Fraud_Detection/Images/Experiment1.png)

- Classification with Under-Sampling Majority.

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Credit_Card_Fraud_Detection/Images/Experiment2.png)

- Classification with Over-Sampling (SMOTE) Data Minority.

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Credit_Card_Fraud_Detection/Images/Experiment3.png)

- Classification with Combination of Over-Sampling & Under-Sampling. 


![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Credit_Card_Fraud_Detection/Images/Experiment4.png)

From above metrics, it is clearly seen that both *Ridge* and *Lasso* outperform other models. A next step is to perform hyperparameter  tuning on 4 models.   
### Results 
 After analyzing above metrics and evaluations, Random Forest Classifier with combination of oversampling and under-sampling gives outstanding results. The model provides a balance trade-off in **AUPRC accuracy 83.2%**, **F1-score 87%**, **AUC accuracy of 91.4%**, **precision of 91%**, **recall of 83%**. A high precision score indicates a trusted model, and a high recall indicates a good classifier, and both achieved here! This model trained only on 50% of the overall data, it can get much higher score if it trained on full dataset.   

The model captures **82.75%** of fraud transactions, and incorrectly classified **17.25%** as non-fraudulent transaction. If I would assume that fraudulent transactions cost a bank **$100 million**, above model will save **$82.75 million**. In addition, the model has less False Positive cases, **0.015%** of total  genuine normal transactions are incorrectly classified as fraud. This indicates that only few transactions will be blocked while majority of transactions will be approved smoothly! 

Please feel free to reach out for any discussion or feedback! 