import math
import csv
import time

a = []
direct = []
airports = set()

def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6378.137  # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d

with open("hangban.csv") as file:
    reader = csv.reader(file)
    for i in reader:
        try:
            origin = [float(i[1]), float(i[2])]
            destination = [float(i[4]), float(i[5])]
            result = distance(origin, destination)
            # 记录出发城市到达城市的距离
            a.append([i[0], i[3], result])
            # 记录机场
            airports.add(i[12])
            airports.add(i[15])

            has_connect = [i[12], i[15]]
            set_has = set(has_connect)
            if set_has not in direct:
                direct.append(set_has)
        except:
            pass

far = []
close = []

a.sort(key=lambda x: x[2], reverse=True)
for i in a:
    first_record = [i[0], i[1], i[2]]
    second_record = [i[1], i[0], i[2]]
    if first_record in far or second_record in far:
        pass
    else:
        far.append(first_record)
    if len(far) > 20:
        break

a.sort(key=lambda x: x[2])
for i in a:
    first_record = [i[0], i[1], i[2]]
    second_record = [i[1], i[0], i[2]]
    if first_record in close or second_record in close:
        pass
    else:
        close.append(first_record)
    if len(close) > 20:
        close.sort(key=lambda x: x[2], reverse=True)
        break

print('距离最远的20个城市:')
for i in far:
    print('%s 到 %s 的距离为: %.2f km' % (i[0], i[1], i[2]), end='\n')
print('-' * 50)
print('距离最近的20个城市:')
for i in close:
    print('%s 到 %s 的距离为: %.2f km' % (i[0], i[1], i[2]), end='\n')

# 机场个数
print('')
print('机场个数:' + str(len(airports)))
print('正在计算，请稍等...')

# 存在的所有可能
possibility = []

# 将机场集合转换成列表
airports_list = []
for i in airports:
    airports_list.append(i)

# 遍历出所有可能的组合
for i in airports_list:
    for s in airports_list:
        sett = set([i, s])
        if s != i and sett not in possibility:
            possibility.append(sett)

count = 0
for i in direct:
    for s in possibility:
        if s >= i:
            count += 1
            print('')
            for r in (s & i):
                print(r, end='-->')
            print('有直达航班!')
            print('第%d条记录，一共有%d个直达航班' % (count, len(direct)))
            # 休眠2s
            time.sleep(2)
        else:
            for r in s:
                print(r, end='---')
            print('没有直达航班')

print('计算结束！')
