import coffeeshop

# Below is an example script showing how to use 
# the decorator design pattern 
# to construct objects with complex behavior using 
# composition rather than inheritance

myCoffee = coffeeshop.Concrete_Coffee()
print('Ingredients: '+myCoffee.get_ingredients()+
	'; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))

myCoffee = coffeeshop.Milk(myCoffee)
print('Ingredients: '+myCoffee.get_ingredients()+
	'; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))

myCoffee = coffeeshop.Vanilla(myCoffee)
print('Ingredients: '+myCoffee.get_ingredients()+
	'; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))

myCoffee = coffeeshop.Sugar(myCoffee)
print('Ingredients: '+myCoffee.get_ingredients()+
	'; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))








