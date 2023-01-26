from django.shortcuts import render, HttpResponse,redirect
import pickle
from app.models import Healthyheart_Users
from datetime import datetime
import numpy as np
from django.contrib import messages

# Create your views here
def home(request):
    return render(request, 'home.html')

def checkup(request):
    return render(request, 'checkup.html')

def prediction(request):
    if request.method == 'POST':
        Patient_name = request.POST['name']
        Age = request.POST['age']
        Gender = request.POST['sex']
        Chestpaintype = request.POST['chestpain']
        RestBP = request.POST['rbp']
        Cholestrol = request.POST['chol']
        Heartrate = request.POST['heartrate']
        Exercise_induced_angina = request.POST['eia']
        Oldpeak = request.POST['oldpeak']
        Slope = request.POST['slope']
        No_of_vessels = request.POST['vessels']
        Thal = request.POST['thal']

        if Chestpaintype =='0':
            Chestpaintype = '1'
        else:
            Chestpaintype = '0'

        if Slope == '2':
            Slope = '1'
        else:
            Slope = '0'

        if No_of_vessels == '0':
            No_of_vessels = '1'
        else:
            No_of_vessels = '0'

        if Thal == '2':
            T2 = '1'
            T3 = '0'
        elif Thal == '3':
            T3 = '1'
            T2 = '0'
        else:
            T2 = '0'
            T3 = '0'

        model = pickle.load(open('svmmodel.pkl', 'rb'))

        response = [int(Age),int(Chestpaintype),int(RestBP),int(Cholestrol),
        int(Heartrate), int(Exercise_induced_angina), float(Oldpeak), int(Slope), int(No_of_vessels),int(T2), int(T3)]

        response = np.array(response).reshape(1,-1)

        output = model.predict(response)
        
        User_data = Healthyheart_Users( Patient_name = Patient_name, Age =Age, Gender =Gender, 
        Chestpaintype =Chestpaintype, RestBP =RestBP, Cholestrol =Cholestrol,
        Heartrate=Heartrate, Exercise_induced_angina=Exercise_induced_angina,
        Oldpeak= Oldpeak, Slope=Slope, No_of_vessels =No_of_vessels, Thal= Thal,
        Report_date = datetime.now() )

        User_data.save()

        messages.success(request, "Your form is sucessfully submitted !!")

        context = {
        'name' : Patient_name,
        'age': Age,
        'gender': Gender,
        'chestpain': Chestpaintype,
        'bp' : RestBP,
        'cholestrol': Cholestrol,
        'heartrate': Heartrate,
        'eia': Exercise_induced_angina,
        'oldpeak' : Oldpeak,
        'slope' : Slope,
        'vessels': No_of_vessels,
        'thal' : Thal,
        'output': output[0]
        }
        return render(request, 'prediction.html', context)
        