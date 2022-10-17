import pyjokes


def tell_some_jokes():
    jokes=pyjokes.get_joke()
    print(jokes)

tell_some_jokes()

