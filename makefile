# make reset
# make awk
# make index
# make debug tree index

# Add more flags by PREPENDing with combinations of:
#	tokens, tree, sll, trace, diagnostics, debug (trace + diagnostics)
# E.g. make trace diagnostics tokens index-

# Another way to call into PYGRUN (e.g. for grammar index):
#	make index-tokens ; make index-sll ; make index-trace ; make index-tree
# E.g. make debug index-tokens

# GENERAL NOTE on pygrun: Tokens are always printed first,
#	afterwards come the debug and trace (interleaved).
#	The tree is printed last.

GrammarFiles := $(wildcard *.g4)
GrammarNames := $(GrammarFiles:%.g4=%)
ParserFiles =

.PHONY : all clean reset run
all : build/index.html | archive github
clean :
	rm -f parsers/*/*.interp parsers/*/*.tokens
	rm -rf build
reset : | clean ; rm -rf parsers
run : build/index.html ; cd build && php -S localhost:8000

build/%.html : %.md index.template known.aka.pickle *.py | build/archive/
	python render.py -do $@ index.template source=$<

%.aka.pickle : %.aka ; python known.py -o $@ $<

# %/ : ; mkdir -p $@
build/ : ; mkdir $@
build/archive/ : ; mkdir -p $@

ArchiveSources = $(wildcard archive/*.md)
ArchiveTargets = $(ArchiveSources:archive/%.md=build/archive/%.html)
ArchiveTargetNames = $(ArchiveSources:archive/%.md=%)

.PHONY : archive
archive : $(ArchiveTargets) | build/archive/

.PHONY : github
github : build/github.css build/github.svg
build/github.% : github.% | build/ ; cp $< $@

.PHONY : test
PythonFiles := $(shell find . -iname '*.py')
test : $(PythonFiles) ; python -m doctest $^

.PHONY : awk gawk
awk gawk : ; @gawk -f index.awk -- index.md

define deriveParserFiles
parsers/$1/$1Listener.py parsers/$1/$1Lexer.py parsers/$1/$1Parser.py
endef

define makeParserRule
$(eval ParserFiles += $(call deriveParserFiles,$1))
$(call deriveParserFiles,$1) : $1.g4 ; antlr4 -o parsers/$1 -Dlanguage=Python3 $$<
endef

define makeParserCommand
.PHONY : $1
$1 : $(call deriveParserFiles,$1) ; @cd parsers/index && pygrun -eutf8 blog start $2 -- ../../index.md
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
$1 : $(call deriveParserFiles,$1) ; @cd parsers/index && pygrun -eutf8 index start $$(PYGRUN_FLAGS) -- ../../index.md
$1-tokens : $(call deriveParserFiles,$1) ; @cd parsers/index && pygrun -eutf8 index start --tokens $$(PYGRUN_FLAGS) -- ../../index.md
$1-trace : $(call deriveParserFiles,$1) ; @cd parsers/index && pygrun -eutf8 index start $2 -a $$(PYGRUN_FLAGS) -- ../../index.md
$1-tree : $(call deriveParserFiles,$1) ; @cd parsers/index && pygrun -eutf8 index start $2 -t $$(PYGRUN_FLAGS) -- ../../index.md
$1-sll : $(call deriveParserFiles,$1) ; @cd parsers/index && pygrun -eutf8 index start $2 -s $$(PYGRUN_FLAGS) -- ../../index.md
endef

# $(foreach name,$(GrammarNames),$(info $(call makeParserRule,$(name))))
$(foreach name,$(GrammarNames),$(eval $(call makeParserRule,$(name))))

# $(foreach name,$(GrammarNames),$(info $(call makeParserCommands,$(name))))
$(foreach name,$(GrammarNames),$(eval $(call makeParserCommands,$(name))))
