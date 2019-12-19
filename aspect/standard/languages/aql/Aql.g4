grammar Aql;

//
fragment A 			: ('A'|'a');
fragment S 			: ('S'|'s');
fragment C 			: ('C'|'c');
fragment D 			: ('D'|'d');
fragment E 			: ('E'|'e');
fragment DIGIT  	: '0'..'9' ;
fragment IDKEY		: ('a'..'z'|'A'..'Z'|'_') ;
fragment ID 		: IDKEY (IDKEY|DIGIT)* ;
fragment INT 		: ('0'..'9')+ ;
fragment EXPONENT 	: E ('+'|'-')? INT ;

//
DESC				: D E S C; 
ASC					: A S C;
IDENTIFIER 			: ID;
INTEGER 			: INT;
FLOAT 				: INT '.' INT EXPONENT? | '.' INT EXPONENT? | INT EXPONENT;
WS 					: ( ' ' | '\t' | '\r' | '\n' )+ -> skip;
STRING_LITERAL		: '\''
					  ( '\'' '\''  | ~('\''|'\n'|'\r')  )*
					  ( '\'' | ) // Error, text literal not closed
					;

queryExpression
	: expression
	;

expression
	: navigateExpression
	;

navigateExpression
	: orExpression
	( 
	  	  ( '.'  IDENTIFIER ('[' orExpression ']' | ) )
	  	| (	'.@' IDENTIFIER	('[' orExpression ']' | ) )
		//( ( '.' /* | '->' | '<-' */ )	orExpression ) 
	)*
	;

orExpression
	: andExpression	( '||' andExpression )*
	;	

andExpression
	: bitOrExpression ( '&&' bitOrExpression )*
	;

bitOrExpression
	: bitXorExpression ( '|' bitXorExpression )*
	;

bitXorExpression
	: bitAndExpression ( '^' bitAndExpression )*
	;
	
bitAndExpression
	: equalsExpression ( '&' equalsExpression )*
	;

equalsExpression 
	: plusExpression
	( '=' plusExpression
	| '!=' plusExpression
	| '=~' plusExpression
	| '>'  plusExpression
	| '<'  plusExpression
	| '>=' plusExpression
	| '<=' plusExpression
	)*
	;

plusExpression
	: multiplyExpression
	( '+' multiplyExpression
	| '-' multiplyExpression
	)*
	;

multiplyExpression
	: unaryExpresion 
	( '*' unaryExpresion
	| '/' unaryExpresion 
	)*
	;

unaryExpresion
	: '-' predicateExpression
	| '!' predicateExpression
	| '~' predicateExpression
	| 	  predicateExpression
	;  

predicateExpression
	: atomExpression ( '[' orExpression ']' )?
	;

atomExpression
	: 'true'
	| 'false'
	| STRING_LITERAL
	| INTEGER
	| FLOAT	
	| '$' IDENTIFIER
	| fieldList	
	| '(' expression ')'
	| IDENTIFIER ( '(' (expressionList)? ')' |	)
	| IDENTIFIER ( '(' ')' | )
	| '@' propertyAccess
	;	

propertyAccess
	: ( ':' )* IDENTIFIER
	;	

expressionList
	: expression ( ',' expression )*
	;

fieldList
	: '{'
	orExpression 
	( ASC | DESC | ':' expression )
	( ',' orExpression ( ASC | DESC | ':' expression )	)*
	'}'
	;
