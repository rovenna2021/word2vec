person_list = list(tokenized_df['director_name'])+list(tokenized_df['actor_1_name'])+list(tokenized_df['actor_2_name'])+list(tokenized_df['actor_3_name'])

def similar_watch(v, n = 7):
     
    # extract most similar movies for the input vector
    ms = model.wv.similar_by_vector(v, topn= n+1)[1:]
     
    # extract name and similarity score of the similar movies
    new_ms = pd.DataFrame()
    for j in ms:
        if j[0] not in person_list:
            r = tokenized_df.loc[(tokenized_df['movie_title'].str.contains(j[0], case=False)) | \
                             (tokenized_df['plot_keywords'].str.contains(j[0], case=False)) | \
                             (tokenized_df['genres'].str.contains(j[0], case=False))]
            new_ms = pd.concat([new_ms, r], ignore_index = True, axis = 0)
    return new_ms.head(7)

results = similar_watch(model.wv['catch me if you can'])
results