import json

infile = "yelp_academic_dataset_review.json"
outfile = "cleaned_file.json"

delete_list1 = [" a ", " in ", " of ", " the ", " at ", " line ", " get "]
delete_list2 = [";", ":", ".", ",", "?", "!", "(", ")", "}", "{", "\"", "\'"]
with open(infile) as fin, open(outfile, "w+") as fout:
    for line in fin:
        for word in delete_list1:
            line = line.replace(word, " ")
        for word in delete_list2:
            line = line.replace(word, "")
        fout.write(line)
