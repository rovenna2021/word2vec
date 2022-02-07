# Convert text to lower-case and strip punctuation/symbols from words
def normalize_text(df):
    # Convert to lowercase
    new_df = df[['movie_title', 'plot_keywords','director_name','actor_1_name','actor_2_name','genres','title_year','actor_3_name', 'country', 'language']].copy()
    new_df['movie_title'] = new_df['movie_title'].str.lower().str.strip()
    new_df['plot_keywords'] = new_df['plot_keywords'].str.lower().str.strip()
    new_df['director_name'] = new_df['director_name'].str.lower().str.strip()
    new_df['actor_1_name'] = new_df['actor_1_name'].str.lower().str.strip()
    new_df['actor_2_name'] = new_df['actor_2_name'].str.lower().str.strip()
    new_df['actor_3_name'] = new_df['actor_3_name'].str.lower().str.strip()
    new_df['genres'] = new_df['genres'].str.lower().str.strip()
    new_df['country'] = new_df['country'].str.lower().str.strip()
    new_df['language'] = new_df['language'].str.lower().str.strip()
    
    # Replace "|" with " " for easier processing later
    new_df['genres'] = new_df['genres'].apply(lambda a: str(a).replace('|', ' '))
    new_df['plot_keywords'] = new_df['plot_keywords'].apply(lambda a: str(a).replace('|', ' '))

    # Fill NaN values with empty string
    new_df.fillna('', inplace=True)

    return new_df

# Tokenizer
def tokenize_text(df, cols):
    new_df = df.copy()
    new_df['tokens'] = new_df[cols].agg(','.join, axis=1)
    new_df['tokens'] = new_df['tokens'].str.split(r'\W+')

    # Make sure all empty strings are cleared
    new_df['tokens'] = new_df['tokens'].apply(lambda row: list(filter(lambda item: item, row)))
    return new_df

# Data Pre-processing Steps
# Step 1: Text Cleansing

cleaned_df = normalize_text(df)

# Step 2: Tokenization

# Step 2a - keywords (tags) tokenization
tokenized_df = tokenize_text(cleaned_df, ['movie_title', 'genres', 'plot_keywords'])

# Step 2b - append other features as tokens
tokenized_df['tokens'] = tokenized_df.apply(lambda row: [row['movie_title'], row['director_name'], row['actor_1_name'], row['actor_2_name'], row['actor_3_name'], row['country']] + row['tokens'], axis=1)

# Step 3: Lemmatization
def lemmatize_words(words):
    lemmatizer = nltk.stem.WordNetLemmatizer()
    return [lemmatizer.lemmatize(w) for w in words]

tokenized_df['tokens'] = tokenized_df['tokens'].apply(lemmatize_words).apply(lambda row: list(filter(lambda item: item, row)))

# Step 4: Stop Words Removal
stop = nltk.corpus.stopwords.words('english')

tokenized_df['tokens'] = tokenized_df['tokens'].apply(lambda x: [word for word in x if word not in stop])

tokenized_df[['movie_title', 'tokens']].head()
