#Simple compilation of our c function to binary
lib: my_library.o
	ld -shared -o my_library.so my_library.o
my_library.o: my_library.c
	gcc -c -O3 my_library.c -o my_library.o

clean:
	/bin/rm my_library.o
