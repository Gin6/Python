num = ['一','二','三']
all_student = []

for i in num:
    str = []
    str = input('请输入第'+ i +'个人的姓名、身高(米)、体重(kg)、腰围(cm)：')
    info = str.split(" ")
    na = info[0]

    while True:
        try:
            he = float(info[1])
            if 0.5<he<2.5:
                break
            else:
                print('您输入的身高不在合理范围内，请重新输入：')
                he = float(input('请输入第' + i + '个人的身高(米)：'))
                info[1] = he
                continue
        except ValueError:
            print('您输入的身高值无效，请重新输入：')
            he = float(input('请输入第' + i + '个人的身高(米)：'))
            info[1] = he
        except IndexError:
            print('您没有输入身高，请重新输入：')
            he = float(input('请输入第' + i + '个人的身高(米)：'))
            info.append(he)
    while True:
        try:
            we = float(info[2])
            if 20<we<300:
                break
            else:
                print('您输入的体重不在合理范围内，请重新输入：')
                we = float(input('请输入第' + i + '个人的体重(kg)：'))
                info[2] = we
                continue
        except ValueError:
            print('您输入的体重值无效，请重新输入：')
            we = float(input('请输入第' + i + '个人的体重(kg)：'))
            info[2] = we
        except IndexError:
            print('您没有输入体重，请重新输入：')
            we = float(input('请输入第' + i + '个人的体重(kg)：'))
            info.append(we)
    while True:
        try:
            wa = int(info[3])
            if 50<wa<200:
                break
            else:
                print('您输入的腰围不在合理范围内，请重新输入：')
                wa = int(input('请输入第' + i + '个人的腰围(cm)：'))
                info[3] = wa
                continue
        except ValueError:
            print('您输入的腰围值无效，请重新输入：')
            wa = int(input('请输入第' + i + '个人的腰围(cm)：'))
            info[3] = wa
        except IndexError:
            print('您没有输入腰围，请重新输入：')
            wa = float(input('请输入第' + i + '个人的腰围(cm)：'))
            info.append(wa)
    student = []
    student.append(na)
    student.append(he)
    student.append(we)
    student.append(wa)
    bmi = we / he ** 2
    student.append(bmi)
    all_student.append(student)
    all_student.sort(key=lambda x: x[4])

f = open('16210120420_郑斌_3.txt','w+')
print('{:10s}{:10s}{:10s}{:10s}{:10s}{:10s}'.format('姓名','身高','体重','腰围','BMI指数','分析结果'))
f.write('{:10s}{:10s}{:10s}{:10s}{:10s}{:10s}'.format('姓名','身高','体重','腰围','BMI指数','分析结果')+'\n')

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
    f.write('{}{:12.2f}{:12.1f}{:12d}{:15.1f}{:>13s}'.format(all_student[j][0], all_student[j][1], all_student[j][2], all_student[j][3], all_student[j][4], res)+'\n')
    j += 1

f.close()