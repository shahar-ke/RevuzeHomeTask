from unittest import TestCase

from utils.word_cleaner import WordCleaner


class TestWordCleaner(TestCase):

    def test_none(self):
        self._test(input_word=None, expected_word=None)

    def test_simple(self):
        word = 'simple'
        self._test(input_word=word, expected_word=word)

    def test_prefix_one_char(self):
        input_word = ',simple'
        expected_word = 'simple'
        self._test(input_word=input_word, expected_word=expected_word)

    def test_postfix_one_char(self):
        word = 'simple;'
        expected_word = 'simple'
        self._test(input_word=word, expected_word=expected_word)

    def test_complex(self):
        word = ',<>1simple1?!#'
        expected_word = '1simple1'
        self._test(input_word=word, expected_word=expected_word)

    def test_unicode(self):
        word = '\u201cmanly\u201d'
        expected_word = 'manly'
        self._test(input_word=word, expected_word=expected_word)

    def test_word_with_none_alpha_in_middle(self):
        word = ":I'm;"
        expected_word = "i'm"
        self._test(input_word=word, expected_word=expected_word)

    def _test(self, input_word=None, expected_word=None):
        cleaned_word = WordCleaner.clean_word(input_word)
        self.assertEqual(cleaned_word, expected_word,
                         f'input:{input_word}, expected: {expected_word}, got: {cleaned_word}')
