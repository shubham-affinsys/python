import requests
import translator
import re

pattern = r'^[a-zA-Z0-9\s.,?!\'"-]+$'
def get_cat_fact(count):
    url=f"https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount={count}"
    response = requests.get(url)

    if response.status_code==200:
        data = response.json()
        ls=[]
        for fact in data:
            fact_is = fact['text']
            if re.fullmatch(pattern, fact_is):
                ls.append(fact_is)
            else:
                transalated = translator.translate_to_eng(fact_is)
                ls.append(transalated)
            # ls.append(fact_is)
        return ls
    else:
        return f"Error : {response.status_code}"


def gen_cat_fact(count):
    try:
        cat_fact = get_cat_fact(count)
        if isinstance(cat_fact,str):
            print(cat_fact)
        else:
            for fact in cat_fact:
                print(fact)
    except:
        print("check api")

count=10
gen_cat_fact(count)