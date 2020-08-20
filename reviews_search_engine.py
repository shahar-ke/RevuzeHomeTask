import itertools
from collections import defaultdict
from typing import List, Tuple, Dict

from review_lib.review import Review
from review_lib.review_word_info import ReviewWordInfo
from utils.word_cleaner import WordCleaner


class ReviewSearchEngine:

    def __init__(self):
        self.words_info: Dict[str, ReviewWordInfo] = defaultdict(ReviewWordInfo)

    def add(self, review: Review) -> None:
        """
        adds a review to search engine DB
        :param review: the review to add
        :return:
        """
        if review is None:
            return
        review_text = review.get_text()
        review_text = review_text.strip().lower()
        review_text_words = review_text.split()
        word_count: Dict[str, int] = defaultdict(int)
        for word in review_text_words:
            # word is already lower case
            word = WordCleaner.clean_word(word, to_lower=False)
            if not word:
                continue
            word_count[word] += 1
        for word, count in word_count.items():
            word_info = self.words_info[word]
            word_info.set_word(word=word)
            word_info.add_review(review=review, count=count)

    def search(self, word: str, n: int = None) -> List[str]:
        """
        search reviews by input word, case insensitive
        :param word: string containing single word
        :param n: optional, number of top matches to return
        :return: list of matching Reviews, sorted by number of appearances of word in the review text
        """
        if n is not None and n <= 0:
            return []
        word = WordCleaner.clean_word(word)
        if word not in self.words_info:
            return []
        review_word_info: ReviewWordInfo = self.words_info[word]
        top_reviews: List[Review] = review_word_info.get_top_reviews(n)
        return [review.get_text() for review in top_reviews]

    def most_common(self, n: int) -> List[Tuple[str, int]]:
        """
        return list of n most common words and the number of reviews they appeared in (each word is counted only once per review)
        :param n: length of list to return
        :return: list of tuples (word, n_reviews_appeared_in) sorted by n_reviews_appeared_in (desceding)
        """
        if n is None or n <= 0:
            return []
        # noinspection PyTypeChecker
        ordered_words_info = \
            sorted(self.words_info.items(), key=lambda words_info_item: words_info_item[1], reverse=True)
        top_reviews = itertools.islice(ordered_words_info, n)
        tuple_list: List[Tuple[str, int]] = [(top_review[0], len(top_review[1])) for top_review in top_reviews]
        return tuple_list


def main():
    search_engine = ReviewSearchEngine()

    file_path = "input_data/review_data.txt"
    with open(file_path) as input_file:
        lines = input_file.readlines()
        for line in lines:
            review = Review(line)
            search_engine.add(review)

    search_words = ["Great", "product", "love", "happy"]
    for word in search_words:
        num_results = len(search_engine.search(word))
        print(f"{word} : {num_results} results.")

    print("Most Common Words")
    for word, num_results in search_engine.most_common(10):
        print(f"{word} : {num_results} results")


if __name__ == '__main__':
    main()
