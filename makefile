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
all : build/index.html build/index.css | archive github extra
clean :
	rm -f parsers/*/*.interp parsers/*/*.tokens
	rm -rf build
reset : | clean ; rm -rf parsers
run : build/index.html ; cd build && php -S localhost:8001

build/index.css : index.css ;
	python render.py -do $@ $<

build/index.html : index.md index.template known.aka.pickle *.py *.style | build/
	python render.py -do $@ index.template source=$<

build/%.html : archive/%.md index.template known.aka.pickle *.py *.style | build/
	python render.py -do $@ index.template source=$<

build/vendor/% : vendor/% ; mkdir -p $(dir $@) && cp $< $@

%.aka.pickle : %.aka known.py ; python known.py -o $@ $<

# %/ : ; mkdir -p $@
build/ : ; mkdir $@

.PHONY : extra
extra : build/sticky.js
build/sticky.js : js/sticky.js build/vendor/underscore/underscore-min.js ; cp $< $@

ArchiveSources = $(wildcard archive/*.md)
ArchiveTargets = $(ArchiveSources:archive/%.md=build/%.html)
ArchiveTargetNames = $(ArchiveSources:archive/%.md=%)

.PHONY : archive
archive : $(ArchiveTargets)

.PHONY : github
github : build/github.css build/github.svg
build/github.% : github.% | build/ ; cp $< $@

.PHONY : test test-doctest test-mypy
PythonFiles := $(shell find . -iname '*.py')
# test : | test-mypy test-doctest
test : | test-doctest
test-mypy-strict : $(PythonFiles) ; -python -m mypy --strict $^
test-mypy : $(PythonFiles) ; -python -m mypy $^
test-doctest : $(PythonFiles) ; -python -m doctest $^

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

TitlesSources := index $(notdir $(basename $(ArchiveSources)))
TitlesTargets := $(TitlesSources:%=titles-%)
.PHONY : $(TitlesTargets)
titles : $(TitlesTargets)
# 	@printf '%s' index.md
# 	@sed -n '/^#/p' index.md
# 	@find archive/*.md -exec printf '\n\n{}' \; -exec sed -n '/^#/p' '{}' \;

titles-index : index.md ; @printf '$<\n' && sed -n '/^#/p' $<
$(filter-out titles-index,$(TitlesTargets)) : titles-% : archive/%.md ; @printf '\n\n$<\n' && sed -n '/^#/p' $<
