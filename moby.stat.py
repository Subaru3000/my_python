with open('123.txt') as file:
    s = file.readlines()
    s = s[0].split()
    print(s)
def histogram(s):

    word_count = {}
    for word in s:
        word_count.setdefault(word, 0)  # word_count[key] = 0, если такого key не было ранее
        word_count[word] += 1 # word_count[word] = word_count[word] + 1        
    return word_count

if __name__ == "__main__":

    d = histogram(s)
    print(d)


list_d = list(d.items())


list_d.sort(key=lambda i: i[1])
print(list_d)
print(list_d[0:5], list_d[len(list_d)-5:len(list_d)])
