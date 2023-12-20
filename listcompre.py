a = [(),(),(""),('a','b'),('a','b','c'),('d')]
removetup= [t for t in a if t!=()]
print("List of tuples without empty tuples:", removetup)
