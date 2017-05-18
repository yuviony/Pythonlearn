#Remove a Employee Details from the Dictionaries
print("List the Employee Details")
print("-------------------------")
emp = {
	"john" : 200,
	"James" : 201,
	"Jack" : 202
}
print("Before using of Delete employee details from Dictionaries")
print(emp)
print("After Delete Operations")
del emp["James"]
print(emp)
