
# Sales Forecasting: Products of 1115 Stores
Author: Mohammed Ba Salem 

Contact: basaleemm@gmail.com

LinkedIN: [https://www.linkedin.com/in/mohammed-basalem/](https://www.linkedin.com/in/mohammed-basalem/)

# Business Problem
Sales department wants to develop a  sales & promotion plan to increase their daily sales and skyrocket their growth. The department wants to use historical data for past years sales to predict future daily sales using ML Facebook prophet model which it lays out the tactics the sales department will use to achieve their goals! 

In this project, we attempt to forecast future sales based on 2.5 years historical records for 1115 stores while taking into account seasonality effects, demands, holidays.  

# Dataset-Background 

The datasets contains sales information for 1115 stores from 2013 to 2015.The data is given in two separate files. The first file contains 9 columns and 1,017,209 rows while second file contains information about store type, competition and promotions. 

**First file:**

* Store: unique store id 
* DayOfWeek: 7 for Sunday and 1 for Monday
* Date
* Sales: sales per day
* Customers: number of customers per day
* Open: 1 = store is open on that day, and 0 = close. 
* Promo: describes if store is running a promo on that day or not. 
* StateHoliday: indicates which state holiday (a = public holiday, b = Easter holiday, c = Christmas, 0 = None)
* SchoolHoliday: indicates if the (Store, Data) was affected by the closure of public schools. 


**Second file:** 

* Store: unique store id will be later used to merge 2 data.             
* StoreType: categorical variable to indicate type of store (a,b,c,d), not clearly defined by data owner.   
* Assortment: describes an assortment level: a = basic, b = extra, c = extended
* CompetitionDistance (meters): distance to closet competitor store.        
* CompetitionOpenSinceMonth: provides an estimate of the date when competition was open month.  
* CompetitionOpenSinceYear: rovides an estimate of the date when competition was open year.   
* Promo2: Promo2 is a continuing and consecutive promotion for some store (0 = store is not participating, 1 store is participating)     
* Promo2SinceWeek: date when store started participating in Promo2 since a week.
* Promo2SinceYear: date when store started participating in Promo2 since a year.         
* PromoInterval: describes the consecutive intervals Promo2 is started, naming the months the promotion is started new. 

# Libraries 
**Python Version**: 3.7.6

**Jupyter Notebook**: 6.0.3

**Packages**:  pandas, numpy, matplotlib, seaborn, fbprophet (Facebook prophet model)
 
# Exploratory Data Analysis 
 As it is always important to understand data and its quality, EDA takes care of that. But, it helps us to understand sales behavior . For that, some pre-processing is needed to validate quality of data: 
 1. Explorer data type and its feature.
 2. Check missing values and imputation if needed. 
 3. Check duplicates. 
 4. Data Statistics. 
 5. Data Visualization. 

## Data Insights: 
* Highest sales took place around December, you guess it! Clearly due to Black Friday and Christmas. Similarly, average number of customers visiting stores peaked around December too! 

 ![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Sales_Forecasting_Products_of_1115_Stores/Images/Average_Monthly_Performance.png)

* Highest sales usually took place around Sunday while lowest sales took place in Saturday. 

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Sales_Forecasting_Products_of_1115_Stores/Images/Average_Daily_Performance.png)

* The highest sales took place on the 30th and 1st of the month. A middle peak can be observed in the middle of month (17th of month). This trend is normal due to fact that most of customers got their pay check biweekly and they got to spend some money on themselves! 

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Sales_Forecasting_Products_of_1115_Stores/Images/Average_DayofMonth_Performance.png)

* Days where there is a running promotion, stores' sales increase while days where no promotion is running has low sales relatively. 

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Sales_Forecasting_Products_of_1115_Stores/Images/Promotion_Effect.PNG)

# Model Selection: Facebook Prophet

The purpose of selecting fbprophet model is due to the fact that our data has a lot of non-linear trends which are more likely not be captured by some ML models due to model assumptions. On the other hand, Fbprophet can take care of  non-linear trends by using an additive model to fit seasonality (Yearly, Monthly, Weekly, Daily and Holidays) effect which are more likely resulted from new products launched or logging changes. 

A fully generic defined function is developed to forecast sales for different stores at different future time frame. In other words, user has only to provide full data, store id number, future time frame to forecast and dates of holidays. The function will return a plot of predicted sales, trends of sales, holidays affect, weekly trends and monthly trends. 

These outcomes help department to outline the goals, objectives, strategies, revenue target and team structure. In a nutshell, it lays out the tactics the sales department will use to achieve their goals! 

For the purpose of demonstration results, I performed sales forecasting for 30 days for store number 15. 

![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Sales_Forecasting_Products_of_1115_Stores/Images/Forecasting_Trend1.PNG)


![alt text](https://github.com/basalem/Data-Science-Projects/blob/master/Sales_Forecasting_Products_of_1115_Stores/Images/Forecasting_Trend2.PNG)
   
**Observations:**
1. Sales for store 15 are going up.
2. Trends in day of the week show that most of the sales happended around Monday time frame. 
3. Trends in monthly sales show that most of the sales took place around December (Black Friday and Chrismas). There are some small peaks around April, May and August. 
4. There are some spikes on sales due to holidays around June, August, and December.  

**If you read this summary and you would like to discuss further opportunities, please do not hesitate to reach out (my contact is at top of page)** 

