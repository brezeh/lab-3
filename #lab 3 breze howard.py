#lab 3 breze howard

#importing os and csv file 
import os
import csv

#variable
keep_going = 'y'

#define the function
def main():
    data = getdata()
    serialsearch(data)

#getting budget data
def getdata():
    with open("budget_data.csv", "r") as sales: 
        get = csv.reader(sales)
        next(get)
        data = []
        for dates in get:
            data.append(dates)
    return data

#searching the dates/getting profit/loss
def serialsearch(data):
    serialsearch = input("what date would you like to search?")
    i = 0
    found = False
    for value in data:
        if serialsearch in value[0]:
            found = True
            print(f"{serialsearch}:${value[1]}")

#call the function and restart
while keep_going == 'y':
    main()
    keep_going = input ('would you like to run again? ')