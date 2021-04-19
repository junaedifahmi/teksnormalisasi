from teksnormalisasi.patterns import Patterns


def rm_url(text: str, tag="<URL>") -> str:
    text = Patterns.url.sub(tag, text)
    text = text.replace(tag, '')
    return text


def rm_username(text: str, tag='<USERNAME>') -> str:
    text = Patterns.username.sub(tag, text)
    text = text.replace(tag, '')
    return text


def rm_email(text: str, tag='<EMAIL>') -> str:
    text = Patterns.email.sub(tag, text)
    text = text.replace(tag, '')
    return text


def rm_multiple_spaces(text: str) -> str:
    return Patterns.multiplespaces.sub(' ', text)


def rm_punctuation(text: str) -> str:
    text = Patterns.punctuation.sub('', text)
    return text


def rm_emoji(text: str) -> str:
    text = Patterns.emoji_tag.sub('', text)
    return text
