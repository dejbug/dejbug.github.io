grammar blog;

fragment SP : [ \t] ;
fragment LF : '\r'? '\n' ;
fragment UrlChars : ~[ \t\r\n] ;
fragment LineChars : ~[\r\n] ;
fragment WordChars : ~[ \t\r\n] ;


/*
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
*/

fragment HS : [ \t] ;
fragment VS : [\r\n] ;
fragment PUNCT : [,;.:!?<>] ;
fragment LINKCC : [-A-Za-z0-9._~:/?#[\]@!$&()+*,;=%'] ; // '
fragment LINECC : ~[\r\n] ;
fragment WORDCC : ~( [ \t] | [\r\n] | [,;.:!?] ) ;

// ANY : . -> skip ;

/*
Link : ( 'http' | 'https' ) '://' LINKCC+ HS* ; // {print(f'LINK |{$LINKCC.text}|')} ;

FirstTitle : Title ;
InnerTitle : VS+ Title ;
Title : '#'+ HS* LINECC+ ; // {print(f'TITLE |{$LINECC.text}|')} ;
Text : VS+ ( HS* LINECC+ )+ ; // {print(f'TEXT |{$LINECC.text}|')} ;

item : Link
	| Title {print(f'TITLE |{$Title.text}|')}
	| Text ;

start : FirstTitle? item* EOF ;
*/

Hash : '#' ;
Punct : ~[ \r\t\n0-9A-Za-z] ;
// Char : ~[ \t\r\n] ;
Char : [0-9A-Za-z] ;
Word : Char+ ;
Link : ( 'http' | 'https' ) '://' LINKCC+ ;
Space : [ \t] ;
Feed : [\r\n] ;


hash : Hash ;
punct : Punct ;
// word : Char+ ;
space : Space ;
feed : Feed ;

word : Word (punct+ Word?)* ;

title : hash+ (space* word)+ ;
link : Link ;
// text : (space | punct) text | word ;
// white : space | feed ;

item : title | link | word | space | punct ;

line : space* item+ feed+;

start : line* EOF ;
