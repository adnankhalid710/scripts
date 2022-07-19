################
## this file "read_log_file_19.py"is working proper by logic extracted from read_log_file_19.py
################
def time_calculation(str1, str2):
    s1 = str1.split()
    s2 = str2.split()
    c = int(s2[0]) - int(s1[0])
    return c

file_write = open("D:/script/script_files/log_file_reader/new_tracer_19.log", "a+")
j = ['Qussw', 'fadd']
length_dic = len(j)
print("The length of list is :{} given as :{}".format(length_dic, j))
exit()
for i in range(length_dic):
    total_time = 0
    counter = 0
    time_list = []
    file_open = open("D:/script/script_files/log_file_reader/tracer19a.log", "r+")
    while True:
        line = file_open.readline()
        if not line:
            break;
        if j[i] in line:
            counter+=1
            line_n = next(file_open)
            c = time_calculation(line, line_n)
            time_list.append(c)
            total_time += c
            
    file_write.write("\n==================={}==========================".format(j[i]))
    file_write.write("\nThe total {} instructions are {}.".format(j[i], counter))
    file_write.write("\nThe total time taken by {}, is {}.".format(j[i], total_time))
    avg_t = total_time/counter
    file_write.write("\nThe average time taken by {}, is {}.".format(j[i], avg_t))
    file_write.write("\nThe Maximum time taken by {}, is {}.".format(j[i], max(time_list)))
    file_write.write("\nThe Minimum time taken by {}, is {}.".format(j[i], min(time_list)))
    
print("Done, Please check the file named as \'new_tracer_19.txt\' ")
            #exit()

