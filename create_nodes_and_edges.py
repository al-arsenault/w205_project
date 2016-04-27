import csv

#first convert the pipe-delimited text to a csv

with open('cn16.txt', 'rb') as f:
  readerpipe = csv.reader(f, delimiter = '|')
  with open('cn16.csv', 'wb') as outputfile:
      writer = csv.writer(outputfile)
      writer.writerows(readerpipe)

#now open and read the csv

with open('cn16.csv', 'rb') as g:
  reader = csv.reader(g)
  with open('candidate.csv', 'wb') as outputfile:
    for row in reader:
       candidate_ID = row[0]

       #need to remove commas from the candidate's name

       name = row[1]
       candidate_name = name.translate(None, ',')
       election_year = row[3]
       office = row[5]
       committee_ID = row[9]
       if election_year == '2016' and office == 'P': 
           s = candidate_ID + ',' + candidate_name + ',' + office + ',' + committee_ID + '\n'
#           writer = csv.writer(outputfile)
#           writer.writerows(s)
           outputfile.write(s)


import csv

#first convert the pipe-delimited text to a csv

with open('cm16.txt', 'rb') as f:
  readerpipe = csv.reader(f, delimiter = '|')
  with open('cm16.csv', 'wb') as outputfile:
      writer = csv.writer(outputfile)
      writer.writerows(readerpipe)

#now open and read the csv

with open('cm16.csv', 'rb') as g:
  reader = csv.reader(g)
  with open('committee.csv', 'wb') as outputfile:
    for row in reader:
       committee_ID = row[0]
       committee_name = row[1]
       committee_type = row[9]
       candidate_ID = row[14]
       if committee_type == 'P': 
           s = committee_ID + ',' + committee_name + ',' + committee_type + ',' + candidate_ID + '\n'
#           writer = csv.writer(outputfile)
#           writer.writerows(s)
           outputfile.write(s)


import csv

#first convert the pipe-delimited text to a csv

with open('indiv16.txt', 'rb') as f:
  readerpipe = csv.reader(f, delimiter = '|')
  with open('indiv16.csv', 'wb') as outputfile:
      writer = csv.writer(outputfile)
      writer.writerows(readerpipe)

#now open and read the csv

with open('indiv16.csv', 'rb') as g:
  reader = csv.reader(g)
  with open('individual_contributions.csv', 'wb') as outputfile:
    for row in reader:
       committee_ID = row[0]
       trans_type = row[5]
       entity_type = row[6]

       #Need to remove commas from the contributor's name

       name = row[7]
       contributor_name = name.translate(None, ',')
       employer = row[11]
       amount = row[14] 
       s = committee_ID + ',' + trans_type + ',' + entity_type + ',' + contributor_name + ',' + employer + ',' + amount + '\n'
#           writer = csv.writer(outputfile)
#           writer.writerows(s)
       outputfile.write(s)


import csv

#first convert the pipe-delimited text to a csv

with open('itpas216.txt', 'rb') as f:
  readerpipe = csv.reader(f, delimiter = '|')
  with open('itpas216.csv', 'wb') as outputfile:
      writer = csv.writer(outputfile)
      writer.writerows(readerpipe)

#now open and read the csv

with open('itpas216.csv', 'rb') as g:
  reader = csv.reader(g)
  with open('pass_through.csv', 'wb') as outputfile:
    for row in reader:
       committee_ID = row[0]
       trans_type = row[5]
       employer = row[11]
       amount = row[14]
       candidate_ID = row[16] 
       s = committee_ID + ',' + trans_type + ',' + employer + ',' + amount + ',' + candidate_ID + '\n'
#           writer = csv.writer(outputfile)
#           writer.writerows(s)
       outputfile.write(s)


