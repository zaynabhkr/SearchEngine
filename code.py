import os
import re
class searchengine:
    def __init__(self,directory):
        self.index = {}
        self.directory = directory

    def traverse_directory(self,directory):
        for root,dirs,files in os.walk(directory):
            for file in files:
                if file.endswith(('.txt', '.md','.log')):
                    file_path = os.path.join(root,file)
                    self.indexing_line(file_path)

    def indexing_line(self, file_path):

        with open(file_path, 'r') as file_data:

            i = 0

            for line in file_data:
                i += 1
                # for each word in each line we are indexing its file_path, line number and line itself where it is
                line_cleaned = self.clean_up(line)
                
                for word in line_cleaned:
                    if word not in self.index:
                        self.index[word] = []
                
                    self.index[word].append((file_path, i, line))
                    
        # trying to figure how to sort them:
        self.index = dict(sorted(self.index.items(), key=self.sort_by_list_length))

            
    def sort_by_list_length(self, item):
        return len(item[1])
        
    def search(self, query_input):
        results = []
        query_input = self.clean_up(query_input)
        for query in query_input:
            if query in self.index:
                return self.index[query]
       
                                            
    @staticmethod
    def clean_up(line):
        cleaned_line = "".join(e for e in line.lower() if e.isalnum() or e.isspace())
        return cleaned_line.split()


test_dir = './test_dir'

with open(os.path.join(test_dir, 'file1.txt'), 'w') as f1:
        f1.write("Foo is the bar best way to bat my biz bop!\n")
        f1.write("somethings random written dog.\n")
        
with open(os.path.join(test_dir, 'file2.md'), 'w') as f2:
        f2.write("foo bar does not baz bop at all\n")
        f2.write("Biz is great but biz is not bop too.\n")


search_engine = searchengine("./test_dir")
#Test Case 1:
search_engine.traverse_directory("./test_dir")
results = search_engine.search("biz +foo +bar +(bat baz) bop")
for result in results:
    print(f"Test case 1: {result[0]}, Line {result[1]}: {result[2]}")
#Test Case 2:
results = search_engine.search("+foo +bar")
for result in results:
        print(f"Test case 2: {result[0]}, Line {result[1]}: {result[2]}")
#Test Case 3:
results = search_engine.search("biz bop")
for result in results:
        print(f"Test case 3: {result[0]}, Line {result[1]}: {result[2]}")

        
