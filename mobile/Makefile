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
		-id ./HD/images/\
		-id ./HD/images/Navigation_elements\
		-id ./HD/images/Presentation_views\
		-id ./HD/images/User_Input_Elements\
		-id ./HD/images/Assist_Views\
		-id ./HD/images/Copy_Paste\
		-id ./HD/images/Emoticon\
		-id ./HD/images/Old\
		-sd ./HD/sounds -fd ../objects \
		$(SRC)-$(TARGET)-$$s.edc $(DST)-$(TARGET)-$$s.edj; \
	done
	edje_cc $(EDJE_FLAGS_$(V)) -id default/images/tizen-hd -sd default/sounds -fd ../objects \
		-id ./HD/images/\
		-id ./HD/images/Navigation_elements\
		-id ./HD/images/Presentation_views\
		-id ./HD/images/User_Input_Elements\
		-id ./HD/images/Assist_Views\
		-id ./HD/images/Copy_Paste\
		-id ./HD/images/Emoticon\
		-id ./HD/images/Old\
		default.edc default.edj

clean:
	for s in $(SIZE); do \
		rm -rf $(DST)-$(TARGET)-$$s.*; \
	done
	rm -rf default.edj;\

install:
	mkdir -p $(THEME_DIR)
	for s in $(SIZE); do \
		$(INSTALL) $(DST)-$(TARGET)-$$s.edj $(THEME_DIR); \
	done
	$(INSTALL) default.edj $(THEME_DIR); \

uninstall:
	rm -rf $(THEME_DIR)/

distclean: clean
