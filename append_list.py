#syntax: list.append()
#append() adds an element to the end of the list
languages=['c','cpp','java']
print(languages)
languages.append('python')
print(languages)
languages.append('ruby')
print(languages)

#insert method adds an item at a specificied position in a list
languages.insert(0,'Php')
print(languages)

#We can also use extend method.
more_languages = ["css","reactpy"]
languages.extend(more_languages)
print(languages)