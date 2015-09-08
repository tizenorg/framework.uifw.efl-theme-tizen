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
		-id ./$$s/images/Bottom_button\
		-id ./$$s/images/Button\
		-id ./$$s/images/Controller\
		-id ./$$s/images/End_effect\
		-id ./$$s/images/End_effect/Bottom\
		-id ./$$s/images/End_effect/Left\
		-id ./$$s/images/End_effect/Right\
		-id ./$$s/images/End_effect/Top\
		-id ./$$s/images/Indicator\
		-id ./$$s/images/Indicator/Horizontal_dot\
		-id ./$$s/images/List\
		-id ./$$s/images/List/progress\
		-id ./$$s/images/No_items\
		-id ./$$s/images/Option\ popup\
		-id ./$$s/images/Popup\
		-id ./$$s/images/Progress\
		-id ./$$s/images/Progress/Processing_full\
		-id ./$$s/images/Progress/Processing_popup\
		-id ./$$s/images/Progress/Processing_small\
		-id ./$$s/images/Progress/Progress_full\
		-id ./$$s/images/Progress/Progress_popup\
		-id ./$$s/images/Progress/Progress_small\
		-id ./$$s/images/Scroll\
		-id ./$$s/images/Thumbnail\
		-id ./$$s/images/Time_picker\
		-id ./$$s/images/Title_bar\
		-id ./$$s/images/No_items\
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
