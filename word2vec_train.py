from gensim.models import word2vec

# Building Word2Vec Model
dataset = [row for row in tokenized_df['tokens']]
print(dataset[911])
model = word2vec.Word2Vec(dataset, workers=num_workers, \
            size=num_features, min_count = min_word_count, \
            window = context)

# If the model is not going to be trained further, init_sims can be called 
# init_sims will make the model much more memory-efficient.
model.init_sims(replace=True)