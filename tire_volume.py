import math
from datetime import datetime

pi = math.pi
current_date_and_time = datetime.now()

width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))
volume = (pi * (width ** 2) * aspect * (width * aspect + (2540 * diameter))) / 10000000000
print(f'The approximate volume is {volume:.2f} liters.')
buy = input('Do you want to buy tires with the dimensions you entered? (Y/N) ')
if buy.upper() == 'Y':
    phone = input('Please, type your phone number: ')
    with open('volumes.txt', 'at') as dimens_file:
        print(f'{current_date_and_time:%Y-%m-%d}, {width:.0f}, {aspect:.0f}, {diameter:.0f}, {volume:.2f}, {phone}', file = dimens_file)
        print('Done!')
else:
    print('No problem!')
    with open('volumes.txt', 'at') as dimens_file:
        print(f'{current_date_and_time:%Y-%m-%d}, {width:.0f}, {aspect:.0f}, {diameter:.0f}, {volume:.2f}', file = dimens_file)