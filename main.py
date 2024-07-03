import random
#1

list_1 = [1,2,3,4,5,6]
cort = (list_1)
list_1.remove(3)
print(cort)
#tuple - незмінюваний тип даних, тому вкладений список не змінюється


#2

cort_2 = (1,2,3,4,5,6,7,8,10)
for i in cort_2:
    list_2 = []
    cort_3 = (list_2)
    if i%2!=0:
        continue
    list_2.append(i)
    cort_3+=list_2
    print(cort_3)

  
#3

cort_4 = ("a","b","c","d","e")
print(f"кількість букв а - {cort_4.count("a")}")
print(f"кількість букв b - {cort_4.count("b")}")
print(f"кількість букв d - {cort_4.count("d")}")
print(f"кількість букв e - {cort_4.count("e")}")
gmd_list = []
if cort_4.count("c")>-1:
  gmd_list.append(1)
print(gmd_list)

#4

# cort_5 = tuple()



#5


f_list = [3,5,7,9]
n_list = [2,4,6,8]
f_set = set(f_list)
n_set = set(n_list)
print(f_set.union(n_set))
print(f_set.intersection(n_set))
print(f_set.difference(n_set))
print(f_set.symmetric_difference(n_set))


#6

# tuple_1 = (10,15,25,30,40)
# tuple_2 = (15,20,35,40,50)
# set_1 = set(tuple_1)
# set_2 = set(tuple_2)
# print(set_1.isdisjoint(set_2))


#7


gen_list = []
list_f = [8,37,96,28,65]
list_n = [84,747,288,43]
list_m = [9673,748,37,44]
gen_list.append(list_f)
gen_list.append(list_n)
gen_list.append(list_m)
set_f = set(list_f)
set_n = set(list_n)
set_m = set(list_m)
print(set_f.union(set_n,set_m))

#8
a_list = []
b_list = []
c_list = []
d_list = []
e_list = []
f_list = []
g_list = []
h_list = []
i_list = []
j_list = []
for i in range(3):
    a_list.append(random.randint(1,100))
a_cort = tuple(a_list)
for i in range(3):
    b_list.append(random.randint(1,100))
b_cort = tuple(b_list)
for i in range(3):
    c_list.append(random.randint(1,100))
c_cort = tuple(c_list)
for i in range(3):
    d_list.append(random.randint(1,100))
d_cort = tuple(d_list)
for i in range(3):
    e_list.append(random.randint(1,100))
e_cort = tuple(e_list)
for i in range(3):
    f_list.append(random.randint(1,100))
f_cort = tuple(f_list)
for i in range(3):
    g_list.append(random.randint(1,100))
g_cort = tuple(g_list)
for i in range(3):
    h_list.append(random.randint(1,100))
h_cort = tuple(h_list)
for i in range(3):
    i_list.append(random.randint(1,100))
i_cort = tuple(i_list)
for i in range(3):
    j_list.append(random.randint(1,100))
j_cort = tuple(j_list)

cort_list = [a_cort, b_cort,c_cort,d_cort,e_cort,f_cort,g_cort,i_cort,j_cort]
cort_set = set(cort_list)
print(cort_set)



#9

tup = (5,10,15,20)
lt = list(tup)
print(lt)
sum = 0
x = 0
n = 1
d = 1
for i in lt:
    x+=i
    sum = x
print(f"сума - {sum}")
for i in lt:
    d*=i
print(f"добуток - {d}")
for i in lt:
    i+=-16
print(f"середнє арифметичне - {sum/i}")


#10


# c_1 = (1,2,3)
# c_2 = (3,4,5)
# c_3 = (6,7,8)
# c_4 = (9,10,11)
# main_cort = (c_1, c_2, c_3, c_4)
# c_11 = set(c_1)
# c_11.discard(2)
# print(c_11)

#11

# the_list = [1,1,2,2,2,2,2,2,3,3,4,4,5,5,5]
# the_set = set(the_list)
# n_1 = 0
# n_2 = 0
# n_3 = 0
# n_4 = 0
# n_5 = 0
# for i in the_set:
#     if i == 1:
        
# print(f"к-ість чисел 1 - {n_1}")
# for i in the_set:
#     if i == 2:
#         n_2+=1
# print(f"к-ість чисел 2 - {n_2}")
# for i in the_set:
#     if i == 3:
#         n_3+=1
# print(f"к-ість чисел 3 - {n_3}")
# for i in the_set:
#     if i == 4:
#         n_4+=1
# print(f"к-ість чисел 4 - {n_4}")
# for i in the_set:
#     if i == 5:
#         n_5+=1
# print(f"к-ість чисел 5 - {n_5}")