import random

from data.data import Person
from faker import Faker

faker_en = Faker('En')

def generate_person():
    return Person(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email(),
        address=faker_en.address(),
        mobile= f"{(random.randint(1000000000, 9999999999))}"
    )