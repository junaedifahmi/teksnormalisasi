from teksnormalisasi.normalization import *
from teksnormalisasi.remover import *
from teksnormalisasi.tagging import *


def optimize(text: str) -> str:
    text = rm_url(text)
    text = rm_email(text)
    text = rm_username(text)
    text = rm_multiple_spaces(text)
    text = emoji_to_tag(text)
    text = emoticon_to_tag(text)
    text = rm_punctuation(text)
    text = normalize_multiple_chars(text)
    text = normalize_reduplication(text)
    text = normalize_typography(text)
    text = formalize_words(text)
    return text


__all__ = [
    optimize,
    rm_url,
    rm_email,
    rm_punctuation,
    rm_username,
    rm_multiple_spaces,
    rm_emoji,
    normalize_reduplication,
    normalize_multiple_chars,
    normalize_typography,
    formalize_words,
    email_to_tag,
    username_to_tag,
    url_to_tag,
    emoji_to_tag,
    emoji_to_emotion_word,
    emoticon_to_tag,
    emoticon_to_emotion_word
]
