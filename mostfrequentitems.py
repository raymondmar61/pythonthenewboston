#newboston 54 Finding Most Frequent Items

from collections import Counter

text = "We hope to one day become the world's leader in free, education resources.  We are constantly " \
"discovering and adding more free content to the website everyday.  There is already an enormous " \
"amount of resoruces online that can be accessed for free by anyone in the world, the main issue " \
"right now is that very little of it is organized or structured in any way.  We want to be the " \
"solution to that problem."
#convert text above to a list of words in list [] format
words = text.split()
print(words) #print ['We', 'hope', 'to', 'one', 'day', 'become', 'the', "world's", 'leader', 'in', 'free,', 'education', 'resources.', 'We', 'are', 'constantly', 'discovering', 'and', 'adding', 'more', 'free', 'content', 'to', 'the', 'website', 'everyday.', 'There', 'is', 'already', 'an', 'enormous', 'amount', 'of', 'resoruces', 'online', 'that', 'can', 'be', 'accessed', 'for', 'free', 'by', 'anyone', 'in', 'the', 'world,', 'the', 'main', 'issue', 'right', 'now', 'is', 'that', 'very', 'little', 'of', 'it', 'is', 'organized', 'or', 'structured', 'in', 'any', 'way.', 'We', 'want', 'to', 'be', 'the', 'solution', 'to', 'that', 'problem.']
#most frequently occuring word.  Give Counter() function a list
counter = Counter(words)
top_three = counter.most_common(3) #three most common words from the list
print(top_three) #print [('the', 5), ('to', 4), ('is', 3)]