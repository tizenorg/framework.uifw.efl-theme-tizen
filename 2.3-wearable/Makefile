prefix ?= /usr
INSTALL=install -c
THEME_DIR=$(DESTDIR)/$(prefix)/share/elementary/themes
EDJE_FLAGS_VERBOSE_ =
EDJE_FLAGS_VERBOSE_0 =
EDJE_FLAGS_VERBOSE_1 = -v
SRC=tizen
SIZE=HVGA

all:
	for s in $(SIZE); do \
		cp $(SRC).edc $(SRC)-$(TARGET)-$$s.edc; \
		perl -pi -e "s/TIZEN_TMP_INC/\"$$s-inc.edc\"/g" $(SRC)-$(TARGET)-$$s.edc; \
		edje_cc $(EDJE_FLAGS_$(V))\
		-id ./$$s/images/\
		-id ./$$s/images/Action_bar\
		-id ./$$s/images/Action_bar/Activity\
		-id ./$$s/images/Body\
		-id ./$$s/images/Button\
		-id ./$$s/images/Controller_icon\
		-id ./$$s/images/List\
		-id ./$$s/images/Overscrolling\
		-id ./$$s/images/Overscrolling/Bottom\
		-id ./$$s/images/Overscrolling/Left\
		-id ./$$s/images/Overscrolling/Right\
		-id ./$$s/images/Overscrolling/Top\
		-id ./$$s/images/Option\ popup\
		-id ./$$s/images/Popup\
		-id ./$$s/images/Progress\
		-id ./$$s/images/Progress/Activity\
		-id ./$$s/images/Scroll\
		-id ./$$s/images/Slider\
		-id ./$$s/images/TimePicker\
		-id ./$$s/images/Title_bar\
		-id ./$$s/images/Search\
		-id ./$$s/images/Focus\
		-id ./$$s/images/temp\
		-id ./$$s/images/temp/Copy_Paste\
		-id ./$$s/images/Emoticon\
		-id ./$$s/images/temp/swipe\
		-id ./$$s/images/Map\
		-sd ./$$s/sounds -fd ../objects \
		$(SRC)-$(TARGET)-$$s.edc $(SRC)-$(TARGET)-$$s.edj; \
	done

clean:
	for s in $(SIZE); do \
		rm -rf $(SRC)-$(TARGET)-$$s.*; \
	done

install:
	mkdir -p $(THEME_DIR)
	for s in $(SIZE); do \
		$(INSTALL) $(SRC)-$(TARGET)-$$s.edj $(THEME_DIR); \
	done

uninstall:
	rm -rf $(THEME_DIR)/

distclean: clean
