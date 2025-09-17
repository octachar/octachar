import datetime
import math
import os

journals = "./content/subsections/journal/"

def dateNow():
	yearLength = 31449600
	secondsLength = 86400
	yearCurrent = 1341
	dayTemp = 0

	knownDate = datetime.datetime(1726, 4, 5)
	dayTemp = datetime.datetime.now() - knownDate
	realDate = int((dayTemp.days) * secondsLength)

	currentDate = 1

	x = datetime.datetime.now()
	if 0 <= int(x.hour) < 2:
		currentDate = realDate - secondsLength
	else:
		currentDate = realDate

	day = math.floor(currentDate/86400)
	month = math.floor(currentDate/2419200)

	# Get day number
	if day >= 28: 
		day = day - (28 * math.floor(day/28))
	if day >= 7:
		week = math.floor(day/7)
	else: 
		week = 0

	# Get month number
	y = math.floor(month/13)
	month = month - (13 * y)
	monthName = 0
	if month > 0:
		for x in range(1,13):
			if month % x == 0:
				monthName = x
				
	if currentDate > yearLength:
		yearCurrent = yearCurrent + math.floor(currentDate/yearLength)
	return str(day).rjust(2, "0") + "-" + str(monthName+1).rjust(2, "0") + "-" + str(yearCurrent) + "T00:00:00-00:00"

with open(journals + "journal" + str(len(os.listdir(journals)) + 1) + ".md", "w") as f:
    header = [
		"+++\n",
		"date = '" + dateNow() + "'\n",
		"draft = false\n",
		"title = 'Journal #" + str(len(os.listdir(journals))) + "'\n",
		"+++\n",
		"\n"
    ]
	
    f.writelines(header)

print(
	"Page created with information:\n",
	"\tDATE:\t" + dateNow() + "\n",
	"\tTITLE:\tJournal #" + str(len(os.listdir(journals))) + "\n"
)
