name1 = input('请输入第一个人的姓名：')
height1 = float(input('请输入第一个人的身高(米)：'))
weight1 = float(input('请输入第一个人的体重(kg)：'))
waistline1 = int(input('请输入第一个人的腰围(cm)：'))
name2 = input('请输入第二个人的姓名：')
height2 = float(input('请输入第二个人的身高(米)：'))
weight2 = float(input('请输入第二个人的体重(kg)：'))
waistline2 = int(input('请输入第二个人的腰围(cm)：'))
name3 = input('请输入第三个人的姓名：')
height3 = float(input('请输入第三个人的身高(米)：'))
weight3 = float(input('请输入第三个人的体重(kg)：'))
waistline3 = int(input('请输入第三个人的腰围(cm)：'))
bmi1 = weight1/height1**2
bmi2 = weight2/height2**2
bmi3 = weight3/height3**2
if bmi1 < 18.5:
    result1 = '偏瘦'
elif bmi1 >=18.5 and bmi1 <=24:
    result1 = '正常'
elif bmi1 >24 and bmi1 <28:
    result1 = '偏胖'
else:
    result1 = '肥胖'

if bmi2 < 18.5:
    result2 = '偏瘦'
elif bmi2 >=18.5 and bmi2 <=24:
    result2 = '正常'
elif bmi2 >24 and bmi2 <28:
    result2 = '偏胖'
else:
    result2 = '肥胖'

if bmi3 < 18.5:
    result3 = '偏瘦'
elif bmi3 >=18.5 and bmi3 <=24:
    result3 = '正常'
elif bmi3 >24 and bmi3 <28:
    result3 = '偏胖'
else:
    result3 = '肥胖'
print('{:10s}{:10s}{:10s}{:10s}{:10s}{:10s}'.format('姓名','身高','体重','腰围','BMI指数','分析结果'))
print('{}{:12.2f}{:12.1f}{:10d}{:13.1f}{:>10s}'.format(name1,height1,weight1,waistline1,bmi1,result1))
print('{}{:12.2f}{:12.1f}{:10d}{:13.1f}{:>10s}'.format(name2,height2,weight2,waistline2,bmi2,result2))
print('{}{:12.2f}{:12.1f}{:10d}{:13.1f}{:>10s}'.format(name3,height3,weight3,waistline3,bmi3,result3))