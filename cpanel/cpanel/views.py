from django.shortcuts import render
import pyrebase

config = {
    'apiKey': "AIzaSyDFwjbd1F3wwTo3d3p2DScyTHKGX3MIdz4",
    'authDomain': "nbatraderdatabase.firebaseapp.com",
    'databaseURL': "https://nbatraderdatabase.firebaseio.com",
    'projectId': "nbatraderdatabase",
    'storageBucket': "nbatraderdatabase.appspot.com",
    'messagingSenderId': "667217101415",
    'appId': "1:667217101415:web:3401eab3b75809a6a7cac2",
    'measurementId': "G-SZ6ERYE5N1"
}
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def signIn(request):
    return render(request, "signIn.html")


# noinspection PyBroadException
@csrf_exempt
def postsign(request):
    email = request.POST.get("email")
    passw = request.POST.get("pass")
    try:
        user = auth.sign_in_with_email_and_password(email, passw)
    except:
        message = "invalid credentials"
        return render(request, "signIn.html", {"msg": message})
    print(user)
    return render(request, "welcome.html", {"e":email})
