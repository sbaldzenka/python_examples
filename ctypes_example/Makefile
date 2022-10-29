APP = libc_functions.so

OBJECTS = functions.o \
		  sum.o

HEADERS = functions.h \
		  sum.h

all: $(APP)

$(APP): $(OBJECTS)
	gcc -shared -o $@ $^

%.o: %.c $(HEADERS)
	gcc -c -Wall -Wextra -fpic -o $@ $<

clean:
	rm -f $(APP) $(OBJECTS)