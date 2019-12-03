1. DESCRIPTION

GENIE is a restaurant recommendation tool built with Python, D3, and Flask. It uses machine learning techniques to provide customized restaurant recommendations along a user-selected route.

2. INSTALLATION

Minimum Computer Requirements:
-8GB RAM
-512GB disk
-Dual-core Core i5

a. Download Yelp dataset json files (https://www.yelp.com/dataset/download)
-Files should include business.json, review,json, and user.json
b. Move json files to /YR/data folder
c. Run converter.py 
-Converts json to csv
-NOTE: Process may take over 2 minutes
d. Run pipeline.py
-Generates Las Vegas csv files
-Performs filtering and merges dataframes
-Generates LasVegas-reviews-user-business.csv
e. Run CrossValidationMapReduce.py
-Performs CV on algorithms with HP Tuning
-Generates LasVegas-cv-algos.csv
-NOTE: Process may take over 3 hours
f. Run recommender.py
-Uses geofilter and returns top 3 recommended restaurants along route
-Generates LasVegas-recommendations-svd-filtered.csv
g. Copy "LasVegas-cv-algos.csv" and "LasVegas-recommendations-svd-filtered.csv" into /app folder

3. EXECUTION - How to run a demo on your code

a. Navigate to /app folder, and run run.py
b. From the drop-down menus, select User ID and Start and End locations
c. Click "Create Recommendations" button
d. Refresh page to show route with 3 restaurant recommendations
-Can mouseover markers to display restaurant name above the marker
e. Click "View Visualizations" on the top left to view summary comparison visualizations
-Can mouseover bars to show rating and total reviews
-Can click restaurant name to open Yelp page
f. Click "View Map" to return to map and start over

DEMO VIDEO: https://www.youtube.com/watch?v=TSVMMBp17MU
