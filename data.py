accounts =  [
    {"account_number": "HDFC10009234556", "balance": 500.75},
    {"account_number": "SBI00094567291", "balance": 1500.20},
    {"account_number": "YES10008282626", "balance": 250.00},
    {"account_number": "ACC10007802727", "balance": 3200.45},
    {"account_number": "KTK10098373628", "balance": 780.80}
]



# users_by_id={
#     "user_id_1":{
#         "phone":"+91 1234322221",
#         "cif":32323223,
#         "accounts":{
#             "HDFC1427987491378":{"balance":98383.63},
#             "SBI8489203884932":{"balance":683937.51}
#         }
#     },
#     "user_id_2":{
#         "phone":"+91 1876556322",
#         "cif":95857282,
#         "accounts":{
#             "PNB3877382920837":{"balance":73737.98},
#             "SBI0475985847842":{"balance":6267292.75}
#         }
#     }
# }

# cif_to_user_id={
#     32323223:"user_id_1",
#     95857282:"user_id_2"
# }

# phone_to_user_id={
#     "+91 1234322221":"user_id_1",
#    "+91 1876556322":"user_id_2"
# }

# account_to_user_id={
#     "HDFC1427987491378":"user_id_1",
#     "SBI8489203884932":"user_id_1",
#     "PNB3877382920837":"user_id_2",
#     "SBI0475985847842":"user_id_2"
# }



users="""
<users>
    <user id="user_id_1">
        <phone>+91 1234322221</phone>
        <cif>32323223</cif>
        <accounts>
            <account id="HDFC1427987491378">
                <balance>98383.63</balance>
            </account>
            <account id="SBI8489203884932">
                <balance>683937.51</balance>
            </account>
        </accounts>
    </user>
    <user id="user_id_2">
        <phone>+91 1876556322</phone>
        <cif>95857282</cif>
        <accounts>
            <account id="PNB3877382920837">
                <balance>73737.98</balance>
            </account>
            <account id="SBI0475985847842">
                <balance>6267292.75</balance>
            </account>
        </accounts>
    </user>
</users>
"""

cif_to_user_id="""
<cifToUserId>
    <cif id="32323223">user_id_1</cif>
    <cif id="95857282">user_id_2</cif>
</cifToUserId>
"""

phone_to_user_id="""
<phoneToUserId>
    <phone id="+91 1234322221">user_id_1</phone>
    <phone id="+91 1876556322">user_id_2</phone>
</phoneToUserId>
"""

account_to_user_id="""
<accountToUserId>
    <account id="HDFC1427987491378">user_id_1</account>
    <account id="SBI8489203884932">user_id_1</account>
    <account id="PNB3877382920837">user_id_2</account>
    <account id="SBI0475985847842">user_id_2</account>
</accountToUserId>
"""

# import pprint
# all_accs = []
# for usr in users_by_id:
#     ussr = users_by_id[usr]
#     all_accs.append(ussr["accounts"])
# pprint.pprint(all_accs)