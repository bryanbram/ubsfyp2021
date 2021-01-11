# # to get a string like this run:
# # openssl rand -hex 32
import jwt
import uuid

def token_generation(number):
    result = []
    for i in range(number):
        SECRET_KEY = str(uuid.uuid4())
        encoded_jwt = jwt.encode({"some": "payload"}, SECRET_KEY, algorithm="HS256")
        result.append(encoded_jwt)

    return result

print(token_generation(3))