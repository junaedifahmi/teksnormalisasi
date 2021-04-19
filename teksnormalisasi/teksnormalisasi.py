from teksnormalisasi.normalization import *
from teksnormalisasi.remover import *
from teksnormalisasi.tagging import *


class Normalisasi:
    def __init__(self):
        self.rm_url = rm_url
        self.rm_email = rm_email
        self.rm_punctuation = rm_punctuation
        self.rm_username = rm_username
        self.rm_multiple_spaces = rm_multiple_spaces
        self.rm_emoji = rm_emoji
        self.normalize_reduplication = normalize_reduplication
        self.normalize_multiple_chars = normalize_multiple_chars
        self.normalize_typography = normalize_typography
        self.formalize_words = formalize_words
        self.email_to_tag = email_to_tag
        self.username_to_tag = username_to_tag
        self.url_to_tag = url_to_tag
        self.emoji_to_tag = emoji_to_tag
        self.emoji_to_emotion_word = emoji_to_emotion_word
        self.emoticon_to_tag = emoticon_to_tag
        self.emoticon_to_emotion_word = emoticon_to_emotion_word

    def optimized(self, text: str) -> str:
        text = self.rm_url(text)
        text = self.rm_email(text)
        text = self.rm_username(text)
        text = self.rm_multiple_spaces(text)
        text = self.emoji_to_tag(text)
        text = self.emoticon_to_tag(text)
        text = self.rm_punctuation(text)
        text = self.normalize_multiple_chars(text)
        text = self.normalize_reduplication(text)
        text = self.normalize_typography(text)
        text = self.formalize_words(text)
        return text
