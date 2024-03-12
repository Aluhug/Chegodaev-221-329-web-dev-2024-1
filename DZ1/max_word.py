n=input() #Это для тестов, чтбы вводить названия разных файлов для проверки
with open(n, 'r', encoding='utf-8') as file:
    s=file.read().split()

words=[''.join(filter(str.isalnum, word)) for word in s]
maxlen=max(len(x) for x in words)
maxlenwords=[x for x in words if len(x)==maxlen]
for word in maxlenwords:
    print(word)