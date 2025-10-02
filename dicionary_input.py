 #create an empty dictionary . allow  friends to enter their favoraite lang as value and use keys as their names .
 #  assume that the names are unique


Dic = {}

name=input("enter friend name")
lang=input("enter language name")

Dic.update({name:lang})

name=input("enter friend name")
lang=input("enter language name")

Dic.update({name:lang})

name=input("enter friend name")
lang=input("enter language name")

Dic.update({name:lang})

name=input("enter friend name")
lang=input("enter language name")

Dic.update({name:lang})


print(Dic)


output:
enter friend name shivam
enter language name eng
enter friend name sachin
enter language name c
enter friend name abhay
enter language name python
enter friend name yash
enter language name hindi
{'shivam': 'eng', 'sachin': 'c', 'abhay': 'python', 'yash': 'hindi'}
