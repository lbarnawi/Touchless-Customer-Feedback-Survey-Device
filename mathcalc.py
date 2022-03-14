#get file object reference to the file
file = open("feedback.txt", "r")

#read content of file to string
data = file.read()

#get number of occurrences of the substring in the string
occurrences = data.count("راضي")


occurrences1 = data.count("محايد")


occurrences2 = data.count("غير راضي")


print('عدد الراضين :', occurrences-occurrences2)
print('عدد المحايدين :', occurrences1)
print('عدد الغير راضين :', occurrences2)