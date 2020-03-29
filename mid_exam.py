
#读文件，添加总分和平均分两列
with open('report.txt',encoding='utf-8') as f:
    i = 0
    list_lines = []
    for line in f.readlines():
        if line:
            list_line = line.split()
            i += 1
            if i > 1:
                all_score = 0
                for j in range(1,len(list_line)):
                    list_line[j] = int(list_line[j])
                    all_score += list_line[j]
                    average_score = all_score/(len(list_line)-1)
                list_line.append(all_score)
                list_line.append(float('%.1f' %average_score))
            elif i == 1:
                list_line.append('总分')
                list_line.append('平均分')
            list_lines.append(list_line)
            list1 = sorted(list_lines[1:],key=lambda x:x[-1],reverse=True)
            list1.insert(0,list_lines[0])
#添加名次列
list2 = []
n = 0
for m in list1:
    n += 1
    if n == 1:
        m.insert(0,'名次')
    else:
        m.insert(0,n-1)
    list2.append(m)
#定义一个算一科平均分的函数
def subject_ave_score(rank,list=list2):
    all = 0
    for k in range(1,len(list)):
        listin = list[k]
        all += listin[rank]
    average = all/(len(list)-1)
    if rank == len(listin):
        ave = round(average,1)
    elif rank >= 2:
        ave = int(average)
    else:
        print('ERROR')
    return ave
#用函数得出第二行每科平均分
line2 = [0,'平均']
for l in range(len(list_line)):
    if l > 1:
        line2.append(subject_ave_score(l))
#所有数据计算完毕，在list2里
list2.insert(1,line2)
#小于60用“不及格”替换
for p in list2[2:]:
    for q in range(2,len(p)):
        if p[q] < 60:
            p[q] = '不及格'
#写入新文件
with open('result.txt','w',encoding='utf-8') as fi:
    for r in list2:
        for s in r:
            fi.writelines(str(s)+' ')
        fi.write('\n')