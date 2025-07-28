while True:
    message = input("type some word and I will add emoji behind it: ")
    words = message.split()
    emojis = {":)":"😊", ":(":"☹️"}
    out_put = ""
    for word in words:
        out_put += emojis.get(word, word) 
    print(out_put)