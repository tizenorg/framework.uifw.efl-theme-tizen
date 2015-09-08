prefix ?= /usr
INSTALL=install -c
THEME_DIR=$(DESTDIR)/$(prefix)/share/elementary/themes
EDJE_FLAGS_VERBOSE_ =
EDJE_FLAGS_VERBOSE_0 =
EDJE_FLAGS_VERBOSE_1 = -v
EDJE_FLAGS = -no-save
SRC=tizen

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
		-id ./HD/images/\
		-id ./HD/images/Activity_indicator/\
		-id ./HD/images/Activity_indicator/large\
		-id ./HD/images/Activity_indicator/medium\
		-id ./HD/images/Activity_indicator/small\
		-id ./HD/images/Content_views\
		-id ./HD/images/Controls\
		-id ./HD/images/Copy_Paste\
		-id ./HD/images/Emoticon\
		-id ./HD/images/Navigation_elements\
		-id ./HD/images/Popups\
		-sd ./HD/sounds -fd ../objects \
		$(SRC)-$(TARGET)-$$s.edc $(SRC)-$(TARGET)-$$s.edj; \
	done
	edje_cc $(EDJE_FLAGS_$(V)) -id default/images/tizen-hd -sd default/sounds -fd ../objects \
		-id ./WVGA/images/\
		-id ./WVGA/images/Activity_indicator/\
		-id ./WVGA/images/Activity_indicator/large\
		-id ./WVGA/images/Activity_indicator/medium\
		-id ./WVGA/images/Activity_indicator/small\
		-id ./WVGA/images/Content_views\
		-id ./WVGA/images/Controls\
		-id ./WVGA/images/Copy_Paste\
		-id ./WVGA/images/Emoticon\
		-id ./WVGA/images/Navigation_elements\
		-id ./WVGA/images/Popups\
		default.edc default.edj

clean:
	for s in $(SIZE); do \
		rm -rf $(SRC)-$(TARGET)-$$s.*; \
	done
	rm -rf default.edj;\

install:
	mkdir -p $(THEME_DIR)
	for s in $(SIZE); do \
		$(INSTALL) $(SRC)-$(TARGET)-$$s.edj $(THEME_DIR); \
	done
	$(INSTALL) default.edj $(THEME_DIR); \

uninstall:
	rm -rf $(THEME_DIR)/

distclean: clean
