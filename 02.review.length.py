import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

infile = "input_file.txt"
outfile = "cleaned_file.json"

delete_list1 = [" a ", " in ", " of ", " the ", " at ", " line ", " get "]
delete_list2 = [";", ":", ".", ",", "?", "!", "(", ")", "}", "{", "\"", "\'"]
dict_word = {};
with open(infile) as fin, open(outfile, "w+") as fout:
    for line in fin:
        for word in delete_list1:
            line = line.replace(word, " ")
        for word in delete_list2:
            line = line.replace(word, "")
        fout.write(line)
        split_word = line.split();
        for word in split_word:
            if word in dict_word:
                dict_word[word] = dict_word[word]+1
            else:
                dict_word[word] = 1

for k, v in dict_word.items():
    print(k, v)

noise = np.random.normal(0, 1, (1000, ))
density = stats.gaussian_kde(noise)
n, x, _ = plt.hist(noise, bins=np.linspace(-3, 3, 50),
                   histtype=u'step', density=True)
plt.plot(x, density(x))
plt.savefig('02.review.length.png')
plt.show()
