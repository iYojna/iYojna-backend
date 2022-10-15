#  nlp implementation 
def nlp(text):
    
    from gensim.parsing.preprocessing import STOPWORDS
    
    import nltk
    
    nltk.download('punkt')
    
    from nltk.tokenize import word_tokenize
    
    all_stopwords_gensim = STOPWORDS
    
    sw_list = {"not"}
    
    all_stopwords_gensim = STOPWORDS.difference(sw_list)

    
    # text = "how i am elidgible for kalash chit fund scheme"
    
    text_tokens = word_tokenize(text)
    
    tokens_without_sw = [word for word in text_tokens if not word in all_stopwords_gensim]
    return tokens_without_sw
