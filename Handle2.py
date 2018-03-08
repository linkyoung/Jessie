#如果两个企业在某一年相联系，可能中间通过了很多人，每个人占原始数据的一行。
#本代码就是计算这些人的salary、allowance等各种信息的是否有、均值、总和等信息。


#coding=gbk

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
    if seq_pre[4] == 'male' : #男性个数
        seq_final[1] = str(int(seq_final[1]) + 1)
    elif seq_pre[4] == 'female' : #女性个数
        seq_final[2] = str(int(seq_final[2]) + 1)

    #在focalfirm中的salary总数
    if seq_pre[6].strip() != 'NA' and seq_pre[6].strip() != '#VALUE!' :
        seq_final[3] = str(float(sumx(float(seq_final[3]),float(seq_pre[6]))))
        seq_assis[3] = str(float(seq_assis[3]) + 1)
	
    #在focalfirm中的salary均值
    if N != 0:
        if seq_pre[6].strip() != 'NA' and seq_pre[6].strip() != '#VALUE!' :
            seq_final[4] = str(float(aver(float(seq_final[4]),float(seq_pre[6]))))
    else:
        if seq_pre[6].strip() != 'NA' and seq_pre[6].strip() != '#VALUE!' :
            seq_final[4] = seq_pre[6]

	#在focalfirm中的allowance总数
    if seq_pre[7].strip() != 'NA' and seq_pre[7].strip() != '#VALUE!' :
        seq_final[5] = str(float(sumx(float(seq_final[5]),float(seq_pre[7]))))
        seq_assis[5] = str(float(seq_assis[5]) + 1)

	#在focalfirm中的allowance均值
    if N != 0:
        if seq_pre[7].strip() != 'NA' and seq_pre[7].strip() != '#VALUE!' :
            seq_final[6] = str(float(aver(float(seq_final[6]),float(seq_pre[7]))))
    else:
        if seq_pre[7].strip() != 'NA' and seq_pre[7].strip() != '#VALUE!' :
            seq_final[6] = seq_pre[7]

	#在focalfirm中的share总数
    if seq_pre[8].strip() != 'NA' and seq_pre[8].strip() != '#VALUE!' :
        seq_final[7] = str(float(sumx(float(seq_final[7]),float(seq_pre[8]))))
        seq_assis[7] = str(float(seq_assis[7]) + 1)

	#在focalfirm中的share均值
    if N != 0:
        if seq_pre[8].strip() != 'NA' and seq_pre[8].strip() != '#VALUE!' :
            seq_final[8] = str(float(aver(float(seq_final[8]),float(seq_pre[8]))))
    else:
        if seq_pre[8].strip() != 'NA' and seq_pre[8].strip() != '#VALUE!' :
            seq_final[8] = seq_pre[8]

	#在focalfirm中的占股比总数
    if seq_pre[9].strip() != 'NA' and seq_pre[9].strip() != '#VALUE!' :
        seq_final[9] = str(float(sumx(float(seq_final[9]),float(seq_pre[9]))))
        seq_assis[9] = str(float(seq_assis[9]) + 1)

	#在focalfirm中的占股比均值
    if N != 0:
        if seq_pre[9].strip() != 'NA' and seq_pre[9].strip() != '#VALUE!' :
            seq_final[10] = str(float(aver(float(seq_final[10]),float(seq_pre[9]))))
    else:
        if seq_pre[9].strip() != 'NA' and seq_pre[9].strip() != '#VALUE!' :
            seq_final[10] = seq_pre[9]

	#在focalfirm中的tenure总数
    if seq_pre[20].strip() != 'NA' and seq_pre[20].strip() != '#VALUE!' :
        seq_final[11] = str(float(sumx(float(seq_final[11]),float(seq_pre[20]))))
        seq_assis[11] = str(float(seq_assis[11]) + 1)

	#在focalfirm中的tenure均值
    if N != 0:
        if seq_pre[20].strip() != 'NA' and seq_pre[20].strip() != '#VALUE!' :
            seq_final[12] = str(float(aver(float(seq_final[12]),float(seq_pre[20]))))
    else:
        if seq_pre[20].strip() != 'NA' and seq_pre[20].strip() != '#VALUE!' :
            seq_final[12] = seq_pre[20]

	#在联系企业中的salary总数
    if seq_pre[22].strip() != 'NA' and seq_pre[22].strip() != '#VALUE!' :
        seq_final[13] = str(float(sumx(float(seq_final[13]),float(seq_pre[22]))))
        seq_assis[13] = str(float(seq_assis[13]) + 1)
	
    #在联系企业中的salary均值
    if N != 0:
        if seq_pre[22].strip() != 'NA' and seq_pre[22].strip() != '#VALUE!' :
            seq_final[14] = str(float(aver(float(seq_final[14]),float(seq_pre[22]))))
    else:
        if seq_pre[22].strip() != 'NA' and seq_pre[22].strip() != '#VALUE!' :
            seq_final[14] = seq_pre[22]

	#在联系企业中的allowance总数
    if seq_pre[23].strip() != 'NA' and seq_pre[23].strip() != '#VALUE!' :
        seq_final[15] = str(float(sumx(float(seq_final[15]),float(seq_pre[23]))))
        seq_assis[15] = str(float(seq_assis[15]) + 1)

	#在联系企业中的allowance均值
    if N != 0:
        if seq_pre[23].strip() != 'NA' and seq_pre[23].strip() != '#VALUE!' :
            seq_final[16] = str(float(aver(float(seq_final[16]),float(seq_pre[23]))))
    else:
        if seq_pre[23].strip() != 'NA' and seq_pre[23].strip() != '#VALUE!' :
            seq_final[16] = seq_pre[23]

	#在联系企业中的share总数
    if seq_pre[24].strip() != 'NA' and seq_pre[24].strip() != '#VALUE!' :
        seq_final[17] = str(float(sumx(float(seq_final[17]),float(seq_pre[24]))))
        seq_assis[17] = str(float(seq_assis[17]) + 1)

	#在联系企业中的share均值
    if N != 0:
        if seq_pre[24].strip() != 'NA' and seq_pre[24].strip() != '#VALUE!' :
            seq_final[18] = str(float(aver(float(seq_final[18]),float(seq_pre[24]))))
    else:
        if seq_pre[24].strip() != 'NA' and seq_pre[24].strip() != '#VALUE!' :
            seq_final[18] = seq_pre[24]

	#在联系企业中的占股比总数
    if seq_pre[25].strip() != 'NA' and seq_pre[25].strip() != '#VALUE!' :
        seq_final[19] = str(float(sumx(float(seq_final[19]),float(seq_pre[25]))))
        seq_assis[19] = str(float(seq_assis[19]) + 1)

	#在联系企业中的占股比均值
    if N != 0:
        if seq_pre[25].strip() != 'NA' and seq_pre[25].strip() != '#VALUE!' :
            seq_final[20] = str(float(aver(float(seq_final[20]),float(seq_pre[25]))))
    else:
        if seq_pre[25].strip() != 'NA' and seq_pre[25].strip() != '#VALUE!' :
            seq_final[20] = seq_pre[25]

	#在联系企业中的tenure总数
    if seq_pre[36].strip() != 'NA' and seq_pre[36].strip() != '#VALUE!' :
        seq_final[21] = str(float(sumx(float(seq_final[21]),float(seq_pre[36]))))
        seq_assis[21] = str(float(seq_assis[21]) + 1)

	#在联系企业中的tenure均值
    if N != 0:
        if seq_pre[36].strip() != 'NA' and seq_pre[36].strip() != '#VALUE!' :
            seq_final[22] = str(float(aver(float(seq_final[22]),float(seq_pre[36]))))
    else:
        if seq_pre[36].strip() != 'NA' and seq_pre[36].strip() != '#VALUE!' :
            seq_final[22] = seq_pre[36]

	#是否有23-32
    for k1 in range(23,33) :
        if seq_pre[k1-13].strip() != 'NA' and seq_pre[k1-13].strip() != '#VALUE!' :
            if seq_pre[k1-13].strip() != '0' :
                seq_final[k1] = '1'
        if seq_pre[k1+3].strip() != 'NA' and seq_pre[k1+3].strip() != '#VALUE!' :
            if seq_pre[k1+3].strip() != '0' :
                seq_final[k1] = '1'

	#数量33-42
    for k2 in range(33,43) :
        if seq_pre[k2-23].strip() != 'NA' and seq_pre[k2-23].strip() != '#VALUE!' :
            seq_final[k2] = str(sumx(float(seq_final[k2]),float(seq_pre[k2-23])))
            seq_assis[k2] = str(float(seq_assis[k2]) + 1)
        else:
            if seq_pre[k2-7].strip() != 'NA' and seq_pre[k2-7].strip() != '#VALUE!' :
                seq_final[k2] = str(sumx(float(seq_final[k2]),float(seq_pre[k2-7])))
                seq_assis[k2] = str(float(seq_assis[k2]) + 1)

	#均值43-52
    if N != 0:
        for k3 in range(43,53) :
            if seq_pre[k3-33].strip() != 'NA' and seq_pre[k3-33].strip() != '#VALUE!' :
                seq_final[k3] = str(aver(float(seq_final[k3]),float(seq_pre[k3-33])))
    else:
        for k3 in range(43,53) :
            if seq_pre[k3-33].strip() != 'NA' and seq_pre[k3-33].strip() != '#VALUE!' :
                seq_final[k3] = seq_pre[k3-33]

	#是否有红53-91
    for k4 in range(53,92) :
        if seq_pre[k4-16].strip() != 'NA' and seq_pre[k4-16].strip() != '#VALUE!' :
            if seq_pre[k4-16].strip() != '0' :
                seq_final[k4] = '1'

	#数量红92-130
    for k5 in range(92,131) :
        if seq_pre[k5-55].strip() != 'NA' and seq_pre[k5-55].strip() != '#VALUE!' :
            seq_final[k5] = str(sumx(float(seq_final[k5]),float(seq_pre[k5-55])))
            seq_assis[k5] = str(float(seq_assis[k5]) + 1)

	#均值红131-169
    if N != 0:
        for k6 in range(131,170) :
            if seq_pre[k6-94].strip() != 'NA' and seq_pre[k6-94].strip() != '#VALUE!' :
                seq_final[k6] = str(aver(float(seq_final[k6]),float(seq_pre[k6-94])))
    else:
        for k6 in range(131,170) :
            if seq_pre[k6-94].strip() != 'NA' and seq_pre[k6-94].strip() != '#VALUE!' :
                seq_final[k6] = seq_pre[k6-94]

    #new
    if seq_pre[76].strip() != 'NA' and seq_pre[76].strip() != '#VALUE!' :
            if seq_pre[76].strip() != '0' :
                seq_final[170] = '1'
    if seq_pre[76].strip() != 'NA' and seq_pre[76].strip() != '#VALUE!' :
            seq_final[171] = str(sumx(float(seq_final[171]),float(seq_pre[76])))
            seq_assis[171] = str(float(seq_assis[171]) + 1)
    
