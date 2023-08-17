grammar blog;

fragment SP : [ \t] ;
fragment LF : '\r'? '\n' ;
fragment UrlChars : ~[ \t\r\n] ;
fragment LineChars : ~[\r\n] ;
fragment WordChars : ~[ \t\r\n] ;

TITLE : SP* [#]+ LineChars+ ;
URI : SP* 'http' 's'? '://' UrlChars+ ;
EOL : LF+ ;
WORD : SP* WordChars+ ;

start : firsttitle? item* ;

item :
	URI {print(f'<{$URI.text.strip()}>')} |
	title |
//	words {text = $words.text.replace("\t","\\t"); print(f'({text})')} |
	words {print(f'({$words.text})')} |
	EOL ;

title : EOL TITLE {print(f'[{$TITLE.text}]')} ;

words : WORD+ ;

firsttitle : TITLE {print(f'[{$TITLE.text}]')} ;
