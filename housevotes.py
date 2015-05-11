import csv
from sunlight import openstates

ok_legislators = openstates.legislators(
    state='ok',
    active='true'
)

ok_legislators_csv_key = ['leg_id']
ok_legislators_array = []
for legislator in ok_legislators:
    ok_legislators_csv_key.append(legislator['leg_id'])
    ok_legislators_array.append(legislator['leg_id'])

with open('housescores.csv', 'w') as w:
    writer = csv.DictWriter(w, fieldnames=ok_legislators_csv_key, extrasaction='ignore')
    writer.writeheader()

    for legislatorA in ok_legislators_array:

        leg_scores = {}
        leg_scores['leg_id'] = legislatorA

        for legislatorB in ok_legislators_array:

            with open('housevotes.csv') as f:
                reader = csv.DictReader(f)

                voteTotal = 0
                match = 0
                noMatch = 0

                for bill in reader:

                    if not bill[legislatorA] or not bill[legislatorB]:

                        noMatch += 1

                    elif bill[legislatorA] == bill[legislatorB]:

                        voteTotal += 1
                        match += 1

                    else:

                        voteTotal += 1

        writer.writerow(leg_scores)
