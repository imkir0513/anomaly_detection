from flask import Flask, request, render_template
import pandas as pd
import joblib


# Declare a Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    
    # If a form is submitted
    if request.method == "POST":
        
        # Unpickle classifier
        # clf = joblib.load("/Users/meizhuchen/Desktop/Columbia/Columbia_summer/5450/Machine-Learning-Web-App-main/dtree.pkl")
        
        # Get values through input bars
        hour = request.form.get("hour")
        amt = request.form.get("amt")
        age = request.form.get("age")
        
        # # Put inputs to dataframe
        # X = pd.DataFrame([[hour, amt]], columns = ["hour", "amt"])
        
        # Get prediction
        # prediction = clf.predict(X)[0]

        dtree = joblib.load("/usr/share/nginx/html/dtree.pkl")

        # X = pd.DataFrame([[90, 30]], columns = ["Height", "Weight"])
        X = pd.DataFrame([[2, 1,0,0,1,hour,amt,47,age,6011724471098086]], columns = ['city_pop_segment', 'location', 'gender', 'hourEnc', 'category', 'hour',
               'amt', 'state', 'age', 'cc_num'])
        dtree_pred = dtree.predict(X)[0]

        if dtree_pred==1:
            #prediction = "Default. I got you."
            return render_template("fraud.html")
        else:
            #prediction = "Non Default."
            return render_template("Not_fraud.html")
        
    else:
        return render_template("website.html")

# Running the app
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
    #app.run(debug = True)
