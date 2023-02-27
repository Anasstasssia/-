f = open('википедия.txt') #открываем текст
f_r = open('реферат.txt')
vik = f.read()
ref = f_r.read()
total = len(ref)  #смотрим общую длину реферата
mas_words_ref = ref.split()
mas_words_vik = vik.split()
mas_words_vik_new = [] #создаем новые массивы, в которых будут объединены по три слова, так как плагиат в нашем случае 3 подряд слова
mas_words_ref_new = []
for i in range(0,len(mas_words_ref)-2):
    mas_words_ref_new.append(str(mas_words_ref[i]+mas_words_ref[i+1]+mas_words_ref[i+2])) #объединяем по три слова в тексте реферата
for i in range(0,len(mas_words_vik)-2):
    mas_words_vik_new.append(str(mas_words_vik[i]+mas_words_vik[i+1]+mas_words_vik[i+2])) #объединяем по три слова в тексте википедии

copi = 0
for i in mas_words_ref_new:
    for j in mas_words_vik_new:
        if i == j: #сравниваем значения в тексте реферата и википедии
            copi += len(i) #в случае совпадения добавляем выявление плагиата(добавляем 3, так как разбивали по тройкам)
print('Процент плагиата - ', (copi/total)*100)