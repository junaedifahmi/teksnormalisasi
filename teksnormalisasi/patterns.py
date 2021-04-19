import re


class Patterns:
    # online docs specifics
    email = re.compile(r'[\w\.-]+@[\w\.-]+\.\w+')
    url = re.compile(r'http(s)?//[\w-]+\.[\w+]')

    # twitter specific
    username = re.compile(r'@[\w_]+')
    hashtag = re.compile(r'#[\w_]+')

    # non words related
    multiplespaces = re.compile(r'\s+')
    multiplechars = re.compile(r'(.)\1{2,}')
    punctuation = re.compile(r'[^\w\s]')
    emoji_tag = re.compile(r':[a-z_]+:')

    # words form related
    reduplication = re.compile(r'([a-zA-Z]+)([0-9])')

