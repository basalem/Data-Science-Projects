
# 2018 Kaggle ML & DS Salary Prediction
Author: Mohammed Ba Salem 

Contact: basaleemm@gmail.com

LinkedIN: [https://www.linkedin.com/in/mohammed-basalem/](https://www.linkedin.com/in/mohammed-basalem/)

## Purpose 
The purpose of this challenge was to *tell a data story about a subset of the data science community represented in this survey, through a combination of both narrative text and data exploration.* 

## Datasets 
The data, as given is in a form of survey which originally contains 15430 rows and 397 columns. Those columns are in a form of questions. In addition, some questions contain multiple choice questions separated in different columns. To preserve the respondent privacy, Kaggle team modified the data and a lot of text has been shuffled. The format of data is combination of numeric and categorical one! 

Here are some important features or labelled columns: 
**Duration**: Time taken to complete survey
**Q1**: Gender
**Q2**: Age Class 
**Q3**: Country
**Q4**: Highest Level of Education 
**Q5**: Undergraduate Major 
**Q6**: Role Title (Job Title)
**Q7**: Industry 
**Q8**: Years of Work Experience 
**Q9**: Annual Salary (**Target Variable**)
## Libraries 
**Python Version**: 3.7.6
**Packages**:  pandas, numpy, sklearn,re, matplotlib, seaborn, worldcloud. 
## Methodology 
### Data Cleaning 
Survey data has to be organized into a more structured look and amenable. This process involves the following:  
- Explore data and delete unnecessary columns. 
- Filling missing values with appropriate reasonable values. 
- Convert categorical data into numerical for the ML to work effectively while predicting values. 
### Exploratory Data Analysis 
- Top 10 Countries in Kaggle Community of Data Science. 
	![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Side%20Projects/2018_Kaggle_Survey/images/Top_10Countries.png) 
	
- Top 10 Countries for Average Annual Compensation in Kaggle Community of Data Science. 
	![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Side%20Projects/2018_Kaggle_Survey/images/Top10_Salary.png)
	
- Kaggle Community Continent Distribution. 

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Side%20Projects/2018_Kaggle_Survey/images/Continent.PNG)
	
- Level of Education vs Average Annual Compensation in Kaggle Community of Data Science. 
	![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Side%20Projects/2018_Kaggle_Survey/images/Education.png)
- Age Class vs Average Annual Compensation in Kaggle Community of Data Science. 
	![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Side%20Projects/2018_Kaggle_Survey/images/Age.png)

### Feature Importance & Selection 
To explore the feature importance, a regression technique (Ridge Regression Model) used to obtain regression coefficients. The inputs are all 607 columns and target variable is annual salary (**Q9**). 

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Side%20Projects/2018_Kaggle_Survey/images/Top_Features.PNG)

As less important features usually result in instability in estimating the coefficient of regression model, a feature selection performed to reduce computation time and to give good predictive results. **R-square** score is used as **measurement metrics**. 200 out of 607 features are selected to do model implementation.  

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Side%20Projects/2018_Kaggle_Survey/images/Feature_Selection.PNG)

### Model Implementation 
 4 different regression algorithms (baselines) with 10 fold cross validation are implemented. Algorithms used are *Lasso Regressor*, *Ridge Regressor*, *RandomForest Regressor* and *DecisionTree Regressor*.  The following statistical metrics are used: 
 - Mean of R-square value for training and validation data. 
 - Std of R-square value for training and validation data. 
 - R-square value for 10 different folds for training and validation. 

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Side%20Projects/2018_Kaggle_Survey/images/Mean_Std_Val_R2.png)

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Side%20Projects/2018_Kaggle_Survey/images/Learning_Curve.PNG)

From above metrics, it is clearly seen that both *Ridge* and *Lasso* outperform other models. A next step is to perform hyperparameter  tuning on 4 models.   
 
 ### Hyperparameter Tuning & Model Performance
 Hyperparameter tuning will improve the generalization characteristics of algorithm by tuning its parameters! GridSearchCV used to iterate through a set of algorithm parameter. After tuning, the following results obtained.  

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Side%20Projects/2018_Kaggle_Survey/images/Hypertune_Results.PNG)


![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Side%20Projects/2018_Kaggle_Survey/images/HyperTuning_Learning_Curve.PNG)

- The R-square values for all models have gone up after tuning whereas RMSE errors have decreased.  
- R-square for Ridge mode is 0.474 while R-square value for Lasso is 0.474. 
- Ridge is the best candidate here for testing and deployment.  

### Model Testing & Evaluation 
#### How does your model perform on the testing set and training sets? 
![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Side%20Projects/2018_Kaggle_Survey/images/optimal_model.PNG)

- On the training sets the model perform better in terms R2 and RMSE. It has a high value for R2 and lower value for RMSE. 

 - On the testing sets the model perform relatively not good as it has lower R2 value and higher RMSE. 
- The model will overfit the data as training score is greater than testing score. But it will not experience a lot of overfitting as difference between both score is very small. We can also confirm this from residual plot below. 

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Side%20Projects/2018_Kaggle_Survey/images/Ridge_Residuals.PNG)

Please feel free to reach out for any discussion or feedback! 