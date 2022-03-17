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

Data sources

we are picking Github,Stackoverflow,Kaggle and Twitter as our main source.
<img width="569" alt="image" src="https://user-images.githubusercontent.com/94630833/158832186-75c0bd85-82df-4586-b0f6-38c870c1e56c.png">


API integration

Each of the datasource folder is created and the script is included.

Normalising the score

 Three methods we have tried to implement in the normaliser 
 
 1. X(norm)= X-min(x)/max(x)- min(x)

 3. we used harmonicc mean for some attributes and arthimetic mean of all the harmonic mean
 
 5. we used scaler funcations

Information on database

We have used SQLlite database for this project ,name :HushHush.db available in Application-->Data (folder)

Selection Algorithims

To avoid people hacking the algorithm, we are selecting on the basis of percentiles instead of absolute scores of candidates.
STEP 1: Check normalized score of candidates in all datasets except Twitter.

STEP 2: Candidates will be selected as per the percentiles below (in any dataset).

STEP 3: For remaining candidates:(candidates who are below 70percentile in all datasets)

STEP 4: Sort Candidates by the sum of Weighted Score in Descending order. 

STEP 5: Candidates will be selected as per the below percentile hierarchy.

<img width="240" alt="image" src="https://user-images.githubusercontent.com/94630833/158832050-11e6a7bd-58e4-4a42-be1d-d0f93c3860a2.png">
Email Notification
Interphase
Application Design



Credits

This is a group project of Big data programming-1(semester -1) for the master program in big data and business analytics.
Developers  are Sasha (@Rrschch-6), Nissy (@sasidn), Garima (@Garima27dec) ,Omer(@atesch93) and Fatemeh (@karampanah927)


