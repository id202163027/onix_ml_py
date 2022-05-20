## Lesson_021 task
For the provided text dataset contained in the file dataset.txt:
1. Download data, if there are problems with the encoding, skip the problem characters.
2. Preprocess the loaded text by removing the following characters: carriage return to the next line (\n), return to the beginning of the current line (\r), tabulation (\t). In addition, repeating spaces should be replaced with a single space.
3. Using the capabilities of the spaCy library, perform tokenization, lemmatization, enlarged and refined POS tagging (Token.pos_ and Token.tag_), and also find syntax dependency tags (Token.dep_). All results are presented as a Pandas dataframe.
4. Remove duplicate rows in the received dataframe and save the resulting dictionary table in XLSX format.
5. Using the Gensim library, build a Word2Vec model based on lemmas and demonstrate the results of its work (similarity, most_similar, most_similar_cosmul, etc.).