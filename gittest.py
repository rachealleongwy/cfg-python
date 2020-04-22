# cfg python 2020: spreadsheet project
# covid.csv lists 15 countries, their respective regions, number of confirmed cases and deaths

import csv

# read data from covid.csv spreadsheet
def read_data():
    data = []

    with open('covid.csv','r') as covid_csv:
        spreadsheet = csv.DictReader(covid_csv)
        for row in spreadsheet:
            data.append(row)
    return data

# collect all number of confirmed cases from each country into a single list
def run():
    data = read_data()

    confirmed_num = []
    for row in data:
        confirmed = int(row['confirmed'])
        confirmed_num.append(confirmed)

# output total number of cases across all 15 listed countries
    confirmed_total = sum(confirmed_num)
    print('Total confirmed: {}'.format(confirmed_total))

run()