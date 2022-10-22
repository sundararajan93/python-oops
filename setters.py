class Token:

    def __init__(self, token):
        self._token = token

    def get_token(self):
        return self._token

    def set_token(self, new_token):
        if isinstance(new_token, int):
            self._token = new_token
        else:
            print("Enter valid Token format!!!")

my_token = Token(1234)

print("My Token is", my_token.get_token())

my_token.set_token("Testing")

print("My New Token is", my_token.get_token())

