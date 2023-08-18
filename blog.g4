grammar blog;

fragment WORDCC : [0-9A-Za-z] ;
fragment LINKCC : [-A-Za-z0-9._~:/?#[\]@!$&()+*,;=%'] ; // '
fragment HASHCC : [_0-9A-Za-z] ;

Hash : '#' ;
Punct : ~[ \r\t\n0-9A-Za-z] ;
// Word : Char+ ;
// Char : ~[ \t\r\n] ;
// Char : [0-9A-Za-z] ;
Word : WORDCC+ ;
Link : ( 'http' | 'https' ) '://' LINKCC+ ;
Space : [ \t] ;
Feed : [\r\n] ;
Hashtag : Hash HASHCC+ ;


hash : Hash ;
punct : Punct ;
space : Space ;
feed : Feed ;
link : Link ;


hashtag : Hashtag ;

word : hashtag | punct | link | hash | Word (punct+ Word)* punct* ;

words : word+ (space+ word+)* space* ;

title : Hash+ space* words feed+ ;

line : title | space* words feed+;

start : line* EOF ;
