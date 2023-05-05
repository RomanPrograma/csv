import csv
user_name = input('Enter name: ')
sername = input('Enter sername: ')
age = int(input('Enter age: '))
work = input('Enter where working: ')
hobby = input('Enter hobby: ')
address = input('Enter address: ')
def saveCSV(data, filename, fields_name):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields_name)
        writer.writeheader()
        writer.writerows(data)
        file.close()
def readCSV(filename):
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row["name"], row["sername"], row['age'], row["Where working"], row['hobby'], row['Address'])
def main():
    FILENAME = "users.csv"
    users = [
        {'name': user_name, 'sername': sername, 'age': age,
        'Where working': work, 'hobby': hobby, 'Address': address}
        ]
    while True:
        print(' save - 1 : load - 2')
        action = input('action->')
        if action == '1':
            fields_name = {'name', 'sername', 'age', "Where working", 'hobby', 'Address'}
            saveCSV(users, FILENAME, fields_name)
        elif action == '2':
            readCSV(FILENAME)
        else: print('Action not found!')
main()