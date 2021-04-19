import unittest

from teksnormalisasi.teksnormalisasi import Normalisasi

normalizer = Normalisasi()


class Testing(unittest.TestCase):
    def test_rm_punctuation(self):
        text = "mau kemana? zxcvbnm,./asdfghjkl;'qwertyuiop[]"
        hyp = normalizer.rm_punctuation(text)
        ref = "mau kemana zxcvbnmasdfghjklqwertyuiop"
        self.assertEqual(hyp, ref)

    def test_formalized(self):
        hyp = normalizer.formalize_words("kenapa gak bilang ke aku?")
        ref = "mengapa tidak bicara ke aku?"
        self.assertEqual(text, ref)


if __name__ == '__main__':
    unittest.main()
