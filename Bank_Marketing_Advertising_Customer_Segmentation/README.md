
# Bank Marketing Advertising Customer Segmentation
Author: Mohammed Ba Salem 

Contact: basaleemm@gmail.com

LinkedIN: [https://www.linkedin.com/in/mohammed-basalem/](https://www.linkedin.com/in/mohammed-basalem/)

# Business Problem
A marketing team at one of New York City Banks wants to launch a targeted ad marketing campaign by segmenting customers into potential groups based on given features in the data. In this project, I will leverage both data science and machine learning tools to perform market segmentation to assist marketing department with understanding customers' spending habits to develop customer oriented marketing strategies. 

# Dataset-Background 
The dataset contains records for credit card purchases transactions for NYC bank's customers. The history for those purchases records goes back for 6 months. The data contains 18 columns and 8950 rows where are all entries are numerical types except CUSTID which is in string format. 


* CUSTID: Customer Identification of Credit Card holder
* BALANCE: Amount left in customer's account to make purchase. 
* BALANCE_FREQUENCY: How frequently the Balance is updated,score between 0 & 1 (1=frequently updated, 0=not frequently updated)
* PURCHASES: Amount of purchases made from account
* ONEOFFPURCHASES: Maximum purchase amount done in one-go
* INSTALLMENTS_PURCHASES: Amount of purchase done in installment
* CASH_ADVANCE: Cash in advance given by the user
* PURCHASES_FREQUENCY: How frequently the Purchases are being made,score between 0 & 1 (1=frequently purchased, 
0=not frequently purchased)
* CASH_ADVANCE_TRX: Number of Transactions made with "Cash in Advance"
* PURCHASES_TRX: Number of purchase transactions made
* CREDIT_LIMIT: Limit of Credit Card for user
* PAYMENTS: Amount of Payment done by user
* MINIMUM_PAYMENTS: Minimum amount of payments made by user  
* PRC_FULL_PAYMENT: Percent of full payment paid by user
* TENURE: Tenure of credit card service for user

# Libraries 
**Python Version**: 3.7.6

**Jupyter Notebook**: 6.0.3

**Packages**:  pandas, numpy, datetime, sklearn, matplotlib, seaborn, PCA, AutoEncoder, KMeans, Keras. 
 
# Exploratory Data Analysis 
 As it is always important to understand data and its quality, EDA takes care of that. But, it helps us to understand customers spending habits to identify potential groups. For that, some pre-processing is needed to validate quality of data: 
 1. Check missing values and imputation if needed. 
 2. Check duplicates. 
 3. Data Distribution Plots. 
 4. Pearson Correlation Heat Map. 

# Customer Segmentation Methodology 
 Customer segmentation is a subdivision of marketing analytics that discrete customer groups that share similar characteristics. It helps companies to develop uniquely appealing products and services. 

Since the business problem focuses on developing marketing strategies on targeted ads through understanding customers spending habits, the best ML model to address the following problem is K-Means. 

**K-Means:** 
It is an unsupervised machine learning algorithm that works by grouping observations with similar attribute values together by measuring Euclidean distance between points. The model iteratively update centroid of Euclidean distance by minimize objective function. The objective function used here is the Within Cluster Sum of Squares (WCSS) while varying number of clusters (K).

**Methodology:**

Two ML approaches will be used here to obtained the most optimal number of clusters, "The Elbow Method". Elbow Method calculates WCSS for different values of K, and choose the K for which WCSS first starts to diminish. 

The two methods blind in two different dimensional reduction techniques to reduce sparsity in the features such that model can cluster observation perfectly.   

1. PCA & KMeans Clustering
2. AutoEncoder & KMeans Clustering

**Note:** 
Since data contains different numerical values, it is best to change values to a common scale without distorting differences in ranges of values by normalization.

## PCA-KMeans Cluster Approach
In this approach, we use PCA to reduce dimensions to find optimal number of components which capture the greatest amount of variance in the data. After that, we use K-means clustering algorithm to determine number of customer groups in the data. Finally, a 2D PCA plot will be used to visualize clusters in the data. In a nutshell, the following steps will be applied: 

1. Dimensionality Reduction with PCA. 

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Bank_Marketing_Advertising_Customer_Segmentation/Images/PCA.png) 

2. K-Means clustering by using PCA components. 

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Bank_Marketing_Advertising_Customer_Segmentation/Images/PCAKMeans_NumClusters.PNG)

3. 2D PCA plot to visualize clusters. 

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Bank_Marketing_Advertising_Customer_Segmentation/Images/PCA&KMeans_Cluster.PNG) 


