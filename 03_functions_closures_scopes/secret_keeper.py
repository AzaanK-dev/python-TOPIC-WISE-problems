# Create a function that stores a secret value. The secret must not be accessible 
# directly from outside. Only returned functions can read, modify, or reset it.


def secret_keeper():
    secret = 123456
    old = secret
    def get_secret():
        return secret
    def set_secret(new_secret):
        print("updated")
        nonlocal secret
        secret = new_secret
    def reset_secret():
        nonlocal secret
        secret = old
        return secret
    return get_secret, set_secret, reset_secret

get, set_, reset = secret_keeper()

print(get())
print(set_(654321))
print(get())
print(reset())




    

