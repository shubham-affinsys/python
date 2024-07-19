import requests

def get_cat_fact(count):
    url=f"https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount={count}"
    response = requests.get(url)

    if response.status_code==200:
        data = response.json()
        ls=[]
        for fact in data:
            ls.append(fact['text'])
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