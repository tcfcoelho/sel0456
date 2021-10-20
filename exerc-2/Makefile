CFLAGS = `pkg-config --cflags glib-2.0`
LDFLAGS = `pkg-config --libs glib-2.0`
GCC = gcc

ALL = sort

all: $(ALL)

sort: sort.c
	$(GCC) -o $@ $^ $(CFLAGS)	 $(LDFLAGS)

clean:
	rm -rf *~ *.o

distclean: clean
	rm -rf $(ALL)
