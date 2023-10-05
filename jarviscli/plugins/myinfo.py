from plugin import plugin
import csv


@plugin("myinfo")
def myinfo(jarvis, s):
    name_parameter = input("Write down your name: ")
    born_date = input("Write down your born date(YYYY/MM/DD): ")
    city_parameter = input("Write down your city's name: ")

    mydict = {
        'name_parameter': name_parameter,
        'born_date': born_date,
        'city_parameter': city_parameter,
    }
    if bool(mydict):
        print(f'New inputs are: {mydict}')
        try:
            with open('myinfo.csv', 'w') as csv_file:
                writer = csv.writer(csv_file)
                for key, value in mydict.items():
                    writer.writerow([key, value])
        except IOError:
            print("I/O error")
    else:
        print('Nothing in myinfo')
