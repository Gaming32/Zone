def prepare_tokens(tokens):
    return [(lno, line) for (lno, line) in enumerate(tokens) if line]


def token_iter(tokens, source_name='<string>'):
    tokens = prepare_tokens(tokens)
    tokenizer = CommandTokenizer(source_name=source_name)
    for (lno, line) in tokens:
        tokenizer.source_line = lno
        tokenizer.newcode(line)
        yield tokenizer.tokenize()


class CommandTokenizer:
    def __init__(self, code=None, source_name='<string>', source_line=0):
        self.source_name = source_name
        self.source_line = source_line
        self.initialized = False
        if code is not None:
            self.newcode(code)

    def newcode(self, code):
        self.code = code
        self.ix = 0
        self.initialized = True

    def syntax_error(self, message=None):
        print('File:', self.source_name + ';', 'Line', self.source_line)
        print(' ', self.code[-1].strip('\n'))
        print(' ', ' ' * self.ix + '^')
        print('Invalid Syntax', ((': ' + message) if message is not None else ''), sep='')

    def tokenize(self):
        self.syntax_error()
        return None