import pandas as pd
def question_3(dataset):
    condition = (dataset['语文'] > 90) & (dataset['数学'] < 120) & (dataset['英语'] >= 70) & (dataset['英语'] <= 110)
    students = dataset[condition]['学生姓名']
    return students
dataset = pd.read_excel('object-1-1.xlsx')
students = question_3(dataset)
print(students.tolist())
