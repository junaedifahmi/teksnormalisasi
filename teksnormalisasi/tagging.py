import pickle
import pkg_resources

from teksnormalisasi.patterns import Patterns
from emoji import demojize


emoticon_path = pkg_resources.resource_filename('teksnormalisasi', 'dictionaries/emoticon.dict')
with open(emoticon_path, 'rb') as f:
    emoticon = pickle.load(f)


def email_to_tag(text: str, tag="<EMAIL>") -> str:
    text = Patterns.email.sub(tag, text)
    return text


def username_to_tag(text: str, tag="<USERNAME>") -> str:
    text = Patterns.username.sub(tag, text)
    return text


def url_to_tag(text: str, tag="<URL>") -> str:
    text = Patterns.url.sub(tag, text)
    return text


def emoji_to_tag(text: str, tag="<EMOJI>") -> str:
    text = demojize(text)
    text = Patterns.emoji_tag.sub(tag, text)
    return text


def emoji_to_emotion_word(text: str) -> str:
    # TODO: create emoticon to emotion word
    raise NotImplemented


def emoticon_to_tag(text: str, tag="<EMOTICON>") -> str:
    text = [emoticon[word] if word in emoticon.keys() else word for word in text.split()]
    return ' '.join(text)


def emoticon_to_emotion_word(text: str) -> str:
    raise NotImplemented
