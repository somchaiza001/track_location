import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
import os, time, sys

time.sleep(1)
os.system('clear')
number = input('Enter your phone number: ')

time.sleep(2)
print('')
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print("Your Country: "+location)

print('')
service_pro = phonenumbers.parse(number)
service_loc = carrier.name_for_number(service_pro, "en")
print("Your Service: "+service_loc)

print('')
time_zone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(time_zone)
print("Time Zone: "+str(time))
