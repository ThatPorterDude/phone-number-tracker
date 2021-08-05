import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNo = input("Enter the phone number with country code: ")
mobileNo = phonenumbers.parse(mobileNo)

# Getting the timezone of the phone number
print(timezone.time_zones_for_number(mobileNo))

# Getting the carrier of the phone number
print(carrier.name_for_number(mobileNo, "en"))

# Getting region info
print(geocoder.description_for_number(mobileNo, "en"))

# Validating & Checking the possibility of the phone number
print("Phone number is valid:",phonenumbers.is_valid_number(mobileNo))
print("Phone number is possible:",phonenumbers.is_possible_number(mobileNo))