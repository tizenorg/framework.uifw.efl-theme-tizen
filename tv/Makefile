prefix ?= /usr
INSTALL=install -c
THEME_DIR=$(DESTDIR)/$(prefix)/share/elementary/themes
EDJE_FLAGS_VERBOSE_ =
EDJE_FLAGS_VERBOSE_0 =
EDJE_FLAGS_VERBOSE_1 = -v
EDJE_FLAGS = -no-save
SRC=tizen
DST=tizen-$(TIZEN_VER)

all:
	for s in $(SIZE); do \
		cp $(SRC).edc $(SRC)-$(TARGET)-$$s.edc; \
		perl -pi -e "s/TIZEN_TMP_INC/\"$$s-inc.edc\"/g" $(SRC)-$(TARGET)-$$s.edc; \
		edje_cc $(EDJE_FLAGS) $(EDJE_FLAGS_$(V))\
		-id ./$$s/images/\
		-id ./$$s/images/Activity_indicator/\
		-id ./$$s/images/Activity_indicator/large\
		-id ./$$s/images/Activity_indicator/medium\
		-id ./$$s/images/Activity_indicator/small\
		-id ./$$s/images/Content_views\
		-id ./$$s/images/Controls\
		-id ./$$s/images/Copy_Paste\
		-id ./$$s/images/Emoticon\
		-id ./$$s/images/Navigation_elements\
		-id ./$$s/images/Popups\
		-id ./$$s/images/Indicator\
		-sd ./$$s/sounds -fd ../objects \
		$(SRC)-$(TARGET)-$$s.edc $(DST)-$(TARGET)-$$s.edj; \
	done
		-id ./UHD/images/\
		-id ./UHD/images/Activity_indicator/\
		-id ./UHD/images/Activity_indicator/large\
		-id ./UHD/images/Activity_indicator/medium\
		-id ./UHD/images/Activity_indicator/small\
		-id ./UHD/images/Content_views\
		-id ./UHD/images/Controls\
		-id ./UHD/images/Copy_Paste\
		-id ./UHD/images/Emoticon\
		-id ./UHD/images/Navigation_elements\
		-id ./UHD/images/Popups\

clean:
	for s in $(SIZE); do \
		rm -rf $(DST)-$(TARGET)-$$s.*; \
	done

install:
	mkdir -p $(THEME_DIR)
	for s in $(SIZE); do \
		$(INSTALL) $(DST)-$(TARGET)-$$s.edj $(THEME_DIR); \
	done

uninstall:
	rm -rf $(THEME_DIR)/

distclean: clean
