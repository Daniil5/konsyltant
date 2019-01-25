name = input('введите ваше имя')
surename = input('введите вашу фамилию')
age = input('введите ваш возраст')
weight = input('введите ваш вес')
print('ваше имя и фамилия', name, surename, 'полных лет', age, 'вес', weight, 'килограмм')
a = int(30)
b = int(40)
c = int(50)
d = int(120)
if (int(age) <= a) and (int(weight) > 50) and (int(weight) < 120):
    print('вы в хорошей форме')
elif (int(age) > b) and (int(weight) < c):
    print('с вами что то не так')
elif ((int(age) > a) and (int(age) < b)) and ((int(weight) < c) and (int(weight) > d)):
    print('вам следует заняться собой, для лучшего результата проконсультируйтесь с врачем')
elif (int(age) > b) and (int(weight) < c) and (int(weight) > d):
    print('вам конец')
else:
    print('с вами все плохо, нужно проконсультироваться с врачем')
