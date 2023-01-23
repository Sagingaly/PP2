fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

fruits = {"apple", "banana", "cherry"}
fruits.add('orange')
print(fruits) #adding a new item on set

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits) #method to add multiple items to the fruits set.


fruits = {"apple", "banana", "cherry"}
fruits.remove('banana')
print(fruits) #removing element by remove()

fruits = {"apple", "banana", "cherry"}
fruits.discard('banana')
print(fruits) #removing element by discard()

