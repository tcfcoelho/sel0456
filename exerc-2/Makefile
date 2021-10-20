CFLAGS = `pkg-config --cflags glib-2.0`
LDFLAGS = `pkg-config --libs glib-2.0`
GCC = gcc

ALL = sort

all: $(ALL)

sort: sort.c
	$(GCC) -o $@  $^ $(CFLAGS) $(LDFLAGS)

%.s: %.c
	$(GCC) $(CFLAGS) -S $<

clean:
	rm -f *.o *.s a.out

distclean: clean
	rm -r $(ALL)