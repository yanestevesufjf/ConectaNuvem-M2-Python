class English():
    def hello():
        print('Hello')

class Portuguese():
    def hello():
        print('Olá')


class Bilingual(English, Portuguese):
    pass

Bilingual.hello()