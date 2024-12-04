pastmessage = ''
def  printWithoutDuplicates(message):
    global pastmessage
    if pastmessage != message:
        print(message)
        pastmessage = message