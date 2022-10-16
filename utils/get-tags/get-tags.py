import model
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

def remove_stopwords(inputStr):
    new_text = []
    
    for word in inputStr.split():
        if word in stopwords.words('english'):
            new_text.append('')
        else:
            new_text.append(word)
    x = new_text[:]
    new_text.clear()
    return " ".join(x)

ps = PorterStemmer()
def stem_words(inputStr):
    return " ".join([ps.stem(word) for word in inputStr.split()])


def getTags(inputStr):
    tags = model.nlp(inputStr)
    return tags


def nltk():
  return  remove_stopwords(),stem_words(), getTags()
    

    