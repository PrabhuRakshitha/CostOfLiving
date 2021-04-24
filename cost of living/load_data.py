import json
import matplotlib.pyplot as plt

class City:
    def __init__(self, name):
        self.city_name = name
        self.city_col = {}

    def set_city_data(self, item_desc, value):
        self.city_col[item_desc] = value

    def print_city_del(self):

        print('City :',self.city_name)
        print("City Details :", self.city_col)

    def get_details(self, yvalue):
        name = self.city_name
        try:
            value = self.city_col[yvalue]
            value = float(value.replace(',', ''))
        except KeyError:
            return -1, -1

        return name , value


class Country:
    def __init__(self, name):
        self.country_name = name
        self.city_list = {}

    def set_col(self, data):
        if not data['city'] in self.city_list:
            city = City(data['city'])
            self.city_list[data['city']] = city
        self.city_list[data['city']].set_city_data(data['item_desc'], data['value'])

    def print_details(self):
        print('country :',self.country_name)
        for x in self.city_list:
            self.city_list[x].print_city_del()

    def plot_data(self,yvalue):
        label = "COL for cities in " + self.country_name
        x = []
        y = []
        for city in self.city_list:
            name, value = self.city_list[city].get_details(yvalue)
            if value > 0:
                x.append(name)
                y.append(value)
        return label , x ,y





def find_country(cntry_name, cntry_list):
    for country in cntry_list:
        if cntry_name == country.country_name:
            return country


def main():
    cntry_list = []

    with open('COL_data.json', 'r') as f:
        data = json.load(f)
        for item in data:
            cntry_data = find_country(item['country'], cntry_list)
            if not cntry_data:
                cntry_data = Country(item['country'])
                cntry_list.append(cntry_data)
            cntry_data.set_col(item)

    for country in cntry_list:
        country.print_details()

    f.close()
    yvalue = { 1:'Meal, Inexpensive Restaurant',
              2:'Gasoline (1 gallon)',
              3:'Taxi 1 mile (Normal Tariff)' ,
              4:'Basic (Electricity, Heating, Cooling, Water, Garbage) for 915 sq ft Apartment',
              5:'1 min. of Prepaid Mobile Tariff Local (No Discounts or Plans)',
              6:'Internet (60 Mbps or More, Unlimited Data, Cable/ADSL)',
              7:'Apartment (1 bedroom) in City Centre',
              8:'Price per Square Feet to Buy Apartment in City Centre',
              9:'International Primary School, Yearly for 1 Child'}

    print('Below is the list of indicators to determine Cost of living')
    print('1:Meal, Inexpensive Restaurant')
    print('2:Gasoline (1 gallon)')
    print('3:Taxi 1 mile (Normal Tariff)')
    print('4:Basic (Electricity, Heating, Cooling, Water, Garbage) for 915 sq ft Apartment')
    print('5:1 min. of Prepaid Mobile Tariff Local (No Discounts or Plans)')
    print('6:Internet (60 Mbps or More, Unlimited Data, Cable/ADSL)')
    print('7:Apartment (1 bedroom) in City Centre')
    print('8:Price per Square Feet to Buy Apartment in City Centre')
    print('9:International Primary School, Yearly for 1 Child')
    option = input('Please select one option from above ')
    option =int(option)

    for country in cntry_list:
        label, x, y = country.plot_data(yvalue[option])
        plt.plot(x, y, color='green', linestyle='dashed', linewidth=3,
                 marker='o', markerfacecolor='blue', markersize=5)
        plt.xticks(rotation=90)
        plt.xlabel('Cities')
        plt.ylabel(yvalue[option])
        plt.title(label)
        plt.show()

main()


