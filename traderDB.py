import pyrebase
import main
import tradergui

url = "https://nbatraderdatabase.firebaseio.com/"
table_teams_salary = "/nbatraderdatabase/teamsalary"
table_teams_player = "/nbatraderdatabase/player"
table_player_salary = "/nbatraderdatabase/salary"

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

fbase = firebase.FirebaseApplication(url, None)


def uploadTeamsSalary():
    data = {}
    for team in tradergui.starting_list:
        salary = main.checkOverCap(team)
        data[team] = salary
    fbase.post(table_teams_salary, data)


if __name__ == '__main__':
    uploadTeamsSalary()
