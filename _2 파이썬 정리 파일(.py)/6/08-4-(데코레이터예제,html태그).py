def html_tag(tag):
    def deco(func):
        def wrapper():
            return '<' + tag + '>' + func() + '</' + tag + '>'
        return wrapper
    return deco


a, b = input().split()


@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, world!'


print(hello())