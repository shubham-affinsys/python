
import jwt


# sign token with RS256 symmetric algorithm
from cryptography.hazmat.primitives import serialization


payload_data={
    "sub":"4242",
    "name":"John Doe",
    "nickname":"Doe"
}

# read or load key
private_key = open('/home/shubham/.ssh/id_rsa','r').read()
key = serialization.load_ssh_private_key(private_key.encode(),password=b'')



encoded_jwt = jwt.encode(
    payload=payload_data,
    key=key,
    algorithm="RS256"
)

#automatically get header
header_data=jwt.get_unverified_header(encoded_jwt)

print(header_data["alg"])
print(header_data)
print(encoded_jwt)

# InvalidSignature Error
# decoded_jwt = jwt.decode(encoded_jwt,key="my_super_secret",algorithms=["RS256"])
public_key = open('/home/shubham/.ssh/id_rsa.pub','r').read()
key = serialization.load_ssh_public_key(public_key.encode())


try:
    decoded_jwt = jwt.decode(
        encoded_jwt,
        key = key,
        algorithms=[header_data['alg'],]
    )
except jwt.exceptions.ExpiredSignatureError as e:
    print("token expired: ",e)

print(decoded_jwt)


#simple jwt
"""

payload_data={
    "sub":"4242",
    "name":"John Doe",
    "nickname":"Doe"
}

my_secret = "my_super_secret"

#key paramter works for either a secret or a key
# we are using secret here because  degulat encoding algo is HS256 which only require secret
# but asymetric algo like RS356 we need to use private key for signing
token = jwt.encode(
    payload = payload_data,
    key = my_secret
)

print(token)

############
import jwt

header={
    "alg":"HS256",
    "typ":"JWT"
}


#claims
# iat issued at time
payload = {
    "sub":"1234567890",
    "name":"John Doe",
    "iat": 232004
}

secret = "heisenberg"

encoded_jwt = jwt.encode(payload,secret,algorithm="HS256",headers=header)
print(encoded_jwt)


decoded_jwt = jwt.decode(encoded_jwt,secret,algorithms=["HS256"])
print(decoded_jwt)

wrong_secret="not heisenberg"

try:
    decoded_jwt = jwt.decode(encoded_jwt,wrong_secret,algorithms=["HS256"],verify=True)
    print(decoded_jwt)
except jwt.exceptions.InvalidSignatureError:
    print("Invalid signature")

"""