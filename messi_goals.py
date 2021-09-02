# la_liga_goals = 43
# champions_league_goals = 10
# copa_del_rey_goals = 5

# total_goals = la_liga_goals  + champions_league_goals + copa_del_rey_goals
# print(total_goals)

# def messi_goals(la_liga,uefa,copa):
#     sum = la_liga  + uefa + copa
#     print(sum) 
# messi_goals(43,10,5)

def messi_goals():
    laliga = int(input('Enter laliga goals\n'))
    uefa = int(input('Enter Uefa goals\n'))
    copa = int(input('Enter Copa goals\n'))

    sum = laliga + uefa + copa 
    print(f'Messi total goals are {sum}')
messi_goals()    
