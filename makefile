# make reset
# make awk
# make blog
# make debug tree blog

# Add more flags by PREPENDing with combinations of:
#	tokens, tree, sll, trace, diagnostics, debug (trace + diagnostics)
# E.g. make trace diagnostics tokens blog-

# Another way to call into PYGRUN (e.g. for grammar blog):
#	make blog-tokens ; make blog-sll ; make blog-trace ; make blog-tree
# E.g. make debug blog-tokens

# GENERAL NOTE on pygrun: Tokens are always printed first,
#	afterwards come the debug and trace (interleaved).
#	The tree is printed last.

GrammarFiles := $(wildcard *.g4)
GrammarNames := $(GrammarFiles:%.g4=%)
ParserFiles =

.PHONY : all clean reset run
all : build/index.html | archive
clean :
	rm -f parsers/*/*.interp parsers/*/*.tokens
	rm -rf build
reset : | clean ; rm -rf parsers
run : build/index.html ; cd build && php -S localhost:8000

# %/ : ; mkdir -p $@

build/index.html : index.template *.md *.py | build/ ; python render.py -do $@ $< ACTOR=makefile
build/ : ; mkdir build

ArchiveSources = $(wildcard archive/*.md)
ArchiveTargets = $(ArchiveSources:archive/%.md=build/archive/%.html)
ArchiveTargetNames = $(ArchiveSources:archive/%.md=%)

.PHONY : archive
archive : $(ArchiveTargets) | build/archive/
build/archive/ : ; mkdir -p $@

# This is just a HACK. Provide for this in render.py .
build/archive/%.html : archive/%.md index.template *.py | build/archive/
	cp $(word 1,$^) $(dir $@)blog.md
	cp $(word 2,$^) $(dir $@)
	cp *.py $(dir $@)
	cd $(dir $@) && python render.py -do $(notdir $@) $(notdir $(word 2,$^)) ACTOR=makefile

.PHONY : awk gawk
awk gawk : ; @gawk -f blog.awk -- blog.md

define deriveParserFiles
parsers/$1/$1Listener.py parsers/$1/$1Lexer.py parsers/$1/$1Parser.py
endef

define makeParserRule
$(eval ParserFiles += $(call deriveParserFiles,$1))
$(call deriveParserFiles,$1) : $1.g4 ; antlr4 -o parsers/$1 -Dlanguage=Python3 $$<
endef

define makeParserCommand
.PHONY : $1
$1 : $(call deriveParserFiles,$1) ; @cd parsers/blog && pygrun -eutf8 blog start $2 -- ../../blog.md
endef

PYGRUN_FLAGS :=

.PHONY : tokens trace tree sll diag diagnostics debug
tokens : ; $(eval PYGRUN_FLAGS += --tokens) @echo -n
trace : ; $(eval PYGRUN_FLAGS += -a) @echo -n
tree : ; $(eval PYGRUN_FLAGS += -t) @echo -n
sll : ; $(eval PYGRUN_FLAGS += -s) @echo -n
diag diagnostics : ; $(eval PYGRUN_FLAGS += -d) @echo -n
debug : trace diagnostics ; @echo -n

define makeParserCommands
.PHONY : $1 $1-tokens $1-trace $1-tree
$1 : $(call deriveParserFiles,$1) ; @cd parsers/blog && pygrun -eutf8 blog start $$(PYGRUN_FLAGS) -- ../../blog.md
$1-tokens : $(call deriveParserFiles,$1) ; @cd parsers/blog && pygrun -eutf8 blog start --tokens $$(PYGRUN_FLAGS) -- ../../blog.md
$1-trace : $(call deriveParserFiles,$1) ; @cd parsers/blog && pygrun -eutf8 blog start $2 -a $$(PYGRUN_FLAGS) -- ../../blog.md
$1-tree : $(call deriveParserFiles,$1) ; @cd parsers/blog && pygrun -eutf8 blog start $2 -t $$(PYGRUN_FLAGS) -- ../../blog.md
$1-sll : $(call deriveParserFiles,$1) ; @cd parsers/blog && pygrun -eutf8 blog start $2 -s $$(PYGRUN_FLAGS) -- ../../blog.md
endef

# $(foreach name,$(GrammarNames),$(info $(call makeParserRule,$(name))))
$(foreach name,$(GrammarNames),$(eval $(call makeParserRule,$(name))))

# $(foreach name,$(GrammarNames),$(info $(call makeParserCommands,$(name))))
$(foreach name,$(GrammarNames),$(eval $(call makeParserCommands,$(name))))
