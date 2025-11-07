canada = {'on':'ontario', 'ab':'alberata', 'qc':'quebec', 'ab':'alberta2'}
print(canada)

# print(canada['sa']) # throws an execption keyerror aka runtime error 

print(canada.get('sa,' 'this key does not exist'))
