#原始数据是每个企业每年每个董事的各种信息。
#最终得到的数据是如果一个相同年份，相同年龄，相同性别，年龄相差正负1之内的人将两个企业在某一年联系起来，那么写一行。

# -*- coding: UTF-8 -*-
import csv
import codecs

def write_csv(line):
    file_out = codecs.open('out.csv','a+','utf-8')
#    writer = csv.writer(file_out)
#    writer.writerow(line)
    file_out.writelines(line)
    file_out.writelines("\n")
    file_out.close()
    return

def compare(year1,year2,name1,name2,gender1,gender2,age1,age2):
    if age1=='NA' or age2=='NA':
        return False
    if year1==year2 and name1==name2 and gender1==gender2 and (abs(int(age1)-int(age2)) <= 1):
        return True
    return False


if (__name__ == "__main__"):

    N = 191058
#    N = 20
    dep = ";"

    for i in range(1,N):
#        with open("111.csv","r") as csvfile:
#            reader = csv.reader(csvfile)
        print(i)
        file = codecs.open('112.csv','r','utf-8')
        reader = file.readlines()
        for k,rows in enumerate(reader):
            if k==i:
                linei = rows.strip('\r\n')
                linei_list = linei.split(";")
            elif k>i:
                linej = rows.strip('\r\n')
                linej_list = linej.split(";")
                equal = compare(linei_list[1],linej_list[1],linei_list[2],linej_list[2],linei_list[3],linej_list[3],linei_list[4],linej_list[4])
                if equal:
                    linenew_list = []
                    linenew_list.extend(linei_list)
#                    linej_del_list = linej_list[5:-1]
#                    linenew_list.extend(linej_list[0])
                    linenew_list.extend(linej_list)
                    linenew = dep.join(linenew_list)
                    print (linenew)
                    write_csv(linenew)
                    continue
                else:
                    continue
            if k >= N:
                print(k)
                break


