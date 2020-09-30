from collections import defaultdict
from typing import Dict, List, Tuple
from unittest import TestCase

from review_lib.review import Review
from reviews_search_engine import ReviewSearchEngine
from utils.word_cleaner import WordCleaner


class ReviewsTestEngine(TestCase):

    def test_full_flow(self):
        # simply test execution flow w/o exceptions against provided data
        errors = list()
        words_to_reviews: Dict[str, List[Tuple[Review, int]]] = defaultdict(lambda: list())
        try:
            search_engine = ReviewSearchEngine()
            file_path = "../input_data/review_data.txt"
            with open(file_path) as input_file:
                lines = input_file.readlines()
                for line in lines:
                    review = Review(line)
                    search_engine.add(review)
                    words_count = defaultdict(int)
                    review_text = review.get_text()
                    review_text = review_text.strip().lower()
                    for word in review_text.split():
                        cleaned_word = WordCleaner.clean_word(word=word)
                        if not cleaned_word:
                            print(f'word before empty clean: {word}')
                            continue
                        words_count[cleaned_word] += 1
                    for word, count in words_count.items():
                        words_to_reviews[word].append((review, count))

            search_words = ["Great", "product", "love", "happy"]
            for word in search_words:
                try:
                    search_results = search_engine.search(word)
                    num_results = len(search_results)
                    results_check = words_to_reviews[word.strip().lower()]
                    results_check.sort(key=lambda res_tuple: -res_tuple[1])
                    reviews_check = [res_tuple[0].get_text() for res_tuple in results_check]
                    num_results_check = len(results_check)
                    self.assertEqual(num_results, num_results_check)
                    self.assertEqual(reviews_check, search_results)
                    print(f"{word} : {num_results} results.")
                except Exception as e:
                    errors.append(e)
            print("Most Common Words")
            most_common_list = search_engine.most_common(10)
            for word, num_results in most_common_list:
                print(f"{word} : {num_results} results")

            words_to_review_tuples = list(words_to_reviews.items())
            words_to_review_tuples.sort(key=lambda word_review_tuple: len(word_review_tuple[1]), reverse=True)
            most_10_tuples = words_to_review_tuples[:10]
            most_10_res = [(word_to_review_tuple[0], len(word_to_review_tuple[1]))
                           for word_to_review_tuple in most_10_tuples]
            print("Most Common Words check:")
            for word_to_reviews_amount in most_10_res:
                word = word_to_reviews_amount[0]
                num_results = word_to_reviews_amount[1]
                print(f"{word} : {num_results} results")
            self.assertEqual(most_10_res, most_common_list)
        except Exception as e:
            errors.append(e)
        self.assertEqual(errors, [])
