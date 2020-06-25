
# Text Sentiment Analysis-Twitter (NLP)
Public opinion on Twitter about US airlines in 2015

Author: Mohammed Ba Salem 

Contact: basaleemm@gmail.com

LinkedIn: [https://www.linkedin.com/in/mohammed-basalem/](https://www.linkedin.com/in/mohammed-basalem/)

## Purpose
The objective of this project is to compute the sentiment of text information (Tweets) by answering the question **What can public opinion in Twitter tell us about US airlines service in 2015**. Doing so, an analytical insights  will be provided in order to help airlines adopt new business strategist by addressing aspects with low satisfactions. 
## Datasets
Two datasets are used for this project.  The generic_tweets.txt file contains tweets that have had their sentiments already analyzed and recorded as binary values 0 (negative) and 4 (positive). Each line is a single tweet, which may contain multiple sentences despite their brevity. This data aimed to be used as training data as classes are balanced. It has 200,000 rows and 6 columns.

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Sentiment_Analysis_US_Airlines_Tweets/images/Generic_Tweets_Classes.PNG)

The second data set, US_airline_tweets.txt, contains a list of tweets regarding several US airlines. This file is used as a testing data. It has 11,541 rows and 6 columns. 

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Sentiment_Analysis_US_Airlines_Tweets/images/US_Tweets_Classes.PNG)

## Approach
### Data Cleaning with Natural Language Toolkit (NLTK) & Regular Expression 
Data, as given, is not in a form amenable to analysis. A lot of noise exist, thus, a procedure designed to clean and parse data to transform it into a more readable and amenable, some steps are here: 

- Remove all html tags and attributes 
- Replace all html character codes with an ASCII equivalent
- Remove all URLs 
- Remove extra white spaces
- Remove punctuation marks and keeping only letters
- Convert letters into lowercase
- Remove Stop Words.
- If a tweet is empty after pre-processing, it should be preserved as such.

### Exploratory Data Analysis 
The simple procedure was designed to identify the airline of a given tweet and apply the procedure to all the tweets in the datasets. A a good approach was to look at words+hashtags in the tweets, and map it to an airline dictionary to obtain airline name. 

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Sentiment_Analysis_US_Airlines_Tweets/images/Negative_Reasons_Distribution.PNG)

- Public sentiments about US airlines are visualized in a form of bar chart to draw some conclusion on given services.
	- The distribution of negative tweets among the various reasons is not uniform, with majority of them being for **Customer Service Issue** , **Late Flight** and hardly for **Damaged Luggage**. 
	- Negative reviews for **Virgin America Airline** are more associated with *Customer Service Issue*, *Flight Booking Problems* and hardly for *Long lines*. 
	- Negative reviews for **United Airlines** are more associated with *Customer Service Issue*, *Late Flight*,*Lost Luggage* and hardly for *Damaged Luggage*. 
	- Negative reviews for **SouthWest Airlines** are more associated with *Customer Service Issue*, *Late Flight*,*Cancelled Flight* and hardly for *Damaged Luggage*. 
	- Negative reviews for **JetBlue Airways** are more associated with *Late Flight*, *Customer Service Issue*, *Bad Flight* and hardly for *Damaged Luggage*. 
	- Negative reviews for **US Airways** are more associated with *Customer Service Issue*, *Late Flight*,*Cancelled Flight* and hardly for *Damaged Luggage*. 
	- Negative reviews for **American Airways** are more associated with *Customer Service Issue*, *Late Flight*,*Cancelled Flight* and hardly for *Damaged Luggage*. 

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Sentiment_Analysis_US_Airlines_Tweets/images/Airlines_Negative_Tweets.PNG)

- A word cloud to visualize the collection of negative and positive words is generated: 

	![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Sentiment_Analsis/images/Positive_Word_Cloud.png)


	- From above US airlines positive word cloud, it can observed that the word like **"Southwest air",** and  **"jetblue"** have the highest frequency for positive tweets, along with it we can see words like *"best"*, *"amazing"*, *"good customer service"*, *"great",* *"love",* *"nice"*, and *"happy"* etc. 


	- From below US negative word cloud, it can observed that the word like **"americanairlines"**, **"unitedairline"**, **"usaairways"** are the biggest words appeared which indicates more negative responses associated with that airline tweets.However, **"virginamerica"** has the smallest word appeared relative to other airlines words, this indicates that public can expect **Vigine Airlines** as a good airline compared to others. Along with that, we can also see some negative words such as *"cancelled flight"*, *"delayed"*,*"help"*,*"canceled flight"*,*"booking problems"*, *"late flight"* and etc. 

	![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Sentiment_Analysis_US_Airlines_Tweets/images/Negative_Word_Cloud.png)


