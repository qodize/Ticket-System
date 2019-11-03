with open("strings.txt", encoding='utf-8') as f_in:
    data = f_in.readlines()
res = 0

for line in data:
    if not (line == '\n' or line.startswith('#')):
       res += 1

print(res)
