Hush Hush-Recruiter

<img width="170" alt="image" src="https://user-images.githubusercontent.com/94630833/158576922-5f6261ee-d1bf-47ba-a98e-72bc65de5a25.png">

Hush Hush recruiter is an automated recruitment tool written in Python 3 that automates the entire analysis process of selecting potential candidate for Doodle firm.
The secretive process automatically sents email to an candidate if he is selected for a potential role at Doodle.

Recruiter wants to ensure that 
  1. The algorithm to hire a candidate cannot be deterministic 
  2. The data points of potential candidates can be picked over the data source from internet.
  3. The interface to provide the coding solutions should be  invalidated after a specified period
  
Table of contents

Overview

Through API we try to connect with each datasources which will provide the details on activities availble on the activities with their application.
All the datasources with normalised score will be populated to database which is common for all the source . 
From the source we implement our selection algorithm which will list down the potentional candidates and their position. 

we pick each of the candidates and sent them an email based which will have all the link for the doodle challenge.

Data sources

we are picking Github,Stackoverflow,Kaggle and Twitter as our main source.
<img width="569" alt="image" src="https://user-images.githubusercontent.com/94630833/158832186-75c0bd85-82df-4586-b0f6-38c870c1e56c.png">


API integration

Each of the datasource folder is created and the script is included.

Normalising the score

 Three methods we have used to normalise the score :
 
 1. X(norm)= X-min(x)/max(x)- min(x)

 3. we used harmonicc mean for some attributes and arthimetic mean of all the harmonic mean
 
 5. we used scaler funcations

Information on database

We have used SQLlite database for this project ,name :HushHush.db available in Application-->Data (folder)

Selection Algorithims

To avoid people hacking the algorithm, we are selecting on the basis of percentiles instead of absolute scores of candidates.
STEP 1: Check normalized score of candidates in all datasets except Twitter.

STEP 2: Candidates will be selected as per the percentiles below (in any dataset).

STEP 3: For remaining candidates (candidates who are below 70percentile in all datasets).

STEP 4: Sort Candidates by the sum of Weighted Score in Descending order. 

STEP 5: Candidates will be selected as per the below percentile hierarchy.

<img width="240" alt="image" src="https://user-images.githubusercontent.com/94630833/158832050-11e6a7bd-58e4-4a42-be1d-d0f93c3860a2.png">

Classification Algorithm

After implementing our main algorithm, for the further evaluation for new entries we decided to use a machine learning algorithm based on the labels we got from our main algorithm and our initial data. As SVM,NN, LogReg or other models that are trained with gradient descent, are doing very well when the variables are normalized or rescaled we tried these three algorithms with different parameters. Based on our data Neural Network had the best accuracy for us.
Multi-layer Perceptron is sensitive to feature scaling, so it is highly recommended to rescaled data with mean 0 and variance 1
Multi-layer Perceptron (MLP) is a supervised learning algorithm.
MLP algorithm trains using some form of gradient descent and the gradients are calculated using Backpropagation with no activation function in the output layer

Email Notification

<img width="332" alt="image" src="https://user-images.githubusercontent.com/94630833/158844270-38faf49e-cd14-4b68-88a4-20ffa75099e9.png">


Doodle challenge 

https://docs.google.com/forms/d/e/1FAIpQLScEOEKdgnWweYQLzpxiwOILcMvEi_dIuNPhbD6qvf0nUTMtVw/viewform?usp=sf_link


Application Design

<img width="524" alt="image" src="https://user-images.githubusercontent.com/94630833/158843813-67b36e95-000f-499a-bc8f-8c1a975d9adf.png">

Project structure

![image](https://user-images.githubusercontent.com/94630833/158851726-212ffa99-2bd8-43e1-9118-20bc5883cfd1.png)

Front end 
![image](https://user-images.githubusercontent.com/94630833/158851978-c9fb5658-09ce-4be5-a550-6e6e76d45636.png)



Credits

This is a group project of Big data programming-1(semester -1) for the master program in big data and business analytics.
Developers  are Sasha (@Rrschch-6), Nissy (@sasidn), Garima (@Garima27dec) ,Omer(@atesch93) and Fatemeh (@karampanah927)


