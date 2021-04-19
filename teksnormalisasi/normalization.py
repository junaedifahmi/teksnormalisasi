import pickle
import pkg_resources

from teksnormalisasi.patterns import Patterns


formal_path = pkg_resources.resource_filename('teksnormalisasi', 'dictionaries/formal.dict')
normal_path = pkg_resources.resource_filename('teksnormalisasi', 'dictionaries/normal.dict')


with open(formal_path, 'rb') as f:
    formal = pickle.load(f)

with open(normal_path, 'rb') as f:
    normal = pickle.load(f)


def normalize_multiple_chars(text: str) -> str:
    """
    normalize multiple char into two chars
    >>> normalize_multiple_chars("maaf kan aku")
    maaf kan aku
    >>> normalize_multiple_chars("sayaaaaang kamu")
    sayang kamu
    """
    return Patterns.multiplechars.sub(r'\1', text)


def normalize_typography(text: str) -> str:
    """
    normalize typography from a given dict
    >>> normalize_typography("bsk kita makan-makan ya")
    besok kita makan-makan ya
    >>> normalize_typography("kpn mau dtg ke rmh ketemu ortu ku?")
    kapan mau datang ke rumah bertemu orang tua ku?
    """
    teks = [normal[word] if word in normal.keys() else word for word in text.split()]
    return ' '.join(teks)


def formalize_words(text: str) -> str:
    """
    to formal form of the word
    >>> formalize_words("kenapa gak bilang ke aku?")
    mengapa tidak bicara ke aku?
    """
    teks = [formal[word] if word in formal.keys() else word for word in text.split()]
    return ' '.join(teks)


def normalize_reduplication(text: str) -> str:
    """
    change reduplication abbv to its normal form
    >>> normalize_typography("kpn2 kita main2 lagi ya")
    kpn kpn kita main main lagi ya
    """
    for word, times in Patterns.reduplication.findall(text):
        repl = (word+' ')*int(times)
        text = text.replace(word+times, repl.strip())
    return text
