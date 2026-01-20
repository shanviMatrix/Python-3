print("%s to the right" %('This is a string'))

#lists

colleges=['iit', 'nit', 'lpu']
print(colleges[1])
colleges[1]='dtu'
print(colleges[1])
print(colleges)

#append
list2=['table', 'chair', 'fan','clothes', 'bottle']
print(list2)
list2.append('microphone')
print(list2)

#insert
list2.insert(3, 'camera')
print(list2)

#remove
list2.remove('microphone')
print(list2)

#add
list3= list2 + ['pillow', 'tubelight', 'bed']
print(list3)
print(len(list3))