## Auto Encoders -KMeans Clustering Approach 
In this approach, we apply dimensionality reduction technique using Deep Learning approach. AutoEncoders are type of Artificial Neural Network that are used to perform a task of data encoding aka representation learning. It consists of 3 essential layers named **Encoder, Bottleneck and Decoder**. AutoEncoder basically encodes input data then learns how to reconstruct the data back from reduced encoded representation by ignoring the noise in the data.  

After reconstructing original data in less shape (Reduce Dimensions), we will use reduced data to perform KMeans clustering. Finally, we will do 2D PCA plot to visualize different clusters. In a nutshell, the following steps will be performed: 

1. Dimensionality reduction with AutoEncoders (Reconstruct original data without noise, less dimensions). 

2. K-Means clustering by using Reconstructed data from AutoEncoder. 

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Bank_Marketing_Advertising_Customer_Segmentation/Images/AutoEncoderKMeans_NumClusters.PNG)

3. 2D PCA plot to visualize clusters. 

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Bank_Marketing_Advertising_Customer_Segmentation/Images/AutoEncoder&KMeans_Cluster.PNG)

# Comparing Results
The purpose of this section is to explorer characteristic of each cluster obtained from the above 2 techniques. In addition, comparing similar clusters characteristics from PCA and AutoEncoders. Doing so, it will help us understand dimensionality reduction quality and its impact on KMeans algorithm.

**Note:** A detailed comparison is avilable inside attached Jupiter Notebook

**Summary Heat Map**

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Bank_Marketing_Advertising_Customer_Segmentation/Images/Clusters_Summary.PNG)

# Conclusion

As the business objective aims to perform customer segmentation to help marketing team launch a targeted ads marketing campaign by segmenting customers into potential groups, it is important to point out that both above algorithm techniques achieved a high level of dimensionality reduction and clustering performance. I would not recommend one approach over the second as both models give similar results. However, I would give my insights based on clusters characteristics based on above summary heat map. 


**Group 1:** 
The following group (class 2 in PCA) and (class 1 in AutoEncoder) has the following characteristics: 
1. It has the lowest balance amount left in the account compared to other 2 clusters. 
2. It has the middle amount of purchases made, the middle purchases frequency and the middle number of purchase transactions made. 
3. It has the middle maximum purchase done in one-go. 
4. It has the lowest cash in advance given by the user as well as the lowest number of transactions made with cash in advance. 
5. It has the middle amount of purchase done in installment. 
6. It has the lowest limit of credit card for user.
7. It has the lowest amount of payment done by user.
8. It has the middle percent of full payment paid by user. 

**Group 2:** 
The following group (class 1 in PCA) and (class 0 in AutoEncoder) has the following characteristics: 
1. It has the middle balance amount left in the account. 
2. It has the lowest amount of purchases made, the lowest purchases frequency and the lowest number of purchase transactions made. 
3. It has the lowest maximum purchase done in one-go. 
4. It has the highest cash in advance given by the user as well as the highest number of transactions made with cash in advance. 
5. It has the lowest amount of purchase done in installment. 
6. It has the middle limit of credit card for user.
7. It has the middle amount of payment done by user.
8. It has the lowest percent of full payment paid by user. 

**Group 3:** 
The following group (class 0 in PCA) and (class 2 in AutoEncoder) has the following characteristics: 
1. It has the highest balance amount left in the account. 
2. It has the highest amount of purchases made, the highest purchases frequency and the highest number of purchase transactions made. 
3. It has the highest maximum purchase done in one-go. 
4. It has the middle cash in advance given by the user as well as the middle number of transactions made with cash in advance. 
5. It has the highest amount of purchase done in installment. 
6. It has the highest limit of credit card for user.
7. It has the highest amount of payment done by user.
8. It has the highest percent of full payment paid by user. 

# Business Recommendation

I would recommend to target Group 3 population as those ones are having highest overall purchase records, they have a lot of cash (Installment purchases lowest) and has the highest percent (rate) of full payment paid by users compared to other 2 groups. 

For Group 1 & 2, I would say the almost follow same spending habits, only minor differences. However, Group 2 has the highest CASH in ADVANCE or short term load from credit card, therefore, if bank want to benefit from interest rate from money withdraw (As far as I recall, loan interest rate from credit card in NYC is between 19.99% - 24%), then target those group with purchase ads than Group 1. 

Eventually, it is matter of trad off for bank. Does bank want cash money or loan interest rate.More details are left for the marketing department team!  

**If you read this summary and you would like to discuss further opportunities, please do not hesitate to reach out (my contact is at top of page)** 

