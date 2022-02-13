import sys
import csv
# Get args from command line
args = sys.argv
# Assign args to values
fileName = args[1]
dateWanted = args[3]
# Declare main data structure
cookieDict = {}
# Open file and turn into string
with open(fileName, newline='') as csvfile:
    cookieLog = csv.reader(csvfile, delimiter=',')
    for row in cookieLog:
        if row[0] == 'cookie':
            continue
        # Organize data from csv file into date, time, and cookie id
        currCookie = row[0]
        dateData = row[1]
        # Split inputted date into date and time if needed later
        dateNotFiltered = dateData.split('T')
        date = dateNotFiltered[0]
        time = dateNotFiltered[1]
        # Check if date is equal to the date we are searching and if so then increment counter for that cookie
        if date == dateWanted:
            if currCookie in cookieDict:
                cookieDict[currCookie] = cookieDict[currCookie] + 1
            else:
                cookieDict[currCookie] = 1
# Check which cookies are used the most and add them to an array
maxAmt = 0
returnCookies = []
for cookie in cookieDict:
    # If this cookie has more uses than max so far then reset array and redefine maxAmt
    if cookieDict[cookie] > maxAmt:
        returnCookies = [cookie]
        maxAmt = cookieDict[cookie]
    # If this cookie has the same uses as max then append it to our array
    elif cookieDict[cookie] == maxAmt:
        returnCookies.append(cookie)
# Print all the most active cookies
cookieStr = ""
for cookies in returnCookies:
    cookieStr = cookieStr + cookies + '\n'
# Save all the printed vals to a file
prevstdout = sys.stdout
sys.stdout = open('output.txt','w')
print(cookieStr)
sys.stdout.close()
sys.stdout = prevstdout
print(cookieStr)
