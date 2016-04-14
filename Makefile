#Simple compilation of our c function to binary
lib: my_library.o
	ld -shared -o my_library.so my_library.o
my_library.o: my_library.c
