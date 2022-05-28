# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

#def read_file_content():
    # [assignment] Add your code here 
f  = open("story.txt", "r")
print(f.read())
f.close()


#def count_words():
text = open("story.txt")
    # [assignment] Add your code here
count = 0
for line in text:
    words = line.split(" ")
    count += len(words)
text.close()
print(count)

   #return {"as": 10, "would": 20}