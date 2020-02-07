import csv
import datetime


class SearchSchool(object):

	def __init__(self):
		with open('school_data.csv', 'r', encoding='cp1252') as csv_file:
			csv_reader = csv.reader(csv_file)
			self.data = {}

			for row in csv_reader:
				school_name = row[3] + " " + row[4] + ", " + row[5]
				school = row[3].split(" ")
				city = row[4].split(" ")
				for x in school:
					if x in self.data:
						self.data[x] = list(set(self.data[x]).union(set([school_name])))
					else:
						self.data[x] = [school_name]

				for x in city:
					if x in self.data:
						self.data[x] = list(set(self.data[x]).union(set([school_name])))
					else:
						self.data[x] = [school_name]

				if row[5] in self.data:
					self.data[row[5]] = list(set(self.data[row[5]]).union(set([school_name])))
				else:
					self.data[row[5]] = [school_name]



	def school_search(self, query):
		searchset = {}
		duplicateSet = []
		interSet = []
		f = 0
		splitQuery = query.split(" ")
		for x in splitQuery:
			x = x.upper()
			if x in self.data.keys():
				 for y in self.data[x]:
				 	if y in searchset.keys():
				 		searchset[y] += 1
				 	else:
				 		searchset[y] = 1

		for key, value in searchset.items():
			duplicateSet.append([key, value])

		duplicateSet.sort(key=lambda x:x[1], reverse=True)
		print("Results for \"" + query + "\"\n")
		for i in range(0, len(duplicateSet)):
			print(str(i+1) + ". " + duplicateSet[i][0])
			if i == 2:
				break


# Run the following command to execute the search. The preprocessing of data takes a while but the search is quite fast.
# p = SearchSchool()
# query = "jefferson belleville"
# start = datetime.datetime.now()
# p.school_search(query)
# end = datetime.datetime.now()
# print(end-start)
