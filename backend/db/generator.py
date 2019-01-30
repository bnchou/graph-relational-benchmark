from faker import Faker
import random
import json

country = {
    "en_GB": "United Kingdom",
    "dk_DK": "Denmark",
    "fi_FI": "Finland",
    "sv_SE": "Sweden",
    "no_NO": "Norway"
}

def get_company(fake, index=None):
    fake.seed(index)
    suffix = fake.company_suffix()
    name1 = fake.last_name()
    name2 = fake.last_name()
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
        "country": country[fake._Generator__config["locale"]]
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

def get_office(fake, index=None):
    fake.seed(index)
    address = fake.street_address()
    postcode = fake.postcode()
    city = fake.city()

    return {
        "id": index,
        "name": city,
        "phone": fake.phone_number(),
        "address": ' '.join([address, postcode, city]),
        "country": country[fake._Generator__config["locale"]]
    }

def get_coworker(fake, index=None, off_idx=None):
    fake.seed(index)
    last_name = fake.last_name()
    first_name = fake.first_name()
    username = '.'.join([first_name, last_name]).lower()
    company_domain = "lime.tech"

    return {
        "name": ' '.join([first_name, last_name]),
        "phone": fake.phone_number(),
        "email": '@'.join([username, company_domain]),
        "office_id": off_idx
    }

def unique_key(key1, key2):
    return ((key1 + key2) * (key1 + key2 + 1)) // 2 + key2

def get_deal(fake, p_idx=None, co_idx=None):
    index = unique_key(p_idx, co_idx)
    fake.seed(index)
    random.seed(index)

    return {
        "name": fake.catch_phrase(),
        "value": random.randint(50000, 1000000),
        "probability": random.random()
    }

if __name__ == "__main__":
    output = {
        "companies": [],
        "persons": [],
        "offices": [],
        "coworkers": [],
        "deals": []
    }

    for i, lang in enumerate(['en_GB','dk_DK','fi_FI','sv_SE','no_NO']):
        fake = Faker(lang)

        companies = 6
        persons = 5
        offices = 1
        coworkers = 50
        deals = 20

        for j in range(companies):
            co_idx = i * companies + j
            output["companies"].append(get_company(fake, co_idx))

            for k in range(persons):
                p_idx = co_idx * persons + k
                output["persons"].append(get_person(fake, p_idx, co_idx))

        for j in range(offices):
            off_idx = i * offices + j
            output["offices"].append(get_office(fake, off_idx))

            for k in range(coworkers):
                co_idx = off_idx * coworkers + k
                output["coworkers"].append(get_coworker(fake, co_idx, off_idx))

        random.seed(i)

        p_tot = companies * persons
        p_start = i * p_tot
        p_end = p_start + p_tot
        p_list = list(range(p_start, p_end))
        random.shuffle(p_list)

        co_tot = offices * coworkers
        co_start = i * co_tot
        co_end = co_start + co_tot
        co_list = list(range(co_start, co_end))
        random.shuffle(co_list)

        for j in range(deals):
            p_idx = p_list.pop()
            co_idx = co_list.pop()
            output["deals"].append(get_deal(fake, p_idx, co_idx))

    with open('output.json', 'w') as f_out:
        json.dump(output, f_out)