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

    def syntax_error(self, tokix=0, message=None):
        lno, token = self.tokens[self.ix]
        print('File:', self.source_name + ';', 'Line', lno + 1)
        print(' ', token[-1].strip('\n'))
        print(' ', ' ' * tokix + '^')
        print('Invalid Syntax', ((': ' + message) if message is not None else ''), sep='')

    # def parse_call(self)

    def parse_ampersand(self, token):
        tokix = 0
        token_length = len(token[-1])
        tok_type = token[1]

        if tok_type == 'n':
            pass

    def parse_backslash(self, token):
        pass

    def parse(self):
        tokens_length = len(self.tokens)
        block_level = 0
        newtokens = [[]]

        while self.ix < tokens_length:
            lno, token = self.tokens[self.ix]
            if token[0] == '\\':
                pass
            elif token[0] == '&':
                self.parse_ampersand
            elif token[0] == ']':
                block_level -= 1
                if block_level < 0:
                    self.syntax_error(message='end block marker without block')
            # elif token
            self.ix += 1

        return newtokens