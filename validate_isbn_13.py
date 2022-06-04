from faker import Faker
from re import fullmatch
fake = Faker()
iteration = 1000000
matches = 0
for i in range(iteration):
    isbn = fake.isbn13()
    match = fullmatch(r'97[8-9][-]\d{1,5}[-]\d{1,7}[-]\d{1,6}[-][0-9X]', isbn)
    if match:
        matches+=1
print(f'numbers = {iteration}, \n'
      f'matches = {matches} ')