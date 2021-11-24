# House Rocket Real Estate Insights
[Insights Project] The repository contains codes for the porfolio analysis at a fictitious real estate company.<br>

![House_Rocket](https://github.com/fabianaba/Real_Estate_Insights/blob/master/images/houserocket.png)


## Real Estate Insights:
The objetives of this project are:
* Perform exploratory data analysis on properties available on dataset.
* Determine which properties should be bougth according to business criteria.
* Develop an online [dashboard](https://analytics-house-rocket-sales.herokuapp.com/) that can be acessed by the CEO from a cell phone or computer.
<br>

## 1. Business Problem
House Rocket business model consists of purchasing and reselling properties through a digital platform. The data scientist is in charge to develop an online dashboard so the company's CEO can have an overview of properties available to become part of House Rocket portfolio in King County (USA).

<br>The [dashboard](https://analytics-house-rocket-sales.herokuapp.com/) must contain:
   * A table view with attributes filters
   * A map view with properties available
   * Which properties the company should buy
   * Expected profit of each property
<br>

## 2. Business Results
Based on business criteria, from 21,436 available properties, 10,707 should be bought by House Rocket and could result on a US$1,193,412,640.20 profit. <br>
Maximum Value Invested: US$4,094,212,008.00<br>
Maximum Value Returned: US$5,287,624,648.20<br>
Maximum Expected Profit: US$1,193,412,640.20<br>

Revenue forecast: 29.14% gross revenue
<br><br>

## 3. Business Assumptions
* The data available is from May 2014 to May 2015.
* Seasons of the year:<br>
   * Spring starts on March 21st<br>
   * Summer starts on June 21st<br>
   * Fall starts on September 23rd<br>
   * Winter starts on December 21d<br>
  
* Original dataset variables description:<br>

Variable | Definition
------------ | -------------
|id | Unique ID for each property available|
|date | Date that the property was available|
|price | Sale price of each property |
|bedrooms | Number of bedrooms|
|bathrooms | Number of bathrooms, where .5 accounts for a room with a toilet but no shower, and .75 or ¾ bath is a bathroom that contains one sink, one toilet and either a shower or a bath.|
|sqft_living | Square footage of the apartments interior living space|
|sqft_lot | Square footage of the land space|
|floors | Number of floors|
|waterfront | A dummy variable for whether the apartment was overlooking the waterfront or not|
|view | An index from 0 to 4 of how good the view of the property was|
|condition | An index from 1 to 5 on the condition of the apartment|
|grade | An index from 1 to 13, where 1-3 falls short of building construction and design, 7 has an average level of construction and design, and 11-13 have a high quality level of construction and design.|
|sqft_above | The square footage of the interior housing space that is above ground level|
|sqft_basement | The square footage of the interior housing space that is below ground level|
|yr_built | The year the property was initially built|
|yr_renovated | The year of the property’s last renovation|
|zipcode | What zipcode area the property is in|
|lat | Lattitude|
|long | Longitude|
|sqft_living15 | The square footage of interior housing living space for the nearest 15 neighbors|
|sqft_lot15 | The square footage of the land lots of the nearest 15 neighbors|

* Variables created during the project development:

Variable | Definition
------------ | -------------
| decision | wether a property should be bought |
| median_price_zipcode | median price of zipcode region |
| selling_price_suggestion | 30% more on buying price, if property should be bought |
| expected_profit | difference between buying price and selling price suggestion  |
| season | season property became available |

* Business criteria to determine wether a property should be bought are:
   * Property must have a 'condition' equals or bigger than 3.
   * Property price must be below or equal the median price on the region (zipcode)
<br>

## 4. Solution Strategy
1. Understanding the business model
2. Understanding the business problem
3. Collecting the data
4. Data Description
5. Data Filtering
6. Feature Engineering
8. Exploratory Data Analysis
9. Insights Conclusion
10. Dashboard deploy on [Heroku](https://analytics-house-rocket-sales.herokuapp.com/)
<br>

## 5. Top 4 Data Insights
1. After the 80s, number of properties built with basements decreased
2. Almost 60% of the properties became available during summer/spring.
3. 50% of properties that should be bought are in a 15km radius from the lake.
4. Properties selected to be bought in a 15km radius from lake correspond to 60% of expected profit.
<br>

## 6. Conclusion
The objective of this project was to create a online dashboard to House Rocket's CEO. Deploying the dashboard on Heroku platforms provided the CEO acess from anywhere facilitating data visualization and business decisions.
<br><br>

## 7. Next Steps
* Determine which season of the year would be the best to execute a sale
* Get more address data to fill NAs
* Expand the methodology to other regions operated by House Rocket
<br>

***
### References
* Blog [Seja um Data Scientist](https://sejaumdatascientist.com/)
* Dataset House Sales in King County (USA) from [Kaggle](https://www.kaggle.com/harlfoxem/housesalesprediction)
