import csv

data = [('IBM','content text 1','2017-08-28'),
        ('IBM','content text 2','2017-03-19'),
        ('IBM','content text 3','2017-07-22')]


class Parser(object):

    def write_to_csv(file_path:str,data:iterable):
        with open(file_path,'a') as csvFile:
            writer = csv.writer(csvFile, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerows(data)
            csvFile.close()

# I add here some comment.
# I add here some other comment on github.
# I add here some comment #3 localy.