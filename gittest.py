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
    countries = []
    regions = []
    ratio_num = []
    for row in data:
        # collect all confirmed cases from each country into a single list
        confirmed = int(row['confirmed'])
        confirmed_num.append(confirmed)

        # collect all deaths from each country into a single list
        deaths = int(row['deaths'])
        deaths_num.append(deaths)

        # collect countries into a single list
        country = row['country']
        countries.append(country)

        # collect regions into a single list
        region = row['region']
        regions.append(region)

        # collect ratio of deaths to confirmed cases into a single list
        ratio = float(int(row['deaths'])/int(row['confirmed']))
        ratio_num.append(ratio)

    # list of dictionaries
    summary = [
        {'country': countries[0], 'region': regions[0], 'confirmed': confirmed_num[0], 'deaths': deaths_num[0], 'ratio of deaths to confirmed cases': ratio_num[0]},
        {'country': countries[1], 'region': regions[1], 'confirmed': confirmed_num[1], 'deaths': deaths_num[1], 'ratio of deaths to confirmed cases': ratio_num[1]},
        {'country': countries[2], 'region': regions[2], 'confirmed': confirmed_num[2], 'deaths': deaths_num[2], 'ratio of deaths to confirmed cases': ratio_num[2]},
        {'country': countries[3], 'region': regions[3], 'confirmed': confirmed_num[3], 'deaths': deaths_num[3], 'ratio of deaths to confirmed cases': ratio_num[3]},
        {'country': countries[4], 'region': regions[4], 'confirmed': confirmed_num[4], 'deaths': deaths_num[4], 'ratio of deaths to confirmed cases': ratio_num[4]},
        {'country': countries[5], 'region': regions[5], 'confirmed': confirmed_num[5], 'deaths': deaths_num[5], 'ratio of deaths to confirmed cases': ratio_num[5]},
        {'country': countries[6], 'region': regions[6], 'confirmed': confirmed_num[6], 'deaths': deaths_num[6], 'ratio of deaths to confirmed cases': ratio_num[6]},
        {'country': countries[7], 'region': regions[7], 'confirmed': confirmed_num[7], 'deaths': deaths_num[7], 'ratio of deaths to confirmed cases': ratio_num[7]},
        {'country': countries[8], 'region': regions[8], 'confirmed': confirmed_num[8], 'deaths': deaths_num[8], 'ratio of deaths to confirmed cases': ratio_num[8]},
        {'country': countries[9], 'region': regions[9], 'confirmed': confirmed_num[9], 'deaths': deaths_num[9], 'ratio of deaths to confirmed cases': ratio_num[9]},
        {'country': countries[10], 'region': regions[10], 'confirmed': confirmed_num[10], 'deaths': deaths_num[10], 'ratio of deaths to confirmed cases': ratio_num[10]},
        {'country': countries[11], 'region': regions[11], 'confirmed': confirmed_num[11], 'deaths': deaths_num[11], 'ratio of deaths to confirmed cases': ratio_num[11]},
        {'country': countries[12], 'region': regions[12], 'confirmed': confirmed_num[12], 'deaths': deaths_num[12], 'ratio of deaths to confirmed cases': ratio_num[12]},
        {'country': countries[13], 'region': regions[13], 'confirmed': confirmed_num[13], 'deaths': deaths_num[13], 'ratio of deaths to confirmed cases': ratio_num[13]},
        {'country': countries[14], 'region': regions[14], 'confirmed': confirmed_num[14], 'deaths': deaths_num[14], 'ratio of deaths to confirmed cases': ratio_num[14]},
    ]

    print("------------------SUMMARY-------------------")

    for each in summary:
        print('country: {}'.format(each['country']))
        print('region: {}'.format(each['region']))
        print('confirmed cases: {:,}'.format(each['confirmed']))
        print('deaths: {:,}'.format(each['deaths']))
        print('ratio of deaths to confirmed cases: {:.3f}'.format(each['ratio of deaths to confirmed cases']))
        print("-------------------------------------------")

    confirmed_total = sum(confirmed_num)
    deaths_total = sum(deaths_num)
    average = int(sum(confirmed_num) / len(confirmed_num))
    highest = max(summary, key=lambda x:x['confirmed'])
    lowest = min(summary, key=lambda x:x['confirmed'])
    print("STATISTICS")
    print('Total confirmed cases: {:,}'.format(confirmed_total))      # output total number of confirmed cases
    print('Total deaths: {:,}'.format(deaths_total))                  # output total number of deaths
    print('Average number of confirmed cases: {:,}'.format(average))  # output average number of confirmed cases
    print('Most confirmed cases: {}'.format(highest))                 # highest number of confirmed cases
    print('Least confirmed cases: {}'.format(lowest))                 # lowest number of confirmed cases
    print("-------------------------------------------")

run()