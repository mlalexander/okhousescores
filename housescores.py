import csv
from sunlight import openstates

ok_legislators = openstates.legislators(
    state='ok',
    active='true',
    chamber='lower'
)

ok_legislators_csv_key = ['leg_id']
ok_legislators_array = []
for legislator in ok_legislators:
    ok_legislators_csv_key.append(legislator['leg_id'])
    ok_legislators_array.append(legislator['leg_id'])

with open('scores.csv', 'w') as w:
    writer = csv.DictWriter(w, fieldnames=ok_legislators_csv_key, extrasaction='ignore')
    writer.writeheader()

    for legislatorA in ok_legislators_array:
        print "Going through " + legislatorA

        leg_scores = {}
        leg_scores['leg_id'] = legislatorA

        for legislatorB in ok_legislators_array:

            # open the votes csv file
            with open('housevotes.csv') as f:
                reader = csv.DictReader(f)

                voteCount = 0
                voteSame = 0
                notComparable = 0

                for bill in reader:

                    if not bill[legislatorA] or not bill[legislatorB]:

                        notComparable += 1

                    elif bill[legislatorA] == bill[legislatorB]:

                        voteCount += 1
                        voteSame += 1

                    else:

                        voteCount += 1

                try:
                    score = voteSame
                    leg_scores[legislatorB] = score

                except ZeroDivisionError:
                    leg_scores[legislatorB] = "x"

        writer.writerow(leg_scores)
