from use_binary import UseBinary
from cpythonVSBytecode import show_cpython_vs_binary
import time

ub = UseBinary()
ub.load_library("my_library.so","simple_lib")
result = ub.use_function("add_one","simple_lib",[[0,1,2,3,4,5,6,7,8,9],10])

result = ub.use_function("multiply_by","simple_lib",[[0,1,2,3,4,5,6,7,8,9],10,5])


mat_a = [i for i in range(1000)]
mat_b = [i for i in range(1000)]
repeat = 100
start_mat_add = time.time()
result = ub.use_function("matrice_add_a","simple_lib",[mat_a,10,mat_b,repeat])
end_mat_add = time.time()
binary_time = end_mat_add - start_mat_add

start_mat_add = time.time()
for y in range(repeat):
    for i in range(len(mat_a)):
        mat_a[i]+= mat_b[i]
end_mat_add = time.time()
python_time = end_mat_add - start_mat_add
print("Matrice add result , size mat ="+str(len(mat_a))+",repeat ="+str(repeat))
show_cpython_vs_binary(python_time,binary_time)


mat_a = [i for i in range(1000)]
mat_b = [i for i in range(1000)]
repeat = 1000
start_mat_add = time.time()
result = ub.use_function("matrice_add_a","simple_lib",[mat_a,10,mat_b,repeat])
end_mat_add = time.time()
binary_time = end_mat_add - start_mat_add

start_mat_add = time.time()
for y in range(repeat):
    for i in range(len(mat_a)):
        mat_a[i]+= mat_b[i]
end_mat_add = time.time()
python_time = end_mat_add - start_mat_add
print("\n\nMatrice add result , size mat ="+str(len(mat_a))+",repeat ="+str(repeat))
show_cpython_vs_binary(python_time,binary_time)
