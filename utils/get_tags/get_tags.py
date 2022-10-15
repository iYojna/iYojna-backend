from .model import nlp


def getTags(inputStr):
    tags = list(set(nlp(inputStr)))
    return tags
