from firebase import firebase
import main
import tradergui

url = "https://nbatraderdatabase.firebaseio.com/"
table_teams_salary = "/nbatraderdatabase/teamsalary"
table_teams_player = "/nbatraderdatabase/player"
table_player_salary = "/nbatraderdatabase/salary"

firebase = firebase.FirebaseApplication(url, None)


def uploadTeamsSalary():
    data = {}
    for team in tradergui.starting_list:
        salary = main.checkOverCap(team)
        data[team] = salary
    firebase.post(table_teams_salary, data)


if __name__ == '__main__':
    uploadTeamsSalary()
