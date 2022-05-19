# employee data with key as id of the employee and values as age of the employee
employee_data ={101: 43, 102: 25, 103: 43, 104: 31, 105: 26, 106: 28, 107: 29, 108: 43, 109: 25, 110: 22, 111: 22, 112: 25, 113: 30, 115: 45, 116: 23, 117: 29, 118: 28, 119: 30, 120: 28, 121: 42, 122: 39, 123: 29, 124: 42, 125: 43, 126: 42, 127: 40, 128: 27, 129: 23, 130: 30, 131: 37, 132: 20, 133: 36, 134: 27, 135: 27, 136: 22, 137: 28, 138: 23, 139: 45, 140: 39, 141: 29, 142: 33, 143: 39, 145: 34, 146: 26, 147: 30, 148: 38, 149: 29, 150: 24, 151: 28, 152: 34, 153: 42, 154: 29, 155: 23, 156: 31, 158: 25, 160: 45, 161: 42, 162: 27, 163: 24, 164: 20, 166: 24, 167: 28, 168: 20, 169: 33, 170: 34, 171: 37, 172: 45, 173: 35, 174: 23, 175: 44, 176: 27, 177: 30, 178: 26, 179: 27}

#### Identify the senior most employees age

"- 45\n"
"- 44\n"
"- 48\n"
"- 42"
# Type your code here
print((sorted(employee_data.values()))[-1])
# output = 45

#### Identify the age of the employee with employee id 159 [ If the employee isn't present return NA]

"- 25\n"
"- 32\n"
"- NA\n"
"- 42"
# Type your code here
print(159 in employee_data)
# output = false = NA

#### Count the total number of employee in the organization

"- 79\n"
"- 78\n"
"- 60\n"
"- 74"
# Type your code here
print(len(employee_data))
# output = 74

#### Calculate the mean age of the employees

"- 31.36\n"
"- 36.48\n"
"- 28.77\n"
"- 32.47"
# Type your code here
from statistics import mean
print(mean(employee_data.values()))
# output = 31.36


#### Perform the following two tasks and then calculate the updated mean age of the employees
# Task1 Update the ages of employee id - 104,140, and 164 as 27
# Task2 Remove the employ with employee id - 143

"- 30.71\n"
"- 31.36\n"
"- 30.13\n"
"- 31.13\n"
# Type your code here
#task 1
employee_data[140] = 27
employee_data[104] = 27
employee_data[164] = 27

#task 2
del employee_data[143]

print(mean(employee_data.values()))
# output = 31.13

