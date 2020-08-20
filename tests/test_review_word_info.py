from typing import List, Tuple, Optional
from unittest import TestCase

from review_lib.review import Review
from review_lib.review_word_info import ReviewWordInfo


class TestReviewWordInfo(TestCase):

    def test_empty(self):
        self._test(word='', reviews=[], expected_res=[], n=1)

    def test_one_review_n_0(self):
        review_json = '{"body": "great product"}'
        review = Review(json_string=review_json)
        word = 'great'
        self._test(word=word, reviews=[(review, 1)], expected_res=[], n=0)

    def test_one_review_n_1(self):
        review_json = '{"body": "great product"}'
        review = Review(json_string=review_json)
        word = 'great'
        self._test(word=word, reviews=[(review, 1)], expected_res=[review], n=1)

    def test_one_review_no_n(self):
        review_json = '{"body": "great product"}'
        review = Review(json_string=review_json)
        word = 'great'
        self._test(word=word, reviews=[(review, 1)], expected_res=[review], n=None)

    def test_one_review_n_big(self):
        review_json = '{"body": "great product"}'
        review = Review(json_string=review_json)
        word = 'great'
        self._test(word=word, reviews=[(review, 1)], expected_res=[review], n=1000)

    def test_multiple_reviews_n_0(self):
        review_json_1 = '{"body": "great product"}'
        review_json_2 = '{"body": "excellent product product"}'
        review_json_3 = '{"body": "excellent product not like other product and extra product"}'
        review_1 = Review(json_string=review_json_1)
        review_2 = Review(json_string=review_json_2)
        review_3 = Review(json_string=review_json_3)
        reviews = [(review_1, 1), (review_2, 2), (review_3, 3)]
        word = 'product'
        self._test(word=word, reviews=reviews, expected_res=[], n=0)

    def test_multiple_reviews_n_1(self):
        review_json_1 = '{"body": "great product"}'
        review_json_2 = '{"body": "excellent product product"}'
        review_json_3 = '{"body": "excellent product not like other product and extra product"}'
        review_1 = Review(json_string=review_json_1)
        review_2 = Review(json_string=review_json_2)
        review_3 = Review(json_string=review_json_3)
        reviews = [(review_1, 1), (review_2, 2), (review_3, 3)]
        word = 'product'
        self._test(word=word, reviews=reviews, expected_res=[review_3], n=1)

    def test_multiple_reviews_no_n(self):
        review_json_1 = '{"body": "great product"}'
        review_json_2 = '{"body": "excellent product product"}'
        review_json_3 = '{"body": "excellent product not like other product and extra product"}'
        review_1 = Review(json_string=review_json_1)
        review_2 = Review(json_string=review_json_2)
        review_3 = Review(json_string=review_json_3)
        reviews = [(review_1, 1), (review_2, 2), (review_3, 3)]
        word = 'product'
        self._test(word=word, reviews=reviews, expected_res=[review_3, review_2, review_1], n=None)

    def test_multiple_reviews_n_big(self):
        review_json_1 = '{"body": "great product"}'
        review_json_2 = '{"body": "excellent product product"}'
        review_json_3 = '{"body": "excellent product not like other product and extra product"}'
        review_1 = Review(json_string=review_json_1)
        review_2 = Review(json_string=review_json_2)
        review_3 = Review(json_string=review_json_3)
        reviews = [(review_1, 1), (review_2, 2), (review_3, 3)]
        word = 'product'
        self._test(word=word, reviews=reviews, expected_res=[review_3, review_2, review_1], n=1000)

    def _test(self, word: str, reviews: List[Tuple[Review, int]], expected_res: List[Review], n: Optional[int]):
        review_word_info = ReviewWordInfo()
        review_word_info.set_word(word)
        for review_data in reviews:
            review_word_info.add_review(review=review_data[0], count=review_data[1])
        top_reviews = review_word_info.get_top_reviews(n=n)
        self.assertEqual(top_reviews, expected_res, f'expected:{expected_res}, got:{top_reviews}')
