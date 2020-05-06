from pyparsing import *
# ParserElement.enablePackrat()


from .specific_parsers import *


def statement_parse_function(s, loc, toks):
    if len(toks) < 3:
        toks = ['&', 'call'] + toks
    parser_type, string_to_parse = toks[1:3]
    print(string_to_parse)
    if parser_type == 'n':
        newtoks = new_parser.parseString(string_to_parse)
    elif parser_type == 'call':
        newtoks = call.parseString(string_to_parse)
    else:
        raise ParseFatalException(parser_type, msg='Unsupported call type %s' % parser_type)
    return [parser_type] + list(newtoks)

statement = [
    Literal('&').leaveWhitespace(),
    Word(srange('[a-z]')),
    Literal('=').leaveWhitespace().suppress(),
    restOfLine,
]
statement = And(statement)
statement = statement.setParseAction(statement_parse_function)
# statement = statement.setName('statement')


parser = [
    statement,
    White().suppress(),
]
parser = Or(parser)


if __name__ == '__main__':
    print(parser)
    print(new_parser)
    print()

    file = open('test.z')
    for (lineno, line) in enumerate(file):
        try:
            print(parser.parseString(line))
        except ParseException as err:
            print(err.line)
            print(" " * (err.column - 1) + "^")
            err.lineno = lineno + 1
            print(err)
            break