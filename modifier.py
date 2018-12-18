import os

names = 'names.txt'
urls = 'urls.txt'

begin_str = 'curl \"'
middle_str = '" -o "'
ending_str = '.jdx\";\n'
with open(names, 'r') as names_f, open(urls, 'r') as urls_f:
    for line_name, line_url in zip(names_f.readlines(), urls_f.readlines()):
        name_item = line_name.strip()
        url_item = line_url.strip()
        command = begin_str + url_item + middle_str + name_item + ending_str
        os.system(command)

os.system("mkdir -p jdx; mv *.jdx ./jdx/")
os.system("tar -czf jdx.tar.gz jdx")
