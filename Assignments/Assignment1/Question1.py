#Question 1
#statistics module. It provides some functions for calculating basic statistics on data like mean, median
import statistics

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#sort() function to sort the list and min(),max() to find minimum and maximum values of list respectively.
ages.sort()
print("Sorted ages: ", ages)
print("Minimum value of ages: ", min(ages))
print("Maximum value of ages: ", max(ages))
# insert(position, value) - inserts the value in list at specified position
ages.insert(0,min(ages))
# append(value) - appends the value at the end of list
ages.append(max(ages))
print("List after update: ", ages)
#The biggest advantage of using median() function is that the data-list does not need to be sorted 
#before being sent as parameter to the median() function using statistice module
print("Median of ages: ", statistics.median(ages))
print("Average of ages: ", statistics.mean(ages))
print("Range of ages: ", max(ages)-min(ages))

#we can also use below code to find median and average of listed data
"""
ages_length = len(ages)
if ages_length/2 != 0:
    print("Median of ages: ", ages[int(ages_length/2)])
else:
    print("Median of ages: ", ages[ages_length-1/2]+ages[ages_length+1/2])
    
print("Average of ages: ", sum(ages)/ages_length)
"""
#data inside triple quotes is ignored by python while execution, unless it is assigned to a variable



#Question 2
dog= dict()
#update() method inserts the specified dictionary  or any key-value pairs to the resp. dictionary
dog.update({"name":"Tommy", "color":"Apricot", "breed":"Pug", "legs":4, "age":2})
print("Added key-value pair to dog: ",dog)

#used  dict() function which creates a empty dictionary
student_dict = dict()
keyList = ["first_name", "last_name", "gender","age","marital status","skills","country","city","address"]
#added only keys to the dictionary with None value using update method
student_dict.update({key: None for key in keyList})
print("\nStudent_Dictionary after adding keys: ",student_dict)

#utilised len(dictionary) function to calculate lenght
print("Length of Student_Dictionary: ", len(student_dict))
#updated student_dict with sample values
student_dict.update({"first_name": "Sasank", "last_name": "Tipparaju", "gender": "Male", "age": "24",
                     "marital status": "Single", "skills": ["Java","Python"], "country": "India", "city": "Nellore",
                     "address": "2B ABC Street"})

print("\nStudent_dict after values update: ", student_dict)

#accessing paritcular value of key in dict: dict["key"]
print("\nAccessing Skills value in dictionary: ",student_dict["skills"])
#type(value) - function gives the datatype of provided values
print("Data Type of Skills in Student Dict: ", type(student_dict["skills"]))

#The extend() adds all the elements of an iterable (list, tuple, string etc.) to the end of the list
student_dict["skills"].extend(["Apex", "JavaScript"])
print("Updated Skills list after adding new values: ", student_dict["skills"])

# dict.keys() and values() gives the list of keys and values as a list respectively
print("\nStudent: ",student_dict.keys())
print("Student: ",student_dict.values())




#Question 3
sisters = ("Bhavya","Mounika")
print("Sisters: ", sisters,"\t type of sisters: ", type(sisters))
brothers = ("Santhan","Sarath","Prem")
print("Brothers: ", brothers, "\t type of brothers: ", type(brothers))
siblings = sisters+brothers
print("siblings: ",siblings,"\t type of siblings: ", type(siblings))
print("Number of Siblings: ", len(siblings))
family_members = siblings+("Gopikrishna","Sujatha")
print("family_members: ", family_members, "\t type of family members ", type(family_members))




#Question 4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
#add(elements) adds elements into the set
it_companies.add('Twitter')
print("it_companies: ", it_companies)
it_companies.update(['Cognizant','LinkedIn','Salesforce','Wipro'])
print("it_companies after update: ",it_companies, type(it_companies))
#remove() remove the element from the set
it_companies.remove("LinkedIn")
print(it_companies)

#Difference between remove and discard
print("\nDifference between Remove() and Discard(): Discard() method is different from the remove() method, because the remove() method will throw an error if the specified item is not present in list, whereas the discard() method will not throw any error if item doesn't exist in list.")
A = {19, 22, 24, 20, 25, 26} 
B = {19, 22, 20, 25, 26, 24, 28, 27} 
#all set operation can be performed in set: union(), intersection()
print("\nUnion of A and B sets: ",A.union(B))
print("Intersection of A and B sets: ",A.intersection(B))
#issubset() returns true if it is subset of other else false
print("A is Subset of B? ",A.issubset(B))
#to check is A and B are disjoint sets ( no elements in common)
print("A and B are disjoint sets? ",A.isdisjoint(B))
print("(AUB) AND (BUA): ",(A.union(B)).intersection(B.union(A)))
#checking symmetric differece .. return the extra elements of set A that are not in B
print("Symmetric Difference of A with B: ",A.symmetric_difference(B))
#clear() clear/ delete all elements from set
A.clear()
B.clear()
print("After clear Set A values: ", A,"\tSet B values: ",B)

age = [22, 19, 24, 25, 26, 24, 25, 24] 
print("\nage list: ",age)
age_set = set(age)
print("set of ageslist: ", age_set, "Datatype: ", type(age_set))
print("Length of age list: ", len(age), "\nLength of age set",len(age_set))



#Question 5
from math import pi
radius_of_circle = 30
_area_of_circle_ = pi * radius_of_circle **2
print("Area of a circle = ",_area_of_circle_," meters square")
_circum_of_circle_ = 2 * pi * radius_of_circle
print("Circumference of a circle = ",_circum_of_circle_, ' meters')

_radius_of_circle_ = float(input("Enter radius of circle: "))
_area_of_circle_ = pi * _radius_of_circle_ **2
print("Area of a circle = ",_area_of_circle_," meters square")



#Question 6
print("I am a teacher and I love to inspire and teach people")
set_words = set(("I am a teacher and I love to inspire and teach people".split(" ")))
print("Number of Unique words: ",len(set_words), set_words)



#Question 7
text = "Name \t Age \tCountry City\nAsabench 250 \tFinland Helsinki"
print(text)



#Question 8
radius = 10 
area = 3.14 * radius ** 2 
print("The area of a circle with radius",radius,"is %.0f" %area, "meters square.")



#Question 9
#1lb = 0.453592kg
number_of_students = int(input("Enter number of students: "))
weight_of_students_lbs = list() #to store weights in lbs
weight_of_students_kgs = list() # to store weights in kgs

for each in range(number_of_students):
    weight_lb = int(input("Enter weight of {} student in lbs: ".format(each+1)))
    weight_of_students_lbs.insert(each, weight_lb)
    #converting lbs to kg and adding to seperate list
    weight_kg = float("%.2f" %(weight_lb*0.453592))
    weight_of_students_kgs.insert(each, weight_kg)
    
print("weight of students in lbs: ",weight_of_students_lbs)
print("weight of students in kgs: ",weight_of_students_kgs)
