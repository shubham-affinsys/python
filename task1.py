"""
tasks: 
1. a key and dict as input dict can be super nested
    value of key for every occurence
    multiple return values

"""
import pprint

data=[{
    "a":{
        "b":{
            "c":"c end"
        },
        "a":{
            "c":"occ1",
            "d":"obj2",
            "k":{
                "a":"end of dict"
            }
        }
    }
},
{
    "a":{
            "c":"occ1",
            "d":"obj2",
            "k":{
                "a":"end of dict",
                "k":{
                    "b":{
            "c":"c end"
        },
        "a":{
            "c":"occ1",
            "d":"obj2",
            "k":{
                "a":"end of dict"
            }
        }
                }
            }
        }
}

]

def give_all_occurences(key,data):
    if isinstance(data,dict):
        for k in data:
            if k==key:
                pprint.pprint(data[k])
            give_all_occurences(key,data[k])
        return
    elif isinstance(data,list):
        for i in data:
            give_all_occurences(key,i)
    if data==key:
        pprint(data)

give_all_occurences("a",data)