from sunlight import openstates
import csv
import re

oklahoma_lower_bills = openstates.bills(
    state='ok',
    search_window='term:2015-2016',
)

#retrieves legislators in the house,
ok_legislators = openstates.legislators(
    state='ok',
    chamber='lower',
    active='true'
)

ok_legislators_array = ['bill_id', 'chamber', 'vote_id']
for legislator in ok_legislators:
    ok_legislators_array.append(legislator['leg_id'])

with open('housevotes.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=ok_legislators_array, extrasaction='ignore')

    writer.writeheader()

    for bill in oklahoma_lower_bills:
        oklahoma_bill_details = openstates.bill_detail(
            state='ok',
            session='2015-2016',
            bill_id=bill['bill_id']
        )

        for bill_votes in oklahoma_bill_details['votes']:

            pattern = re.compile('third', re.IGNORECASE)

            if pattern.search(bill_votes['motion']):

                total_votes = {}

                total_votes['bill_id'] = bill_votes['bill_id']
                total_votes['vote_id'] = bill_votes['vote_id']
                total_votes['chamber'] = bill_votes['chamber']


                for yes_votes in bill_votes['yes_votes']:
                    total_votes[yes_votes['leg_id']] = 1

                for no_votes in bill_votes['no_votes']:
                    total_votes[no_votes['leg_id']] = 2

                try:
                    writer.writerow(total_votes)

                except ValueError:
                    print "error"
