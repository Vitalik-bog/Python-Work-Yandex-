#-*-coding: utf8 -*-
messages = []
def printOnlyNew(message):
    global messages
    if not message in messages:
        print(message)
        messages += [message]