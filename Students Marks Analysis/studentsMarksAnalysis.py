import numpy as np

students = np.array(["Rahul", "Priya", "Amit", "Sneha", "Rohan"])
subjects = np.array(["Math", "Science", "English"])

import numpy as np

marks = np.array([
    [85, 78, 92],
    [90, 88, 95],
    [72, 80, 75],
    [95, 92, 89],
    [65, 70, 68]
])

print(marks)

print(marks.shape) # gives (rows,column)
print(marks.ndim) # gives which dimension data it is.
print(marks.size) # gives number of elements.

#Average
student_average1 = np.mean(marks) #will make average of all elements
student_average2 = np.mean(marks, axis=0) #0 - column-wise mean
student_average3 = np.mean(marks, axis=1) #1 - row-wise mean

print(student_average1)
print(student_average2)
print(student_average3)

#MAX
top_index = np.argmax(student_average3)
print(students[top_index])
print(top_index)

#MIN
low_index = np.argmin(student_average3)
print(students[low_index])
print(low_index)

#Boolean Filtering
condition = student_average3 > 80
print(condition)
print(students[condition])