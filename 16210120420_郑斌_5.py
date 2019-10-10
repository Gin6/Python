def get_text():
    f = open('David Copperfield.txt','r',encoding='unicode_escape')
    text = f.read()
    for i in '!@#$%^&*()_¯+-;:`~\'"<>=./?,':
        text = text.replace(i,' ')
    return text.split()

ls = get_text()
counts = {}
for i in ls:
    counts[i] = counts.get(i,0) + 1

iteams = list(counts.items())
iteams.sort(key=lambda x:x[1],reverse=True)

for i in iteams:
    print(i)