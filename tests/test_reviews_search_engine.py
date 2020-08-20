from unittest import TestCase

from review_lib.review import Review
from reviews_search_engine import ReviewSearchEngine


class ReviewsTestEngine(TestCase):

    def test_full_flow(self):
        # simply test execution flow w/o exceptions against provided data
        errors = list()
        try:
            search_engine = ReviewSearchEngine()
            file_path = "../input_data/review_data.txt"
            with open(file_path) as input_file:
                lines = input_file.readlines()
                for line in lines:
                    review = Review(line)
                    search_engine.add(review)

            search_words = ["Great", "product", "love", "happy"]
            for word in search_words:
                try:
                    num_results = len(search_engine.search(word))
                    print(f"{word} : {num_results} results.")
                except Exception as e:
                    errors.append(e)
            print("Most Common Words")
            for word, num_results in search_engine.most_common(10):
                print(f"{word} : {num_results} results")
        except Exception as e:
            errors.append(e)
        self.assertEqual(errors, [])
