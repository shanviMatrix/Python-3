#file-IO

#Creating a file
file1=open("shanvi.txt","wb")
print(file1.mode)
print(file1.name)
file1.write(bytes("Learning file handling in python","UTF-8"))
file1.close()

#Reading a file
file1=open('shanvi.txt','r+')
text_to_read=file1.read()
print(text_to_read)
