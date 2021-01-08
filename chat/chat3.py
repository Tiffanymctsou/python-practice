lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())

for line in lines:
    s = line.split(' ')
    time = s[0][:5]
    name = s[0][5:]
    text = str(s[1:])
    print(name + ':' + text)
    # if line == 'Allen':
    #     person = Allen
    #     continue
    # elif line == 'Viki':
    #     person = Viki
    #     continue
    # print(person + ':' + line)
