# uber-pickups-analysis


Data Source: https://www.kaggle.com/fivethirtyeight/uber-pickups-in-new-york-city


Information about data set

The dataset contains, roughly, TWO groups of files: 
● Uber trip data from 2014 (April - September), separated by month, with detailed location information. 
● Uber trip data from 2015 (January - June), with less fine-grained location information. 

Uber trip data from 2014 
There are six files of raw data on Uber pickups in New York City from April to September 2014. The files are separated by month and each has the following columns: 
● Date/Time : The date and time of the Uber pickup 
● Lat : The latitude of the Uber pickup 
● Lon : The longitude of the Uber pickup 
● Base : The TLC base company code affiliated with the Uber pickup. 
These files are named: 
● uber-raw-data-apr14.csv 
● uber-raw-data-aug14.csv 
● uber-raw-data-jul14.csv 
● uber-raw-data-jun14.csv 
● uber-raw-data-may14.csv 
● uber-raw-data-sep14.csv 

Uber trip data from 2015 

Also included is the file uber-raw-data-janjune-15.csv This file has the following columns: 
● Dispatching_base_num : The TLC base company code of the base that dispatched the Uber. 
● Pickup_date : The date and time of the Uber pickup ● Affiliated_base_num : The TLC base company code affiliated with the Uber pickup. 
● locationID : The pickup location ID affiliated with the Uber pickup 
These files are named: 
- uber-raw-data-janjune-15.csv

Flow of Project
We have done Exploratory Data Analysis on full data then we have removed outliers using "LocalOutlierFactor", then finally we have used KNN technique to predict to train the data and to predict whether the transaction is Fraud or not. We have also applied T-SNE to visualize the Fraud and genuine transactions in 2-D.

How to Run the Project

In order to run the project just download the data from above mentioned source then run any file.

Prerequisites
You need to have installed following softwares and libraries in your machine before running this project.

Python 3
Anaconda: It will install ipython notebook and most of the libraries which are needed like sklearn, pandas, seaborn, matplotlib, numpy, scipy.

Installing

Python 3: https://www.python.org/downloads/
Anaconda: https://www.anaconda.com/download/

Authors

KILARI JASWANTH and DEVA DEEKSHITH - comined  work
