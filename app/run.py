from flask import Flask, render_template, request, redirect
import pandas as pd
import time
import visualizations
import GeoFilter

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('directions.html')

@app.route('/viz', methods=["GET","POST"])
def viz():
    return render_template('project - viz.html')

@app.route('/map', methods=["GET","POST"])
def map():
    return redirect("http://localhost:5000")

@app.route('/button', methods=["GET","POST"])
def button():
    if request.method == "POST":
        user = list()
        start_add = list()
        start_lat = list()
        start_long = list()
        end_add = list()
        end_lat = list()
        end_long = list()

        user.append(request.form['userid'])
        start_add.append(request.form['start_add'])
        start_lat.append(request.form['s_lat'])
        start_long.append(request.form['s_long'])
        end_add.append(request.form['end_add'])
        end_lat.append(request.form['e_lat'])
        end_long.append(request.form['e_long'])

        df1 = pd.DataFrame(list(zip(user, start_add, start_lat, start_long, end_add, end_lat, end_long)),
                           columns=['UserID', 'Start_Address', 'Start_Lat', 'Start_Long', 'End_Address', 'End_Lat', 'End_Long'])
        df1.to_csv(r'./static/user_choice.csv', index=False)
        df1.to_csv(r'user_choice.csv', index=False)

        visualizations.main()
        
    #return render_template('directions.html')
    return redirect("http://localhost:5000")

if __name__ == '__main__':
    app.run(debug=True)
