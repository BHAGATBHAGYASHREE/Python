students = (
    ('bhagyashree', (85, 90, 92, 88, 95)),
    ('orry', (78, 85, 90, 80, 88)),
    ('bhupendra jogi', (92, 88, 85, 90, 95)),
    ('binod', (80, 82, 78, 85, 90)),
)

topper = max(students, key=lambda student: sum(student[1]))
topper_name = topper[0]
topper_marks = topper[1]
topper_info = (topper_name, topper_marks)
print(topper_info)