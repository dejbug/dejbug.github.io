#! /bin/gawk -f

function trim(text) {
	gsub(/^\s+|\s+$/,"", text)
	return text
}

function collapse(text) {
	gsub(/\s+/," ", text)
	return trim(text)
}

/#/ { printf "TITLE " }
/https?:\/\// { printf "URI " }
/\S+/ { printf "TEXT |%s| ", collapse($0) }
/[ \t]/ { printf "WS " }
/./ { printf "EOL " }

END {
	print
}
