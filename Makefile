#TARGET will be got from spec
#2.2 is redwood
#2.3-mobile is redwood lite
#2.3-wearable is B3
#TARGET = 2.2 2.3-mobile 2.3-wearable

all:
	for t in $(TARGET); do \
		cd $$t && make $@ TARGET=$$t && cd -; \
	done

install:
	for t in $(TARGET); do \
		cd $$t && make $@ TARGET=$$t && cd -; \
	done

uninstall:
	for t in $(TARGET); do \
		cd $$t && make $@ TARGET=$$t && cd -; \
	done

clean:
	for t in $(TARGET); do \
		cd $$t && make $@ TARGET=$$t && cd -; \
	done

distclean: clean

.PHONY:
	$(TARGET)
