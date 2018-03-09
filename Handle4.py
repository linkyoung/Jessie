#coding=gbk

##原始数据对应raw4.csv


import codecs
import csv
import copy
from itertools import islice

def sumx(x1,x2):
    sumx = x1 + x2
    return sumx

def aver(x1,x2):
    aver = (x1+x2)/2.0
    return aver

def cal(seq_final,seq,seq_pre,N,seq_assis):
    if seq_pre[10] == '1' : #是否有男性
        seq_final[1] = '1'
    if seq_pre[11] == '1' : #是否有女性
        seq_final[2] = '1'
    if seq_pre[10] == '1' : #男性数量
        seq_final[3] = str(int(seq_final[3]) + 1)
    if seq_pre[11] == '1' : #女性数量
        seq_final[4] = str(int(seq_final[4]) + 1)

    #focalfirm中的salary等总数、均值的总数
    for k1 in range(7,17) :
        if seq_pre[k1+5].strip() != 'NA' and seq_pre[k1+5].strip() != '#VALUE!' :
            seq_final[k1] = str(sumx(float(seq_final[k1]),float(seq_pre[k1+5])))
            seq_assis[k1] = str(float(seq_assis[k1]) + 1)

    #联系企业中的salary等总数、均值的总数
    for k1 in range(27,37) :
        if seq_pre[k1-5].strip() != 'NA' and seq_pre[k1-5].strip() != '#VALUE!' :
            seq_final[k1] = str(sumx(float(seq_final[k1]),float(seq_pre[k1-5])))
            seq_assis[k1] = str(float(seq_assis[k1]) + 1)


	#是否有（是否有背景）
    for k1 in range(47,56) :
        if seq_pre[k1-15].strip() != 'NA' and seq_pre[k1-15].strip() != '#VALUE!' :
            if seq_pre[k1-15].strip() != '0' :
                seq_final[k1] = '1'


	#数量（是否有背景）
    for k2 in range(56,65) :
        if seq_pre[k2-24].strip() != 'NA' and seq_pre[k2-24].strip() != '#VALUE!' :
            seq_final[k2] = str(sumx(float(seq_final[k2]),float(seq_pre[k2-24])))
            seq_assis[k2] = str(float(seq_assis[k2]) + 1)

	#是否有（是否有-English）
    for k1 in range(74,114) :
        if seq_pre[k1-33].strip() != 'NA' and seq_pre[k1-33].strip() != '#VALUE!' :
            if seq_pre[k1-33].strip() != '0' :
                seq_final[k1] = '1'


	#数量（是否有-English）
    for k2 in range(114,154) :
        if seq_pre[k2-73].strip() != 'NA' and seq_pre[k2-73].strip() != '#VALUE!' :
            seq_final[k2] = str(sumx(float(seq_final[k2]),float(seq_pre[k2-73])))
            seq_assis[k2] = str(float(seq_assis[k2]) + 1)

    #总数最后
    if seq_pre[81].strip() != 'NA' and seq_pre[81].strip() != '#VALUE!' :
            seq_final[194] = str(sumx(float(seq_final[194]),float(seq_pre[81])))
            seq_assis[194] = str(float(seq_assis[194]) + 1)
    if seq_pre[82].strip() != 'NA' and seq_pre[82].strip() != '#VALUE!' :
            seq_final[196] = str(sumx(float(seq_final[196]),float(seq_pre[82])))
            seq_assis[196] = str(float(seq_assis[196]) + 1)
    if seq_pre[83].strip() != 'NA' and seq_pre[83].strip() != '#VALUE!' :
            seq_final[198] = str(sumx(float(seq_final[198]),float(seq_pre[83])))
            seq_assis[198] = str(float(seq_assis[198]) + 1)
    if seq_pre[84].strip() != 'NA' and seq_pre[84].strip() != '#VALUE!' :
            seq_final[200] = str(sumx(float(seq_final[200]),float(seq_pre[84])))
            seq_assis[200] = str(float(seq_assis[200]) + 1)
        
    return seq_final

