from typing import List, Tuple

from review_lib.review import Review


class ReviewWordInfo:

    def __init__(self):
        self._sorted = False
        self._reviews: List[Tuple[Review, int]] = list()
        self._sorted_reviews: List = list()
        self._word: str = ''

    def __len__(self):
        return len(self._reviews)

    def __gt__(self, other):
        return len(self) > len(other)

    def set_word(self, word):
        self._word = word

    def add_review(self, review: Review, count: int):
        self._reviews.append((review, count))
        self._sorted = False

    def get_top_reviews(self, n: int = None) -> List[Review]:
        if not self._sorted:
            self._sort()
        if n is None:
            n = len(self._reviews)
        if n <= 0:
            return []
        n = min(len(self._reviews), n)
        top_reviews_tuples = self._reviews[:n]
        top_reviews = [review[0] for review in top_reviews_tuples]
        return top_reviews

    def _sort(self):
        self._reviews.sort(key=lambda review_tuple: -review_tuple[1])
        self._sorted = True

