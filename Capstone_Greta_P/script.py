from trie import Trie
from data import *
from welcome import *
from hashmap import HashMap
from linkedlist import LinkedList

#Printing the Welcome Message
print_welcome()

#Write code to insert food types into a data structure here. The data is in data.py
food_types = LinkedList()
for food in types:
	food_types.insert_beginning(food)
#print(food_types.stringify_list())
#print(type(food_types))

#Write code to insert restaurant data into a data structure here. The data is in data.py
type_rest = HashMap(len(types))
for food in types:
  rest_list = LinkedList()
  for rest in restaurant_data:
    #print(rest[0])
    if rest[0] == food:
      rest_hash = HashMap(4)
      rest_hash.assign("name",rest[1])
      rest_hash.assign("price",rest[2])
      rest_hash.assign("rating",rest[3])
      rest_hash.assign("address",rest[4])
      #print(rest_hash.retrieve("address"))
      rest_list.insert_beginning(rest_hash)
  type_rest.assign(food,rest_list)#print(rest_list.stringify_list())

#Write code for user interaction here
while True:
    user_input = str(input("\nWhat type of food would you like to eat?\nType the beginning of that food type and press enter to see if it's here.\n")).lower()
    #Search for user_input in food types data structure here
    matches = []
    current_node = food_types.get_head_node()
    while current_node.get_value() is not None:
      if current_node.get_value().startswith(user_input):
        matches.append(current_node.get_value())
        current_node = current_node.get_next_node()
      else:
        current_node = current_node.get_next_node()
      
      
    if len(matches) == 0:
      print("\nNo food types match your search.")
      
      
    elif len(matches) == 1:
      yn = str(input("\nThe only option with those beginning letters is {0}. Do you to look at {0} restaurants? Enter 'y' for yes and 'n' for no.".format(matches[0])))
      if yn == 'y':
        #After finding food type write code for retrieving restaurant data here
        user_type = matches[0]
        print("\nDisplaying {0} restaurants...".format(user_type))
        rest_list = type_rest.retrieve(user_type)
        current_rest_node = rest_list.get_head_node()
        while current_rest_node:
          current_rest = current_rest_node.get_value()
          if current_rest is not None:
            print("-------------")
            print("Name: {0}".format(current_rest.retrieve("name")))
            print("Prince: {0}".format(current_rest.retrieve("price")))
            print("Rating: {0}".format(current_rest.retrieve("rating")))
            print("Address: {0}".format(current_rest.retrieve("address")))
          current_rest_node = current_rest_node.get_next_node()
               
      elif yn == 'n':
        print("\nOk, let's try again")
      else:
        print("\nPlease try again.")
    else:
      print("With those beginning letters, your choices are {0}".format(matches))
    
       
    
    


    



