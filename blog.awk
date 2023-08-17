#! /bin/gawk -f

BEGIN {
	SEP = "\n"
}

function trim(text) {
	gsub(/^\s+|\s+$/,"", text)
	return text
}

function collapse(text) {
	gsub(/\s+/," ", text)
	return trim(text)
}

/#/ { printf "TITLE" SEP }
/https?:\/\// { printf "URI" SEP }
/\S+/ { printf "TEXT |%s|" SEP, collapse($0) }
/[ \t]/ { printf "WS" SEP }
/./ { printf "EOL" SEP }

END {
	if (SEP !~ "[\r\n]") printf "\n"
}
