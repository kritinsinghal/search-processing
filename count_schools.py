import csv

def print_counts():
	with open('school_data.csv', 'r', encoding='cp1252') as csv_file:
		csv_reader = csv.reader(csv_file)
		total = 0
		states = {}
		mlocale = {}
		city = {}
		l = 0
		c = ""
		f = 0
		for row in csv_reader:
			if f == 0:
				f = 1
				continue

			total = total + 1
			
			if row[5] in states:
				states[row[5]] += 1
			else: 
				states[row[5]] = 1

			if row[8] in mlocale:
				mlocale[row[8]] += 1
			else:
				mlocale[row[8]] = 1

			if row[4] in city:
				city[row[4]] += 1

			else:
				city[row[4]] = 1


	for key, value in city.items():
		if value > l:
			l = value
			c = key

	print("Total Schools: " + str(total) + "\n")
	print("Schools by State:")
	for key, value in states.items():
		print(key + ": " + str(value))
	print("\nSchools by Metro-centric locale:")
	for key, value in mlocale.items():
		print(key + ": " + str(value))

	print("\nCity with most schools: " + c + " (" + str(l) + " schools)")
	print("\nUnique cities with at least one school: " + str(len(city.keys())) + "\n")


	
