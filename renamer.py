import os

def renamer(front,end,source,target):
        #generate a list of the texts needs to be changed
        word_list=[]
        with open(source+'.txt', 'r') as file:
                for line in file:
                        word = line.strip()  # Remove leading/trailing whitespace, if any
                        word_list.append(word)
                        
        #generate a list of modified texts
        final_list=[]
        for word in word_list:
                final_list.append(word[int(front):int(end)])
        
        final_list_line_by_line= '\n'.join(final_list)

        # import final sentences in final file
        with open(target+'.txt', 'w') as file:
                file.write(final_list_line_by_line)

        print("Final file has been modified and created successfully!")

renamer(5,4,'file','final')
