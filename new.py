# example of tokenazing
# in other words splitting

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."
#splitting by sentense
print(sent_tokenize(EXAMPLE_TEXT))
# splitting by word
print(word_tokenize(EXAMPLE_TEXT))

# example of stopwords usage

example_sent = "This is a sample sentence, showing off the stop words filtration."
stop_words = set(stopwords.words('english'))

# splitting by word
word_tokens = word_tokenize(example_sent)

# filtering with stop_words
filtered_sentence = [word for word in word_tokens if word not in stop_words]

print(word_tokens)
print(filtered_sentence)
