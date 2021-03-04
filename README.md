# Wildfire Severity Prediction using USA NASA Soils and Vegetation Datasets 

## Research Problem:
Climate change has increased the risk of wildfires in the Western United States by creating warmer, drier conditions, increasing drought severity and extending the fire season. "Federal wildfire suppression costs in the United States have spiked from an annual average of about $425 million from 1985 to 1999 to $1.6 billion from 2000 to 2019, according to data from the National Interagency Fire Center. [NFPA Journal 2020](https://www.nfpa.org/News-and-Research/Publications-and-media/NFPA-Journal/2020/November-December-2020/Features/Wildfire#:~:text=Federal%20wildfire%20suppression%20costs%20in,the%20National%20Interagency%20Fire%20Center.)" The probability of wildfire occurrence and the severity of wildfires depends on numerous influencing factors including air temperature, soil moisture, type of vegetation and potential fuel. 

## Objective: 
Use relevant data (i.e. soil type, vegetation classification) at each site location where a wildfire has occurred to predict the probability of wildfire occurrence and the severity of wildfires using machine learning techniques (e.g. regression, classification, etc.). 

## Research Questions:
1) Can site location (latitude, longitude), soil type, vegetation and other relevant information be used to predict the likelihood of fire occurrence in the Western US? 
2) Can site location (latitude, longitude), soil type, vegetation and other relevant information be used to predict the severity of wildfires in the Western US? 
3) Can this information be used to predict future trends in wildfire severity and occurrence, assuming climate change continues at the current rate?
 
## Datasets: 
1) Relatively large (800 MB) wildfire dataset containing ~188 million wildfire records from 1992 - 2015 [Kaggle](https://www.kaggle.com/rtatman/188-million-us-wildfires)
2) NASA Land Data Assimilation System (NLDAS) vegetation dataset (14-class UMD map at 1-km; 5MB) [NASA vegetation class] (https://ldas.gsfc.nasa.gov/nldas/vegetation-class)
3) NLDAS soil type dataset (1-km Penn State STATSGO data and have 16 texture types; 5MB) [NASA soils dataset](https://ldas.gsfc.nasa.gov/nldas/soils)
* Other available datasets may be used within this analysis. 

![Fig1_numfires](https://user-images.githubusercontent.com/20464090/109897888-613d2080-7c61-11eb-89ec-4753acd10d4d.png)

## Methods:
First, this work will develop machine learning techniques and prediction frameworks (e.g. regression, classification, etc.) for analyzing Oregon wildfires. Then, the methods will be applied to other western US states. Model performance will be based on a variety of evaluation metrics including R^2, RMSE, MAE, etc. 

## Broader Impacts:
All produced methods, tools and datasets will be freely available and open source. A juptyer notebook will execute all code and reproducing all visualizations. A user will be able to easily adapt the model inputs and notebook to fit their specific regional or temporal areas of interest. A QGIS dataset will also be made available, where a user can interact with the dataset and models. The proposed methods can be used to study past or current fire monitoring and prediction metrics. Private consultants and state and federal policy and decision makers can apply these methods to inform land management in areas with increasing risk of wildfire. 