def cal_aver(seq_final,seq_assis):
    #男女性比例
    seq_final[5] = str(float(seq_final[3])/(float(seq_final[3])+float(seq_final[4])))
    seq_final[6] = str(float(seq_final[4])/(float(seq_final[3])+float(seq_final[4])))

    #在focalfirm中的salary等总数均值的均值
    for i in range(17,27):
        if float(seq_assis[i-10]) != 0:
            seq_final[i] = str(float(seq_final[i-10])/float(seq_assis[i-10]))
        else:
            seq_final[i-10] = 'NA'
            seq_final[i] = 'NA'

    #在联系企业中的salary等总数均值的均值
    for i in range(37,47):
        if float(seq_assis[i-10]) != 0:
            seq_final[i] = str(float(seq_final[i-10])/float(seq_assis[i-10]))
        else:
            seq_final[i-10] = 'NA'
            seq_final[i] = 'NA'

    #均值（是有有背景）
    for i in range(65,74):
        if float(seq_assis[i-9]) != 0:
            seq_final[i] = str(float(seq_final[i-9])/float(seq_assis[i-9]))
        else:
            seq_final[i-18] = 'NA'
            seq_final[i-9] = 'NA'
            seq_final[i] = 'NA'

    #均值（是有有-English）
    for i in range(154,194):
        if float(seq_assis[i-40]) != 0:
            seq_final[i] = str(float(seq_final[i-40])/float(seq_assis[i-40]))
        else:
            seq_final[i-80] = 'NA'
            seq_final[i-40] = 'NA'
            seq_final[i] = 'NA'

    #均值最后
    seq_final[195] = str(float(seq_final[194])/float(seq_assis[194]))
    seq_final[197] = str(float(seq_final[196])/float(seq_assis[196]))
    seq_final[199] = str(float(seq_final[198])/float(seq_assis[198]))
    seq_final[201] = str(float(seq_final[200])/float(seq_assis[200]))

    return seq_final


f = codecs.open('raw.csv','r','utf-8')
#reader = csv.reader(f)

out = codecs.open('out_20180309.csv','a')

join_str = ";"
data_pre_seq = []
data_final_seq = []
data_assis_seq = []
N = 0

for line in islice(f,1,None):
    line = line.strip()
#    print(line)
    
    data_seq = line.split(';')
#    print(data_seq)
#    data_final_seq = copy.deepcopy(data_seq)
#    print(data_final_seq)

#    if len(data_seq) == 0 or len(data_pre_seq) == 0:
    if len(data_pre_seq) == 0:
        data_pre_seq = copy.deepcopy(data_seq)
#        print(data_pre_seq)
        continue
	

    if len(data_final_seq) == 0 :
        data_final_seq = []
        data_final_seq.append(data_pre_seq[1])
        for i in range(201) :
            data_final_seq.append('0')

        data_assis_seq = []
        for n in range(202):
            data_assis_seq.append('0')
        N = 0

    data_final_seq = cal(data_final_seq,data_seq,data_pre_seq,N,data_assis_seq)
#    print (data_final_seq)

    if len(data_seq) == 0 :
        data_final = join_str.join(data_final_seq)
        out.write(data_final)
        out.write("\n")
        break

    if data_seq[0] != data_pre_seq[0]:
        data_final_seq = cal_aver(data_final_seq,data_assis_seq)
#        print(data_final_seq)

        data_final = join_str.join(data_final_seq)
        out.write(data_final)
        out.write("\n")

        data_final_seq = []
        data_final_seq.append(data_seq[1])
        for i in range(201) :
            data_final_seq.append('0')

        data_assis_seq = []
        for n in range(202):
            data_assis_seq.append('0')
        N = 0
    else :
        N = N + 1

    data_pre_seq = []
    data_pre_seq = copy.deepcopy(data_seq)

#    print(line)
#    print(data)


