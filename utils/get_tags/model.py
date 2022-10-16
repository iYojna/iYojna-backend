#  nlp implementation 
def nlp(text):
    
    from gensim.parsing.preprocessing import STOPWORDS
    
    import nltk

    duj = ["લેતા", "શા", "ઉભા", "હો", "હોઈ", "મા", "મૂકી", "નહી", "બધું", "હા", "મી", "એન", "તું", "નો", "છો", "જી",
           "લેવા", "આર", "છીએ", "નં", "એવો", "હોવા", "તેથી", "નું", "છ", "એવા", "એની", "થતાં", "જેવી", "બંને", "હશે",
           "માં", "ની", "હતાં", "તેવી", "થયો", "એવી", "થી", "થયું", "ત્યાં", "બની", "ગયો", "છતાં", "આપી",
           "રહે", "તેઓ", "પાસે", "તેમ", "ને", "તેને", "હું", "બાદ", "શકે", "જો", "અંગે", "રહી", "એમ", "તેના", "કરે",
           "થઇ", "સુધી", "જાય", "રૂા", "કોઈ", "ના", "હવે", "તેની", "સામે", "આવે", "બે", "થઈ", "ન", "જે", "આવી", "તા",
           "પર", "હોય", "હતું", "એ", "કરી", "તે", "હતી", "માટે", "તો", "જ", "પણ", "કે", "આ", "અને", "છે"]

    nltk.download('punkt')
    
    from nltk.tokenize import word_tokenize
    
    all_stopwords_gensim = list(STOPWORDS)
    all_stopwords_gensim.extend(duj)
    STOPWORDS = set(all_stopwords_gensim)
    sw_list = {"not"}
    
    all_stopwords_gensim = STOPWORDS.difference(sw_list)

    # text = "how i am eligible for kalash chit fund scheme"
    text_tokens = word_tokenize(text)
    
    tokens_without_sw = [word for word in text_tokens if not word in all_stopwords_gensim]
    return tokens_without_sw
