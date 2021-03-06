# Copyright 2018 jem@seethis.link
# Licensed under the MIT license (http://opensource.org/licenses/MIT)

MAKEFILE_INC += Makefile
MAKEFILE_INC += $(EFM8_PATH)/efm8.mk

ALL_CFLAGS += \
	$(CFLAGS) \
	$(CDEFS) \
	$(INC_PATHS) \
	$(LIB_PATHS) \
	$(OPTIMIZATION) \

C_REL_FILES = $(patsubst %.c,$(OBJ_DIR)/%.rel,$(C_SRC))
ASM_REL_FILES = $(patsubst %.S,$(OBJ_DIR)/%.rel,$(ASM_SRC))
DEP_FILES = $(patsubst %.c,$(OBJ_DIR)/%.dep,$(C_SRC))

REL_FILES = $(C_REL_FILES) $(ASM_REL_FILES)

all: pre_build $(TARGET_HEX) size

.PHONY: pre_build
pre_build:
	@echo "======  Building: $(TARGET_HEX)  ======="
	@echo ">>> CFLAGS:"
	@echo $(CFLAGS)
	@echo ">>> CDEFS:"
	@echo $(CDEFS)
	@echo ">>> INC_PATHS:"
	@echo $(INC_PATHS)
	@echo ">>> LIB_PATHS:"
	@echo $(LIB_PATHS)
	@echo ">>> LFLAGS:"
	@echo $(LFLAGS)
	@echo
	@echo "=== Compiling files ==="

$(REL_FILES): $(MAKEFILE_INC)

# @echo "REL_FILES:"
# @echo $(REL_FILES)


$(TARGET_HEX): $(REL_FILES)
	@echo
	@echo "=== Compiling and linking target hex file==="
	@$(CC) $(ALL_CFLAGS) $(LFLAGS) $(REL_FILES) -o $@
	@mv "$(TARGET).lk" "$(TARGET).map" "$(TARGET).mem" -t $(OBJ_DIR)

.PHONY:
size: $(TARGET_HEX)
	@echo
	@echo "=== Size Information ($(TARGET_HEX))==="
	@$(EFM8_PATH)/scripts/hex-size.sh $< "$(TARG_OBJ).mem" "$(CODE_SIZE)"
	@echo

# rule for c
$(OBJ_DIR)/%.rel: %.c $(EXTRA_DEPENDENCIES)
	@echo "compiling: $<"
	@mkdir -p $(dir $@)
	@$(CC) $(ALL_CFLAGS) -c $< -o $@

# rule for asm
$(OBJ_DIR)/%.rel: %.S $(EXTRA_DEPENDENCIES)
	@mkdir -p $(dir $@)
	$(AS) $(ASFLAGS) $@ $<

# rule for DEP_FILES
# sdcc doesn't pass the -MT flag correctly to the preprocessor, so need to
# call the preprocessor directly to generate dependency files
$(OBJ_DIR)/%.dep: %.c
	@mkdir -p $(dir $@)
	@$(PP) $(INC_PATHS) $(CDEFS) -MM \
		-MT $(basename $@).rel $< -o $@

.PHONY:
clean:
	rm -f $(TARGET_HEX)
	rm -f $(TARG_OBJ).lk
	rm -f $(TARG_OBJ).map
	rm -f $(TARG_OBJ).mem
	rm -fr $(OBJ_DIR)
