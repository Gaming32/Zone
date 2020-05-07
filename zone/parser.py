def prepare_tokens(tokens):
    return [(lno, line) for (lno, line) in enumerate(tokens) if line]


def parse_tokens(tokens, source_name='<string>'):
    tokens = prepare_tokens(tokens)
    parser = TokenParser(tokens, source_name=source_name)
    return parser.parse()


class TokenParser:
    def __init__(self, tokens=None, source_name='<string>'):
        self.source_name = source_name
        self.initialized = False
        if tokens is not None:
            self.newtokens(tokens)

    def newtokens(self, tokens):
        self.tokens = tokens
        self.ix = 0
        self.initialized = True

    def syntax_error(self, message=None):
        token_set = self.tokens[self.ix]
        print('File:', self.source_name + ';', 'Line', token_set[0])
        print(' ', token_set[1][-1].strip('\n'))
        print(' ', ' ' * self.ix + '^')
        print('Invalid Syntax', ((': ' + message) if message is not None else ''), sep='')

    def parse(self):
        self.syntax_error()
        return None