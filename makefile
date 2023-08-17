# make reset
# make awk
# make parse ; make parse blog

GrammarFiles := $(wildcard *.g4)
GrammarNames := $(GrammarFiles:%.g4=%)
ParserFiles =

.PHONY : all clean reset
all : ; python blog.py blog.md index.template index.html
clean : ; rm -f parsers/*/*.interp parsers/*/*.tokens
reset : | clean ; rm -rf parsers

.PHONY : awk gawk
awk gawk : ; @gawk -f blog.awk -- blog.md

.PHONY : parse

ifneq (,$(filter parse,$(MAKECMDGOALS)))

define deriveParserFiles
parsers/$1/$1Listener.py parsers/$1/$1Lexer.py parsers/$1/$1Parser.py
endef

define makeParserRule
$(eval ParserFiles += $(call deriveParserFiles,$1))
$(call deriveParserFiles,$1) : $1.g4 ; antlr4 -o parsers/$1 -Dlanguage=Python3 $$<
.PHONY : $1
$1 : $(ParserFiles) ; @cd parsers/blog && pygrun -eutf8 blog start -- ../../blog.md
$1-tokens : $(ParserFiles) ; @cd parsers/blog && pygrun -eutf8 blog start --tokens -- ../../blog.md
endef

# $(foreach name,$(GrammarNames),$(info $(call makeParserRule,$(name))))
$(foreach name,$(GrammarNames),$(eval $(call makeParserRule,$(name))))

parse : $(ParserFiles)

endif
