from ctypes import cdll,c_int
from ctypes.util import find_library
import os
import time
import math



class UseBinary(object):
    """
    Easy interface to use binary code in CPython
    Only for python3
    """
    def __init__(self):
        self.src = os.path.dirname(os.path.abspath(__file__))
        self.library_dict = {}

    def load_library(self,relative_path,slug_name):
        self.library_dict[slug_name] = cdll.LoadLibrary(self.src + "/"+str(relative_path))

    def _create_python_call(self,args_list):
        call = ""
        for i in range(len(args_list)):
            call += str(args_list[i])
            if i < len(args_list)- 1:
                call += ","
        return call

    def use_function(self,function_name,slug_lib_name,args):
        exec("""function = self.library_dict[slug_lib_name].{f_name}""".format(f_name=function_name))
        args_list = []
        str_args_list= []
        type_args_list = []
        nb_int_array = 0
        for arg in args:
            try:
                arg[0]
                Array_class_int = (c_int * len(arg))
                int_array = Array_class_int(*arg)
                args_list.append(int_array)
                str_args_list.append("args_list["+str(nb_int_array)+"]")
                type_args_list.append(Array_class_int)
                nb_int_array += 1
            except:
                if not isinstance(arg,str):
                    args_list.append(arg)
                    str_args_list.append("args_list["+str(nb_int_array)+"]")
                    type_args_list.append(c_int)
                    nb_int_array+= 1

        assert(len(args_list) == len(args))
        locals()['function'].argtypes = type_args_list
        call = self._create_python_call(str_args_list)
        exec("""function({args})""".format(args=call))
        return_list = []
        for arg in args_list:
            try:
                return_list.append([arg[i] for i in range(len(arg))])
            except:
                continue
        return return_list
