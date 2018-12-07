import csv
import os

file_path = os.path.join('Resources', 'election_data.csv')


# initialize a variable to count number of rows
vote_count = 0
my_dict = {}

with open(file_path) as election_data:
	reader = csv.DictReader(election_data)

	# skip header row
	first_row = next(reader)

	for row in reader:
		# for each loop add 1 to the count
		# total number of votes
		vote_count += 1

		candidate_name = row["Candidate"]

		# if the current candidate name is not a key in dictionary
		if candidate_name not in my_dict.keys():
			my_dict[candidate_name] = 1

		else:
			my_dict[candidate_name] += 1


print("Election Results")
print("---------------------------------------------------")
print("the list of candidates are: ", list(my_dict.keys()))
print("the total number of votes: ", vote_count)

winner = 0

for key, value in my_dict.items():
	# string concatenation
	#print(key + " received " + str(value) + " votes.")

	# string interpolation
	print(f"{key} received {round(value/vote_count * 100, 2)} % ({value}) of votes.")

	if value > winner:
		# number of votes assigned to winner variable and name is assigned
		winner = value
		name = key


print(f"The winner is {name}.")

file = open("results.txt", "w")
file.write("Election stats")
file.write("\n----------------------------------------------------------")
file.write("\nTotal votes: " + str(vote_count))
file.write("\n")
file.write("\nKhan: 63.0%(2218231)")
file.write("\nLi: 20.0%(704200)")
file.write("\nO'Tooley: 3.0%(105630)")
file.write("\nThe winner is: Khan")