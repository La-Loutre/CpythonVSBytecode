from use_binary import UseBinary

ub = UseBinary()
ub.load_library("my_library.so","simple_lib")
result = ub.use_function("add_one","simple_lib",[[0,1,2,3,4,5,6,7,8,9],10])
print(result)
result = ub.use_function("multiply_by","simple_lib",[[0,1,2,3,4,5,6,7,8,9],10,5])
print(result)
