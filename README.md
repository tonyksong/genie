# genie
### LAT35N Team91 CSE 6242 Group Project

1. DESCRIPTION - GENIE is a restaurant recommendation tool built with Python, D3.js, and Flask. It uses machine learning techniques to provide customized restaurant recommendations along a user-selected route.
1. INSTALLATION<br/>
Minimum Computer Requirements:
-8GB RAM
-512GB disk
-Dual-core Core i5
-Firefox web browser (v69 or above)
   1. Download Yelp Dataset: https://www.yelp.com/dataset/download<br/>
   1. Run converter.py<br/>
     (Converts json to csv)<br/>
   1. Run pipeline.py<br/>
   1.   (Generates Las Vegas csv files, Performs filtering and merges dataframes, Generates heart of collaborative filtering:
     LasVegas-reviews-user-business.csv)<br/>
   1. Run CrossValidationMapReduce.py<br/>
     (Performs CV on algorithms with HP Tuning, Generates LasVegas-cv-algos.csv)<br/>
   1. Run recommender.py<br/>

1. EXECUTION - How to run a demo on your code

   1. Navigate to /app folder, and run run.py
   1. Copy local host 5000 link into Firefox browser and load page
   1. From the drop-down menus, select User ID and Start and End locations
   1. Click "Create Recommendations" button
   1. Refresh page to show route with 3 restaurant recommendations
      1. Can mouseover markers to display restaurant name above the marker
   1. Click "View Visualizations" on the top left to view summary comparison visualizations
      1. Can mouseover bars to show rating and total reviews
      1. Can click restaurant name to open Yelp page
   1. Click "View Map" to return to map and start over

DEMO VIDEO: https://www.youtube.com/watch?v=TSVMMBp17MU

Authors: Blaine Davenport, Rohit Pegallapati, Anthony Song, Shinji Ueno, Lingqi Zhang
