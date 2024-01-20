#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = len(sentence)
    if sentence == "":
        first_sen = "None"
    else:
        first_sen = sentence[0]
    return (str_len, first_sen)
