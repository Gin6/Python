num = ['一','二','三']
all_student = []

for i in num:
    na = input('请输入第'+ i +'个人的姓名：')
    while True:
        he = float(input('请输入第'+ i +'个人的身高(米)：'))
        if 0.5<he<2.5:
            break
        else:
            print('您输入的身高不在合理范围内，请重新输入：')
            continue
    while True:
        we = float(input('请输入第'+ i +'个人的体重(kg)：'))
        if 20<we<300:
            break
        else:
            print('您输入的体重不在合理范围内，请重新输入：')
            continue
    while True:
        wa = int(input('请输入第'+ i +'个人的腰围(cm)：'))
        if 50<wa<200:
            break
        else:
            print('您输入的腰围不在合理范围内，请重新输入：')
            continue
    student = []
    student.append(na)
    student.append(he)
    student.append(we)
    student.append(wa)
    bmi = we/he**2
    student.append(bmi)
    all_student.append(student)
    all_student.sort(key=lambda x: x[4])

print('{:10s}{:10s}{:10s}{:10s}{:10s}{:10s}'.format('姓名','身高','体重','腰围','BMI指数','分析结果'))

j = 0
while j < 3:
    bmi = all_student[j][4]
    if bmi < 18.5:
        res = '偏瘦'
    elif bmi >= 18.5 and bmi <= 24:
        res = '正常'
    elif bmi > 24 and bmi < 28:
        res = '偏胖'
    else:
        res = '肥胖'
    print('{}{:12.2f}{:12.1f}{:10d}{:13.1f}{:>10s}'.format(all_student[j][0], all_student[j][1], all_student[j][2], all_student[j][3], all_student[j][4], res))
    j += 1