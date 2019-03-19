from faker import Faker
import random
import json
import sys


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
        "city": city
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
        "phone": fake.phone_number(),
        "position": fake.job(),
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
        "address": ' '.join([address, postcode, city])
    }


def get_coworker(fake, index=None, off_idx=None):
    fake.seed(index)
    last_name = fake.last_name()
    first_name = fake.first_name()
    username = '.'.join([first_name, last_name]).lower()
    company_domain = "lime.tech"

    return {
        "id": index,
        "name": ' '.join([first_name, last_name]),
        "phone": fake.phone_number(),
        "email": '@'.join([username, company_domain]),
        "office_id": off_idx
    }


def get_deal(fake, index=None, p_idx=None, co_idx=None):
    fake.seed(index)

    return {
        "id": index,
        "name": fake.catch_phrase(),
        "value": random.randint(50000, 1000000),
        "probability": random.random(),
        "person_id": p_idx,
        "coworker_id": co_idx
    }


def get_document(fake, index=None, p_idx=None, d_idx=None):
    fake.seed(index)
    date = fake.date(pattern="%y%m%d")
    domain = fake.domain_word()
    ext = fake.file_extension()

    return {
        "id": index,
        "description": '{}{}.{}'.format(domain, date, ext),
        "type": ext,
        "deal_id": d_idx,
        "person_id": p_idx
    }


def get_history(fake, index=None, p_idx=None, co_idx=None, d_idx=None, doc_idx=None):
    fake.seed(index)
    random.seed(index)

    return {
        "id": index,
        "type": random.choice(["Comment", "Visit", "Email", "Call"]),
        "date": fake.date(pattern="%Y-%m-%d"),
        "notes": fake.paragraph(),
        "person_id": p_idx,
        "coworker_id": co_idx,
        "deal_id": d_idx,
        "document_id": doc_idx
    }


def get_relationship(fake, index=None, p1_idx=None, p2_idx=None):
    random.seed(index)

    return {
        "id": index,
        "type": random.choice(["Knows", "Married", "Met", "Colleague", "Family"]),
        "from_person_id": p1_idx,
        "to_person_id": p2_idx
    }

# - Large size DB -
# companies=10000,
# persons=100000,
# offices=10,
# coworkers=500,
# deals=50000,
# documents=300000,
# histories=3000000


def generate(filename="output.json",
             companies=10000,
             persons=100000,
             offices=10,
             coworkers=500,
             deals=1000,
             documents=30000,
             histories=300000,
             relationships=300000):
    # random.seed(1234)
    fake = Faker()
    output = {
        "companies": [],
        "persons": [],
        "offices": [],
        "coworkers": [],
        "deals": [],
        "documents": [],
        "histories": [],
        "relationships": []
    }

    for i in range(companies):
        output["companies"].append(get_company(fake, i))

    for i in range(persons):
        c_idx = random.randint(0, companies - 1)
        output["persons"].append(get_person(fake, i, c_idx))

    for i in range(offices):
        output["offices"].append(get_office(fake, i))

    for i in range(coworkers):
        o_idx = random.randint(0, offices - 1)
        output["coworkers"].append(get_coworker(fake, i, o_idx))

    for i in range(deals):
        p_idx = random.randint(0, persons - 1)
        c_idx = random.randint(0, coworkers - 1)
        output["deals"].append(get_deal(fake, i, p_idx, c_idx))

    for i in range(documents):
        d_idx = random.randint(0, deals - 1)
        deal = output["deals"][d_idx]
        p_idx = deal["person_id"]
        output["documents"].append(
            get_document(fake, i, p_idx, d_idx))

    for i in range(histories):
        doc_idx = random.randint(0, documents - 1)
        document = output["documents"][doc_idx]
        d_idx = document["deal_id"]
        deal = output["deals"][d_idx]
        p_idx = deal["person_id"]
        c_idx = deal["coworker_id"]
        output["histories"].append(get_history(
            fake, i, p_idx, c_idx, d_idx, doc_idx))

    for i in range(relationships):
        [p1_idx, p2_idx] = random.sample(range(0, persons), 2)
        output["relationships"].append(
            get_relationship(fake, i, p1_idx, p2_idx))

    with open(filename, 'w') as f_out:
        json.dump(output, f_out)


if __name__ == "__main__":
    if(len(sys.argv) > 1):
        generate(sys.argv[1])
    else:
        generate()
