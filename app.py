from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pandas as pd
import pickle


app = Flask(__name__)
model = pickle.load(open('flight_rf.pkl', 'rb'))

@app.route("/")
def home():
    render_template('home.html')

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method=='POST':

        # Date of journey
        data_dep = request.form['Dep_Time']
        journey_day = int(pd.to_datetime(data_dep, format="%Y-%m-%dT%H:%M").day)
        journey_month = int(pd.to_datetime(data_dep, format="%Y-%m-%dT%H:%M").month)

        # Departure
        dep_hour = int(pd.to_datetime(data_dep, format="%Y-%m-%dT%H:%M").hour)
        dep_minute = int(pd.to_datetime(data_dep, format="%y-%m-%dT%H:%M").minute)

        # Arrival Time
        date_arr = request.form['Arrival_Time']
        arrival_hour = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").hour)
        arrival_minute = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").minute)

        # Duration
        dur_hour = abs(arrival_hour-dep_hour)
        dur_mins = abs(arrival_minute- dep_minute)

        # Total Stops
        Total_stops = int(request.form['stops'])

        # airline
        airline = request.form['airline']
        if (airline == 'Jet Airways'):
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            Air_Asia = 0
            GoAir = 0
            Multiple_carriers_Premium_Ecanomy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_Ecanomy = 0
            Trujet = 0

        elif (airline == 'IndiGo'):
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            Air_Asia = 0
            GoAir = 0
            Multiple_carriers_Premium_Ecanomy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_Ecanomy = 0
            Trujet = 0

        elif (airline == 'Air India'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            Air_Asia = 0
            GoAir = 0
            Multiple_carriers_Premium_Ecanomy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_Ecanomy = 0
            Trujet = 0

        elif (airline == 'Multiple carriers'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            Air_Asia = 0
            GoAir = 0
            Multiple_carriers_Premium_Ecanomy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_Business = 0
            Trujet = 0

        elif (airline == 'SpiceJet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            Air_Asia = 0
            GoAir = 0
            Multiple_carriers_Premium_Ecanomy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_Business = 0
            Trujet = 0

        elif (airline == 'Vistara'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            Air_Asia = 0
            GoAir = 0
            Multiple_carriers_Premium_Ecanomy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_Business = 0
            Trujet = 0

        elif (airline == 'Air Asia'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            Air_Asia = 1
            GoAir = 0
            Multiple_carriers_Premium_Ecanomy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_Business = 0
            Trujet = 0

        elif (airline == 'GoAir'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            Air_Asia = 0
            GoAir = 0
            Multiple_carriers_Premium_Ecanomy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_Business = 0
            Trujet = 0

        elif (airline == 'Multiple carriers Premium Ecanomy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            Air_Asia = 0
            GoAir = 0
            Multiple_carriers_Premium_Ecanomy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_Business = 0
            Trujet = 0

        elif (airline == 'Jet Airways Business'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            Air_Asia = 0
            GoAir = 0
            Multiple_carriers_Premium_Ecanomy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_Business = 0
            Trujet = 0

        elif (airline == 'Vistara Premium Business'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            Air_Asia = 0
            GoAir = 0
            Multiple_carriers_Premium_Ecanomy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_Business = 1
            Trujet = 0

        elif (airline == 'Trujet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            Air_Asia = 0
            GoAir = 0
            Multiple_carriers_Premium_Ecanomy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_Business = 0
            Trujet = 1

        else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            Air_Asia = 0
            GoAir = 0
            Multiple_carriers_Premium_Ecanomy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_Business = 0
            Trujet = 0


        Source = request.form['Source']
        if Source == 'Delhi':
            s_Delhi = 1
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0

        elif (Source == 'Kolkata'):
            s_Delhi = 0
            s_Kolkata = 1
            s_Mumbai = 0
            s_Chennai = 0

        elif (Source == 'Mumbai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 1
            s_Chennai = 0

        elif (Source == 'Chennai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 1


        else:
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0


        Source == request.form['Destination']
        if Source == 'Cochin':
            d_Cochin = 1
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (Source == 'Delhi'):
            d_Cochin = 0
            d_Delhi = 1
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (Source == 'New Delhi'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 1
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (Source == 'Hyderabad'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 1
            d_Kolkata = 0

        elif (Source == 'Kolkata'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 1

        else:
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0


        prediction = model.predict([[
            Total_stops,
            journey_day,
            journey_month,
            dep_hour,
            dep_minute,
            arrival_hour,
            arrival_minute,
            dur_hour,
            dur_mins,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_Ecanomy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_Ecanomy,
            s_Chennai,
            s_Kolkata,
            s_Delhi,
            s_Mumbai,
            d_Kolkata,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_New_Delhi
        ]])

        output = round(prediction, 2)

        return render_template('home.html', prediction_text = 'Your flight price is Rs. {}'.format(output))

    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)