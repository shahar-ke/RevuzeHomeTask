# RevuzeHomeTask
## Revuze home task


### solution explained:

when a Review is added to ReviewSearchEngine, the review text is fetched, switched to lower case, and split to words

each word is cleaned for none alpha numeric characters on its edges, and a counter keeps info about amount of appearances for the specific word in the specific review

WordCleaner util is used for word cleanup


ReviewSearchEngine maps each word with a ReviewWordInfo instance that maintains 
per each clean word info about reviews it is associated with and amount of appearances in each review 

upon search, the word correspondent ReviewWordInfo id fetched which implements get_top_reviews(self, n: int = None) that returns the list of reviews by requested order

its worth noting that ReviewWordInfo sorts its data only if and when needed


ReviewWordInfo implements __gt__ based on amount of reviews associated with a given word

this fact is useful for ReviewSearchEngine.most_common which which calls sort on its internal ds by ReviewWordInfo (reverse order)   


### complexity:


Review.__init__: constant time

Review.get_text(self): constant time
 
ReviewSearchEngine.add(self, review:Review): O(n) where n is amount of words in review

ReviewSearchEngine.search(self, word:str, n:int=None): O(N*LOG(N)) where N is the amount of reviews the word appears at
(bounded by R amount of reviews in input data)

ReviewSearchEngine.most_common(self, n:int): O(W*LOG(W)) where W is amount of unique review words in input data  


