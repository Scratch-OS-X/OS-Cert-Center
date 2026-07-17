import re

pattern = r"^[A-Z]{3}-\d{3}-[a-z]{3}$"
admin = input("Certificat >>> ")

if re.fullmatch(pattern, admin):
  pass
else :
  pass
