from collections import Counter

def analyze(filename, outname):
    cnt = Counter()
    with open(filename, 'r') as file:
        for line in file:
            for word in line.split():
                cnt[word] += 1
                
    print('Слово ~ частота употребления')
    for word, num in cnt.most_common(100):
        print(word, '~', num)

    print('\n\n\n\n\n\n\nСоздание отчёта с результатами анализа текста..')
    with open(outname, 'w') as outfile:
        outfile.write("Отчёт с результатами анализа текста.\n\n")
        outfile.write("Топ 100 слов по частоте употребления: \n")
        outfile.write("Слово ~ частота употребления \n\n")

        i = 1
        for word, num in cnt.most_common(100):
            outfile.write(str(i) + '. ' + word + ' ~ ' + str(num) +'\n')
            i+=1
    print('Отчёт сохранён в', outname)