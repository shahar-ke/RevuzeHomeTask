class WordCleaner:

    @classmethod
    def clean_word(cls, word: str, to_lower: bool = True) -> str:
        if word is None:
            return None
        if to_lower:
            word = word.lower()
        start_index = 0
        end_index = len(word) - 1
        for start_index in range(len(word)):
            if word[start_index].isalnum():
                break
        for end_index in reversed(range(len(word))):
            if word[end_index].isalnum():
                break
        cleaned_word = word[start_index: end_index+1]
        return cleaned_word
