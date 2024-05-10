# numbers= 12, 13, 19, 60, 45, 35, 20, 11, 90, 65, 55
# sum=sum(numbers)
# product=(numbers)
# largest_number=max(numbers)
# smallest_number=min(numbers)
# count=len(numbers)
# print(sum)
# print(product)
# print(largest_number)
# print(smallest_number)
# print(count)


# list=[5, 2, 6, 13, 20, 18, 11, 45, 34, 65]
# sort=list[::-1]
# print(sort)

# fruit=("banana")
# first_character=fruit[1]
# modified_string=fruit.replace(first_character, '$')
# print(modified_string)

# first_name="Naomi"
# second_name="Cherono"
# name1= first_name[:2] + second_name[2:]
# name2= second_name[:2] + first_name[2:]
# name=first_name + ' ' + second_name
# print(name)


#11
# words=["ca", "dog", "sun", "cup", "communication"]
# length= max(words)
# length2 = len(length)
# print(length2)

# #12
# input="165"
# if int(input):
#     print("the input is an interger")
# else:
#     print("the input is not an integer")

# #13
# fruits={1: "banana", 3: "apple", 2: "orange"}
# print(fruits[1])
# print(fruits[2])
# print(fruits[3])


#14
# fruits={1: "banana", 3: "apple", 2: "orange"}

# for key, value in fruits.items():
#     print(f"{key}:{value}")
    
#15
# fruits={1: "banana", 3: "apple", 2: "orange"}
# fruits["4"]="pineapple"
# print(fruits)

#16
fruits={1: "banana", 3: "apple", 2: "orange"}
fruits2={4: "three tomatoes", 5: "mango", 6: "passion"}
all_fruits= {**fruits, **fruits2}
print(all_fruits)
