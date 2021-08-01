# Change audio output
# Cooper 8/1/2021
# https://nircmd.nirsoft.net/
from os import system

command = 'nircmd.exe setdefaultsounddevice'
device1 = 'Internal AUX Jack'
device2 = 'USB-C Speakers'

with open('currentdevice.txt', 'r+') as file:
    current_device = file.read()
    file.seek(0)
    if current_device == device1:
        system(f'{command} "{device2}"')
        file.write(device2)
    elif current_device == device2:
        system(f'{command} "{device1}"')
        file.write(device1)
    else:
        raise Exception('Wrong device selected')

    file.truncate()
