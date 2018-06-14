from django.shortcuts import render
import pyrebase

config = {
    'apiKey': "AIzaSyCBGzNP8o9KzDCQDlrGz0f3-V-zHSo_Rzs",
    'authDomain': "fire-3a365.firebaseapp.com",
    'databaseURL': "https://fire-3a365.firebaseio.com",
    'projectId': "fire-3a365",
    'storageBucket': "fire-3a365.appspot.com",
    'messagingSenderId': "655813168955"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

def signIn(request):
    return render(request, "signIn.html")

def postsign(request):
    return render(request,"welcome.html")