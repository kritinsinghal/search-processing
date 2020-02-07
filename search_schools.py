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
		searchset = []
		duplicateSet = []
		interSet = []
		f = 0
		splitQuery = query.split(" ")
		for x in splitQuery:
			x = x.upper()
			if x in self.data.keys():
				k = self.data[x]
			else:
				continue

			if len(searchset) > 3 and len(k) > 3:
				interSet = interSet + list(set(searchset).intersection(set(k)))

			if f == 0 and len(k) > 3:
				searchset = k
				f = 1
			elif len(searchset) == 3:
				break
			elif len(k) < 3:
				duplicateSet = list(set(searchset).difference(set(k)))
				searchset = searchset + duplicateSet
			elif len(k) > 3:
				duplicateSet = list(set(searchset).difference(set(k)))
				searchset = searchset + duplicateSet


		print("Results for \"" + query + "\"\n")
		if len(interSet) >= 3:	
			for i in range(1, 4):
				print(str(i) + ". " + interSet[i])

		else:
			for i in range(1, len(searchset)):
				print(str(i) + ". " + searchset[i-1])
				if i == 3:
					break


# Run the following command to execute the search. The preprocessing of data takes a while but the search is quite fast.
# p = SearchSchool()
# query = "jefferson belleville"
# start = datetime.datetime.now()
# p.school_search(query)
# end = datetime.datetime.now()
# print(end-start)