#    if seq_final[0] == '999-2014-600062' :
#        print (seq_final[52])
        
    return seq_final

def cal_aver(seq_final,seq_assis):
    #在focalfirm中的salary均值
    for i in range(3,22,2):
        if float(seq_assis[i]) != 0:
            seq_final[i+1] = str(float(seq_final[i])/float(seq_assis[i]))
        else:
            seq_final[i+1] = 'NA'
	#均值43-52
    for i in range(33,43):
        if float(seq_assis[i]) != 0:
            seq_final[i+10] = str(float(seq_final[i])/float(seq_assis[i]))
        else:
            seq_final[i+10] = 'NA'
	#均值红131-169
    for i in range(92,130):
        if float(seq_assis[i]) != 0:
            seq_final[i+39] = str(float(seq_final[i])/float(seq_assis[i]))
        else:
            seq_final[i+39] = 'NA'
    #new
    seq_final[172] = str(float(seq_final[171])/float(seq_assis[171]))

    return seq_final


f = codecs.open('raw_new.csv','r','utf-8')
#reader = csv.reader(f)

out = codecs.open('out_new.csv','a')

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
        data_final_seq.append(data_pre_seq[0])
        for i in range(172) :
            data_final_seq.append('0')

        data_assis_seq = []
        for n in range(173):
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
        if data_final_seq[0] == '999-2014-600062' :
            print (data_final_seq[52])

        data_final = join_str.join(data_final_seq)
        out.write(data_final)
        out.write("\n")

        data_final_seq = []
        data_final_seq.append(data_seq[0])
        for i in range(172) :
            data_final_seq.append('0')

        data_assis_seq = []
        for n in range(173):
            data_assis_seq.append('0')
        N = 0
    else :
        N = N + 1

    data_pre_seq = []
    data_pre_seq = copy.deepcopy(data_seq)

#    print(line)
#    print(data)


