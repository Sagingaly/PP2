car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get('model'))

car['year']=2020
print(car) #changing items on dictionary

car['color']='red'
print(car) #adding new item on dictionary

car.pop('model')
print(car) #removing model by the pop()

car.clear()
print(car) # by the method clear empty the car dictionary