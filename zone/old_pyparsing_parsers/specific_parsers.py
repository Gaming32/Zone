from pyparsing import *


varname = Word(alphas+"_", alphanums+"_").setName('variableName')


def parse_call_string(s, loc, toks):
    return toks


object_syntax = Forward()


call_function = Forward().setName('func_call')
call_function <<= varname
call_function << nestedExpr(content=delimitedList(object_syntax))


call_constructor = Forward().setName('class_call')
call_constructor <<= varname
call_constructor << nestedExpr('{', '}', content=delimitedList(object_syntax))


call = Or([
    call_function,
    call_constructor,
])


advanced_string_syntax = QuotedString('`', multiline=True, convertWhitespaceEscapes=False).setName('`string`')
string_syntax = (quotedString ^ advanced_string_syntax).setName('string')


object_syntax <<= Or([
    string_syntax,
    call,
])


new_parser = [
    varname,
    Literal('=').suppress().setName('='),
    object_syntax,
]
new_parser = And(new_parser)