# Filter the list of vectors to include only those that Word2Vec has a vector for
vector_list = [model[word] for word in [item for sublist in dataset for item in sublist] if word in model.wv.vocab]

# Create a list of the words corresponding to these vectors
words_filtered = [word for word in [item for sublist in dataset for item in sublist] if word in model.wv.vocab]

# Zip the words together with their vector representations
word_vec_zip = zip(words_filtered, vector_list)

# Cast to a dict so we can turn it into a DataFrame
word_vec_dict = dict(word_vec_zip)
df = pd.DataFrame.from_dict(word_vec_dict, orient='index')
df.head(3)