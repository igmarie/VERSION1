import csv

def AirportList():
    dataline = ' '
    f = open('Airports.txt','r')
    for row in csv.reader(f):
        dataline= [row[0],row[1],row[2],row[3]]
        Airports.append(dataline)
    f.close()
    print(Airports)

def DetailsForAirport():
    code= input('which UK airport would you like to find, enter a barcode: ')
    if code == 'BOH' or 'LPL':
        OverSeas()
    else:
        print('Invalid Code')

def OverSeas():
    Airports= input('please enter a overseas barcode: ')
    Found = False
    i = 0
    while i < len(Airports)and Found == False:
        if code == Airports [i][0]:
            Found = True
        if not Found:
            print('Invalid Code')
                
            
def FLightDetails():
    Aircraft= print('please enter the type of aircraft')
    print('[1] Medium Narrow Body')
    print('[2] Large Narrow Body')
    print('[3] Medium wide body')
    choice = input()
    if choice == '1':
        AircraftSeats()
    elif choice == '2':
        AircraftSeats()
    elif choice == '3':
        AircraftSeats()
    else:
        print('please choose a option')
        
"""
def AircraftSeats():
    costperseat= -1
    maximumseats= -1
    capacity= -1
    

    if Aircraft == 1:
        costperseat= 8
        maximumseatrange= 2650
        capacity= 180
    elif Aircraft == 2:
        costperseat= 7
        maximumseatrange= 5600
        capacity= 220
    elif Aircraft == 3:
        costperseat=5
        maximumseatrange = 4060
        capacity = 406
    print('the cost per seat is: '+str(costperseat)+'/n the maxiumum seat range is'+str(maxiumumseatrange)+'/n the capacity is: '(capacity))
"""
        
        


#def PriceAndProfit():
    
def Menu():
    print('Please choose one of the following: ')
    print('[1] Input airport details')
    print('[2] Input flight details')
    print('[3] Input price & Calculate profit')
    print('[Q] To Quit')
    choice = input()
    while choice !='Q':
        if choice == '1':
            DetailsForAirport()
        elif choice == '2':
            print('Details for flight')
            FlightDetails()
        elif choice == '2':
            print('Price and profit')
            PriceAndProfit()
        else:
            ('please choose a option')
            
    choice = input()
    print('Please choose one of the following: ')
    print('[1] Input airport details')
    print('[2] Input flight details')
    print('[3] Input price')
    print('[Q] To Quit')

#def ClearData():

#main
Airports= []
Menu()
AirportList()
OverSeas()


