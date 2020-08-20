import json


class Review:
    REVIEW_ATTR = 'body'

    def __init__(self, json_string):
        if not json_string:
            self.review_json = {}
        else:
            self.review_json = json.loads(json_string)

    def get_text(self):
        """
        get relevant text in review
        """
        if self.REVIEW_ATTR not in self.review_json:
            return None
        return self.review_json[self.REVIEW_ATTR]
