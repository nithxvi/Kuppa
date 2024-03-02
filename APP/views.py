from django.shortcuts import render, redirect
from . models import UserPersonalModel
from . forms import UserPersonalForm, UserRegisterForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
import numpy as np

import tensorflow 
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split


def Landing_1(request):
    return render(request, '1_Landing.html')

def Register_2(request):
    form = UserRegisterForm()
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created. ' + user)
            return redirect('Login_3')

    context = {'form':form}
    return render(request, '2_Register.html', context)


def Login_3(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home_4')
        else:
            messages.info(request, 'Username OR Password incorrect')

    context = {}
    return render(request,'3_Login.html', context)

def Home_4(request):
    return render(request, '4_Home.html')

def Teamates_5(request):
    return render(request,'5_Teamates.html')

def Domain_Result_6(request):
    return render(request,'6_Domain_Result.html')

def Problem_Statement_7(request):
    return render(request,'7_Problem_Statement.html')
    

def Per_Info_8(request):
    if request.method == 'POST':
        fieldss = ['firstname','lastname','age','address','phone','city','state','country']
        form = UserPersonalForm(request.POST)
        if form.is_valid():
            print('Saving data in Form')
            form.save()
        return render(request, '4_Home.html', {'form':form})
    else:
        print('Else working')
        form = UserPersonalForm(request.POST)    
        return render(request, '8_Per_Info.html', {'form':form})
    
model = tensorflow.keras.models.load_model('C:/Users/nithi/Music/MAIN_PROJECT/CODE/DEPLOYMENT/PROJECT/APP/DISEASE.h5')
dataset1 = "C:/Users/nithi/Music/MAIN_PROJECT/CODE/DEPLOYMENT/PROJECT/APP/SYMPTOMS.csv"

def Deploy_9(request): 
    if request.method == "POST":
        int_features = [x for x in request.POST.values()]
        input_text2 = int_features[1:]
        print(input_text2)

        if isinstance(input_text2[0], str):
            result = input_text2[0]
        else:
            result = None

        print(result)

        preprocessed_text = result.lower()

        df = pd.read_csv(dataset1)

        df['text'] = df['text'].apply(lambda x: x.lower() if pd.notna(x) else "")

        label_encoder = LabelEncoder()
        df['label'] = label_encoder.fit_transform(df['label'])
        num_classes = len(label_encoder.classes_)

        X = df['text']
        y = df['label']

        y = to_categorical(y, num_classes=num_classes)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        max_words = 10000  
        max_sequence_length = 100 
        tokenizer = Tokenizer(num_words=max_words)
        tokenizer.fit_on_texts(X_train)

        input_sequence = tokenizer.texts_to_sequences([preprocessed_text])
        input_padded = pad_sequences(input_sequence, maxlen=max_sequence_length)

        predicted_probabilities = model.predict(input_padded)
        predicted_class = np.argmax(predicted_probabilities, axis=1)[0]
        output_label = label_encoder.inverse_transform([predicted_class])[0]


        print("Predicted Label:", output_label)
        
        return render(request, '9_Deploy.html', {"prediction_text":f"THE {output_label} DISEASE MIGHT BE OCCUR IN THIS CONDITIONS"})
    else:
        return render (request, '9_Deploy.html')
   
def Per_Database_10(request):
    models = UserPersonalModel.objects.all()
    return render(request, '10_Per_Database.html', {'models':models})

def Logout(request):
    logout(request)
    return redirect('Landing_1')
