import model


def getTags(inputStr):
    tags = model.nlp(inputStr)
    return tags
