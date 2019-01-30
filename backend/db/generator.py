from faker import Faker

brits = Faker('en_GB')
danish = Faker('dk_DK')
finnish = Faker('fi_FI')
swedish = Faker('sv_SE')
norwegian = Faker('no_NO')

def get_company(fake, index=None):
    fake.seed(index)
    name1 = fake.last_name()
    name2 = fake.last_name()
    suffix = fake.company_suffix()
    address = fake.street_address()
    postcode = fake.postcode()
    city = fake.city()

    return {
        "id": index,
        "name": '{} & {} {}'.format(name1, name2, suffix),
        "phone": fake.phone_number(),
        "website": '{}{}.{}'.format(name1, name2, fake.tld()).lower(),
        "address": ' '.join([address, postcode, city]),
        "postcode": postcode,
        "city": city,
        "country": fake.country()
    }

def get_person(fake, index=None, co_idx=None):
    company = get_company(fake, co_idx)
    fake.seed(index)
    first_name = fake.first_name()
    last_name = fake.last_name()
    username = '.'.join([first_name, last_name]).lower()

    return {
        "id": index,
        "name": ' '.join([first_name, last_name]),
        "position": fake.job(),
        "phone": fake.phone_number(),
        "email": '@'.join([username, company["website"]]),
        "company_id": co_idx
    }

print(get_company(brits, 1))
print(get_company(danish, 2))
print(get_company(finnish, 3))
print(get_company(swedish, 4))
print(get_company(norwegian, 5))

print(get_person(brits, 1, co_idx=1))
print(get_person(danish, 2, co_idx=2))
print(get_person(finnish, 3, co_idx=3))
print(get_person(swedish, 4, co_idx=4))
print(get_person(norwegian, 5, co_idx=5))