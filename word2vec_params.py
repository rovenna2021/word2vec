# Parameters of Word2vec model
num_features = 100  # Dimension of word vectors - it defines the number of words each token in the vocabulary is associated with
min_word_count = 1   # Words with occurance below the threshold will be ignored
num_workers = 4       # Number of threads to run in parallel
context = 5          # Context window size for each word
sg = 0 # 0 for CBOW, 1 for skipgram                                     