# cfg python 2020: spreadsheet project by racheal leong

# csv lists 15 countries, their regions, number of confirmed cases and deaths
import csv

# read data from covid.csv spreadsheet
def read_data():
    data = []

    with open('covid.csv','r') as covid_csv:
        spreadsheet = csv.DictReader(covid_csv)
        for row in spreadsheet:
            data.append(row)
    return data

def run():
    data = read_data()

    confirmed_num = []
    deaths_num = []
    ratio_num = []
    for row in data:
        # collect all confirmed cases from each country into a single list
        confirmed = int(row['confirmed'])
        confirmed_num.append(confirmed)
        # collect all deaths from each country into a single list
        deaths = int(row['deaths'])
        deaths_num.append(deaths)
        # collect ratio of deaths to confirmed cases into a single list
        ratio = float(int(row['deaths']) / int(row['confirmed']))
        ratio_num.append(ratio)

    confirmed_total = sum(confirmed_num)
    deaths_total = sum(deaths_num)
    print('Total confirmed cases: {:,}'.format(confirmed_total))      # output total number of confirmed cases
    print('Total deaths: {:,}'.format(deaths_total))                  # output total number of deaths
    print('Ratio: {}'.format(ratio_num))                              # output ratio of deaths to confirmed cases

run()