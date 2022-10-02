# DLW

## Table of Contents:
### 1)CV_clustering.ipynb 
### 2)recommendation.py

### CV_clustering.ipynb
The ipynb file contains the main Computer Vision Algorithm used by our application. A torch model is fited with an image which is sourced from a camera placed in every study space. The camera takes 4 pictures every 5 minutes.

### recommendation.py
After detecting the number people in the picture, we use a K-Means Clustering Algorithm to form clusters within the people detected. The model works on the assumption that a cluster detected by the algorithm is equivalent to an occupied table. This information is relayed t othe recommendation model.


Based on pre-surveyed data, we subtract the number of occupied tables from the total number of tables in a study space. Then, using a geolocation API the application will weigh the user's distance from a study space against it's occupancy, and recommend the best location for the user to go to.