- From distribution of Tweets via Airline we can observe the following: 
	-  **United Airlines** has the highest number of negative tweets, **US Airways** and **American Airlines** takes second and third place in term of number of negative tweets. 
	- The other airlines **Virgin America, SouthWest and JetBlue** are having a low negative tweets, this could indicate that they provide a good services compared to **United Airlines, US Airways and American Airlines**, however, it is still needed to be improved. 
	- Regarding **Delta Assist**, as shown below, it has only two negative tweets and zero positive tweets. I would say that data given to us lack information about Delta Assist airline, therefore, no conclusion can be made, I might take it out from Modeling preparation step. 

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Sentiment_Analysis_US_Airlines_Tweets/images/Distribution_Tweets_per_Airlines.PNG)

### Model Preparation
Generic tweets are used for training and developing the model, thus, a random split of 70% for training data and 30% for test data is performed. This data is prepared for Naive Bayes Classifier **BernoulliNB** and **Logistic Regression** Classifier where each tweet is considered a single observation. In both classifiers, the output is a sentiment value of of 0 or 1 aka negative or positive . The features are tweets / reviews input as text data. 

The frequency of each work is used as extracted features for model (CounterVectorizer or TF-IDF). Alternatively, language modeling by using word n-grams as first step of tagging the word by its part of speech (POS), then use the frequency of each POS as the features of the model. 

### Model Implementation  
Two classifiers are trained on the generic tweets training data and applied on the test data to obtain the following accuracy values. 

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Sentiment_Analysis_US_Airlines_Tweets/images/Combined_Generic_Tweets_Model_Results.png)

- From above report for both models Bernoulli and LogRe, we can see that we have almost a balance F1 score, that means we have equal positive and negative in training data from Generic tweets and this is confirms from above plots of positive and negative for generic plots.73% accuracy for BN mode and 74% accuracy for LogR. LogR seems good so far for tweets by using a low level of NLP. 

The same models are later evaluated on the US airline data. To obtain the following accuracy values. 

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Sentiment_Analysis_US_Airlines_Tweets/images/USA_Tweets_Model_Results.png)

 - BernoulliNB model gives us an accuracy of 77.2%, while LogRe gives an accuracy of 74.7%..The F1 score of positive (0.52) and negative (0.85) is not balanced. That is because data provided to us is skewed into negative.
 
As Bernoulli Model gives us the highest accuracy score, we will use Bernoulli model to predict US airlines sentiments below. 

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Sentiment_Analysis_US_Airlines_Tweets/images/BN_US_Final.PNG)

Finally the negative reasons of US airlines data (70% training data and 30% test data) are used to train a multiclass logistic regression. The model is trained to predict negative reasons. In this data, there are 10 negative reasons as we have seen them above in the EDA.  

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Sentiment_Analysis_US_Airlines_Tweets/images/Negative_Reasons_Multi.PNG)

## Results 
From above EDA, we can see that people have experienced a lot of unsatisfied services during a flight. We count the different positive and negative tweets made by every US airlines. As per the predictions on the US negative reasons, **customer service issue** still has the highest negative reason. This is due to the fact that number of negative reasons is imbalance, and inclined towards Customer Service Issue category. The predicted percentage of each negative reasons category are as follow: Customer Service Issue 46.1%, Can't tell 17.2%, Late Flight 14.3%, Lost Luggage 6.8%, Cancelled Flight 5.2%, Flight Attendant Complaints 3.8%, Bad Flight 3.8%, Flight Booking Problems 2.5% and Longlines 0.19%. Therefore, as per the prediction, Customer Service has to be improved by airlines, they may train their employee to provide a more satisfied customer experience that meet their expectations. 

### Classification Report and Confusion Matrix 
Both metrics show a good prediction accuracy for US tweets model and negative reasons category model . The overall F1 score looks to be almost balance with precision and recall which means we truly in a better position.   
### Failure to Obtain Higher Accuracy for US Tweets
The precision score for BernoulliNB range from 46% to 89%, with total macro average of 67%. On the other hand, the recall score range from 60% to 82%, with total macro score 71%. The overall all accuracy is 77.4% Clearly we have a good classifier able to detect different tweets, but we can still observed some incorrectly predictions, and those can be attributed to following. 
- The model is trained on Generic Tweets Data and has not exposed to US Airlines Data, having industry specific keywords in corpus can enhance the accuracy. 
- A high level **Natural Language Processing Library Spacy** could do much better than NLTK to perform feature extraction. Spacy has a huge English dictionary and corpus for stop words, words contractions,  vocabulary and smart part of speech algorithms to capture overall sentiment meaning. Not to mention Lemmatization! 
- The distribution of positive and negative class category of tweets is not uniform, highly imbalance, there are more negative tweets than positive ones.  
### Failure to Predict Negative Tweets Correctly 
The precision score for multiclass logistic regression range from 0% to 74%, with total macro average of 52%. On the other hand, the recall score range from 0% to 77%, with total macro average of 43%. However, an overall accuracy of 61% is not acceptable and can be attributed to following issues. 
- Negative reasons category are not uniformly distributed, imbalance data! This result in some bias while predicting. This could be due to lack of data resulted from short time data collection! 
- The negative reasons are not classified or grouped for specific type of tweets. (I developed a model for negative tweets after grouping negative reasons for type of tweets and accuracy improved from 61% to 75%, last 2 cells of notebook). 

Please feel free to reach out for any discussion or feedback! 