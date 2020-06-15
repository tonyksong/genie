# genie
### LAT35N Team91 CSE 6242 Group Project

1. DESCRIPTION<br>
GENIE is a restaurant recommendation tool built with Python, D3.js, and Flask. It uses machine learning techniques to provide customized restaurant recommendations along a user-selected route.
1. INSTALLATION<br/>
Minimum Computer Requirements:<br>
-8GB RAM<br>
-512GB disk<br>
-Dual-core Core i5<br>
-Firefox web browser (v69 or above)<br>
   1. [Download Yelp Dataset](https://www.yelp.com/dataset/download)
   1. Run converter.py
      1. Converts json to csv
   1. Run pipeline.py
      1. Generates Las Vegas csv files
      1. Performs filtering and merges dataframes
      1. Generates heart of collaborative filtering: *LasVegas-reviews-user-business.csv*
   1. Run CrossValidationMapReduce.py
      1. Performs CV on algorithms with HP Tuning
      1. Generates *LasVegas-cv-algos.csv*
   1. Run recommender.py

1. EXECUTION - How to run a demo on your code

   1. Navigate to /app folder, and run *run.py*
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
