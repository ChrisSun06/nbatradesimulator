from tkinter import *
from tkinter import _setit, messagebox
from tkinter.ttk import *
from main import getPlayersContracts, checkOverCap

number_of_fields = 2
starting_list = ["GSW", "OKC", "TOR", "POR", "DAL"]
entry_list, option_list, option_var = [], [], []

team1 = ["Please choose a team first"]
team2 = []
team1salary, team2salary = [], []

selected_player_team1 = {}
selected_player_team2 = {}
trading_team1 = {}
trading_team2 = {}

total_team_sal1, total_team_sal2 = 0, 0
NBA_CAP_MAXIMUM = 109140000
NBA_LUXURY_THRESHOLD = 136870000


def quit():
    raise SystemExit()

# Function for add for team 1
def test(*args):
    print(var2.get())
    print(var3.get())
    if var2.get() == "Please choose a team first":
        return
    trading_team1[var2.get()] = selected_player_team1[var2.get()]
    text_team1.config(state="normal")
    text_team1.insert(INSERT, var2.get() + ": $" + str(selected_player_team1[var2.get()]) + '\n')
    text_team1.config(state="disabled")

# Function for add for team 2
def test2(*args):
    print(var2.get())
    print(var3.get())
    if var3.get() == "Please choose a team first":
        return
    trading_team2[var3.get()] = selected_player_team2[var3.get()]
    text_team2.config(state="normal")
    text_team2.insert(INSERT, var3.get() + ": $" + str(selected_player_team2[var3.get()]) + '\n')
    text_team2.config(state="disabled")


# if an item is selected in one of the
# menus run this function
def reset_menu(sel_item):
    # for each field
    for field in range(number_of_fields):
        new_list = [x for x in starting_list]
        selection = option_var[field].get()

        for option in starting_list[1:6]:
            #add selectable blank if option is selected
            if str(selection) == str(option):
                new_list.insert(0, "")
            for j in range(number_of_fields):
                if str(selection) != str(option) and str(option_var[j].get()) == str(option):
                    new_list.remove(option)

        print("field", field, "new list=", new_list)
        print(selection)
        option_list[field].set_menu(*new_list)

        if field == 0:
            var2.set('')
            team1.clear()
            team1salary.clear()
            getPlayersContracts(team1, team1salary, selection)
            playermenu1['menu'].delete(0, 'end')
            for item in team1:
                playermenu1['menu'].add_command(label=item, command=_setit(var2, item))
                selected_player_team1[item] = team1salary[team1.index(item)]
        else:
            var3.set('')
            team2.clear()
            team2salary.clear()
            getPlayersContracts(team2, team2salary, selection)
            playermenu2['menu'].delete(0, 'end')
            for item in team2:
                playermenu2['menu'].add_command(label=item, command=_setit(var3, item))
                selected_player_team2[item] = team2salary[team2.index(item)]

# Trade Logic
def trade(*args):
    if var2.get() == "Please choose a team first":
        return
    total_salary_team1, total_salary_team2 = 0, 0
    salary_team1 = checkOverCap(option_var[0].get())
    salary_team2 = checkOverCap(option_var[1].get())
    for key in trading_team1:
        total_salary_team1 += trading_team1[key]
    for key2 in trading_team2:
        total_salary_team2 += trading_team2[key2]
    valid = True
    if salary_team1 == -1:
        if salary_team1 - total_salary_team1 + total_salary_team2 < NBA_LUXURY_THRESHOLD:
            if total_salary_team2 > min(1.5 * total_salary_team1, total_salary_team1 + 5000000):
                valid = False
        if total_salary_team2 > (1.25 * total_salary_team1 + 100000):
            valid = False
    else:
        if salary_team1 - total_salary_team1 + total_salary_team2 > (NBA_CAP_MAXIMUM + 100000):
            valid = False
    if salary_team2 == -1:
        if salary_team2 - total_salary_team2 + total_salary_team1 < NBA_LUXURY_THRESHOLD:
            if total_salary_team1 > min(1.5 * total_salary_team2, total_salary_team2 + 5000000):
                valid = False
        if total_salary_team1 > (1.25 * total_salary_team2 + 100000):
            valid = False
    else:
        if salary_team2 - total_salary_team2 + total_salary_team1 > (NBA_CAP_MAXIMUM + 100000):
            valid = False
    if valid is False:
        messagebox.showinfo("Message", "Trade is invalid")
    else:
        messagebox.showinfo("Message", "Trade is valid")


root = Tk()
root.title("OptionMenu")
root.geometry("540x280")

frame1 = LabelFrame(root, text="Team 1", width=300, height=150)
frame2 = LabelFrame(root, text="Team 2", width=300, height=150)
frame3 = LabelFrame(root, text="Result", width=300, height=300)

frame1.grid(row=0, column=0, sticky='nw')
frame2.grid(row=0, column=0, sticky='sw')
frame3.grid(row=0, column=1, sticky='e')


# menu variable for each field
for i in range(number_of_fields):
    option_var.append(StringVar(root))

# initial value for each field
for i in range(number_of_fields):
    option_var[i].set("")

# create menu for each field
option_list.append(OptionMenu(frame1, option_var[0], *starting_list, command=reset_menu))
option_list.append(OptionMenu(frame2, option_var[1], *starting_list, command=reset_menu))
var2 = StringVar(root)
var2.set(team1[0])
var3 = StringVar(root)
var3.set(team1[0])
playermenu1 = OptionMenu(frame1, var2, *team1, command=test)
playermenu1.grid(row=1, column=0, sticky=N + S + W + E)
playermenu2 = OptionMenu(frame2, var3, *team1, command=test)
playermenu2.grid(row=2, column=0, sticky=N + S + W + E)

# build gui
for i in range(number_of_fields):
    option_list[i].grid(row=int(i), column=0, sticky=N + S + W + E)

button3 = Button(frame3, text="TRADE", command=trade)
button3.grid(row=0, column=1, sticky='e')

button1 = Button(frame1, text="ADD", command=test)
button1.grid(row=0, column=1, sticky='e')
button2 = Button(frame2, text="ADD", command=test2)
button2.grid(row=1, column=1, sticky='e')

text_team1 = Text(frame3, height=4, width=40)
text_team2 = Text(frame3, height=4, width=40)
text_team1.grid(row=1, column=1, sticky='e')
text_team2.grid(row=2, column=1, sticky='e')

mainloop()
