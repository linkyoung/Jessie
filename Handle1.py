#如果年份、姓名、性别、年龄（+/- 1）共4个属性相等，得出新的一列，表明这个人在某年联系了有多少个不同的企业

# -*- coding: UTF-8 -*-
import csv
import codecs
import copy

def write_csv(line):
    file_out = codecs.open('output.csv','a+','utf-8')
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

    file_out = codecs.open('output.csv','a+','utf-8')

    N = 77070
#    N = 20
    dep = ";"
    diff_stkcd_cnt = 1
    bench_next = ''
    write_seq = []
    stkcd_seq = []

    for i in range(1,N):
#        with open("111.csv","r") as csvfile:
#            reader = csv.reader(csvfile)
#        print(i)
        file = codecs.open('raw.csv','r','utf-8')
        reader = file.readlines()
        bench = copy.deepcopy(bench_next)
        bench_seq = bench.split(";")
        diff_stkcd_cnt = 0
        stkcd_seq = []

        for k,rows in enumerate(reader):
            if k==0:
                continue

            if k==i:
                bench = rows.strip('\r\n')
                bench_seq = bench.split(";")  
                if bench_seq[1] not in stkcd_seq:                 
                    stkcd_seq.append(bench_seq[1])
                    diff_stkcd_cnt = diff_stkcd_cnt + 1
            else:
                if k==i+1:
                    bench_next = rows.strip('\r\n')
                fact = rows.strip('\r\n')
                fact_seq = fact.split(";")
#                print(k)
#                if(k==77070):
#                    print(fact_seq)
                equal = compare(fact_seq[2],bench_seq[2],fact_seq[3],bench_seq[3],fact_seq[4],bench_seq[4],fact_seq[5],bench_seq[5])
                if equal:
                    if fact_seq[1] not in stkcd_seq:
                        stkcd_seq.append(fact_seq[1])
                        diff_stkcd_cnt = diff_stkcd_cnt + 1

            if k >= N:
                print(i)
                break

        write_seq = []
        write_seq.append(bench_seq[3])
        write_seq.append(str(diff_stkcd_cnt))
        write_line = dep.join(write_seq)
#        print(write_seq)
#        print(stkcd_seq)
         
        file_out.write(write_line)
        file_out.write("\n")