from unittest import TestCase

from review_lib.review import Review


class TestReview(TestCase):

    def test_none(self):
        self._test(review_json=None, expected_res=None)

    def test_empty(self):
        self._test(review_json='', expected_res=None)

    def test_no_body(self):
        review_json = '{"a":"a"}'
        self._test(review_json=review_json, expected_res=None)

    def test_full_body(self):
        review_json = '{"crawl_date": "2019-02-14", "is_verified_product": true, "weight": "7.68 pounds", "product_source_url": "https://www.amazon.com/Method-Mens-Cedar-Cypress-Count/dp/B078XXG7BR/ref=sr_1_184_s_it/133-3778610-5810326", "brand_name": "Method", "currency": "USD", "rate": 5.0, "filters": {"Scent Name": "Sea + Surf"}, "recommendation": [{"amazon_id": "B078XYRNCB"}, {"amazon_id": "B078Y3J6BC"}], "asin": "B078XXG7BR", "is_promoted": false, "dimensions": "7.2 x 6.1 x 8.5 inches", "total_number_of_pages": 3, "title": "Good stuff!", "model_number": "10817939018610", "source": "amazon", "page_number": 1, "type": "review", "product_name": "Method Mens Body Wash, Sea + Surf, 6 Count", "review_source_url": "https://www.amazon.com/product-reviews/B078XXG7BR/ref=cm_cr_dp_see_all_btm", "body": "Love the smell and the \u201cmanly looking\u201d bottle. Hard to please boyfriend actually requested that I purchase more. He\u2019s super picky about texture and scent so this stuff must be right on!", "price": "40.34", "collection_key": "0625ab8327a1c523", "date": "2019-02-08 00:00:00", "product_id": "B078XXG7BR", "url": "https://www.amazon.com/s/ref=sr_in_t_p_89_30?fst=as%3aoff&rh=n%3a3760911%2cn%3a%2111055981%2cn%3a11060451%2cn%3a11060521%2cn%3a11056281%2cn%3a11056291%2cp_89%3aalba+botanica%7caveeno%7cburt%27s+bees%7ccetaphil%7ccerave%7cdove%7cdr.+bronner%27s%7chempz%7cl%27occitane%7cmario+badescu%7cmurad%7cneutrogena%7cavon%7cnip%2bfab%7cnivea%7cogx%7colay%7corigins%7cout+of+africa%7cpacifica%7cpalmer%27s%7cpeter+thomas+roth%7cphilosophy%7cskinfix%7cshea+moisture%7csoap+%26+glory%7cst.+ives%7csuave%7ctree+hut%7culta%7cyes+to%7cyes+to+carrots%7cyes+to+blueberries%7cyes+to+coconut%7cyes+to+grapefruit%7cyes+to+tomatoes%7cvictoria%27s+secret%7cvichy%7cahava%7cdial%7caxe%7cbath+%26+body+works%7cbabo+botanicals%7ccaress%7cdr.+teal%27s%7cirish+spring%7cle+petit+marseillais%7civory%7cold+spice%7cmethod%7csoftsoap%7ctone%7czest%7czoella+beauty%7cvitabath%7cclinique%7cdermalogica%7ceucerin%7cthe+body+shop&bbn=11056291&ie=utf8&qid=1510073872&rnid=2528832011", "review_url": "https://www.amazon.com/gp/customer-reviews/RXD2HFAO65VPE/ref=cm_cr_arp_d_rvw_ttl", "author": "Christy", "crawler_name": "c64b82d3-4144-11e8-b4ce-e6dd0c049267_21ce5049-4dfc-11e8-a577-e1d7c086027d_JnJ_body_care_amz", "product_image": "https://images-na.ssl-images-amazon.com/images/I/51Kgv3EaqxL._SY450_.jpg"}'
        expected_res = "Love the smell and the \u201cmanly looking\u201d bottle. Hard to please boyfriend actually requested that I purchase more. He\u2019s super picky about texture and scent so this stuff must be right on!"
        self._test(review_json=review_json, expected_res=expected_res)

    def _test(self, review_json, expected_res):
        review = Review(json_string=review_json)
        review_txt = review.get_text()
        self.assertEqual(review_txt, expected_res, f'expected:{expected_res}, got:{review_txt}')
