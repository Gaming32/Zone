import string


one_line_whitespace = ''.join(c for c in string.whitespace
    if c != '\n'
    if c != '\r'
)
ident_starters = string.ascii_letters + '_'


class SourceTokenizer:
    def __init__(self, code=None, source_name='<string>'):
        self.source_name = source_name
        self.initialized = False
        if code is not None:
            self.newcode(code)

    def newcode(self, code):
        self.code = code
        self.ix = 0
        self.col = 0
        self.line = 0
        self.initialized = True

    def syntax_error(self, message=None, offset=0):
        self.line += offset
        print('File:', self.source_name + ';', 'Line', self.line + 1)
        print(' ', self.code.split('\n')[self.line])
        print(' ', ' ' * self.col + '^')
        print('Invalid Syntax', ((': ' + message) if message is not None else ''), sep='')
        self.line -= offset

    def tokenize(self):
        tokens = [[]]
        code_length = len(self.code)
        in_comment = False
        line_state = 0
        in_string = None
        in_string_escape = False

        while self.ix < code_length:
            char = self.code[self.ix]
            if self.code[self.ix-1] == '\n':
                if in_string is not None and in_string != '`':
                    self.syntax_error('string not finished', -1)
                    return None
                self.col = 0
                self.line += 1
                tokens.append([])
                line_state = 0
                in_comment = False
            if in_comment: pass
            elif char == '#' and in_string is None:
                in_comment = True
            elif line_state == 0:
                if char not in string.whitespace:
                    line_state = 1
                    if char == '&':
                        tokens[-1].extend(('&', ''))
                    elif char == '\\':
                        tokens[-1].extend(('\\', ''))
                    elif char in ident_starters:
                        tokens[-1].extend(('&', 'call', char))
                        line_state = 2
                    elif char == ']':
                        tokens[-1].append(']')
                        line_state = -1
                    else:
                        self.syntax_error('invalid line starter: %s' % char)
                        return None
            elif line_state == 1:
                if char == '=':
                    tokens[-1].append('')
                    line_state = 2
                elif char not in one_line_whitespace:
                    tokens[-1][-1] += char
                else:
                    self.syntax_error('Whitespace not allowed in command statement')
                    return None
            elif line_state == 2:
                tokens[-1][-1] += char
                if char == '\\':
                    if in_string:
                        in_string_escape = not in_string_escape
                    else:
                        self.syntax_error('backslash (\\) not allowed outside of string')
                        return None
                elif char == '"':
                    if in_string is None:
                        in_string = '"'
                    elif in_string == '"':
                        if not in_string_escape:
                            in_string = None
                        else:
                            in_string_escape = False
                elif char == "'":
                    if in_string is None:
                        in_string = "'"
                    elif in_string == "'":
                        if not in_string_escape:
                            in_string = None
                        else:
                            in_string_escape = False
                elif in_string is not None and in_string != '`' and in_string_escape:
                    in_string_escape = False
            elif line_state == -1:
                if char not in string.whitespace:
                    self.syntax_error('extra code after end block', -1)
                    return None
            if char != '\n':
                self.col += 1
            self.ix += 1
        if in_string == '`':
            self.syntax_error('raw string not completed')
            return None
        return tokens


if __name__ == '__main__':
    source_file = 'test.z'
    tokenizer = ZoneTokenizer(open(source_file).read(), source_name=source_file)
    tokens = tokenizer.tokenize()
    print(tokens)
    # tokenizer.line = 5
    # tokenizer.col = 11
    # tokenizer.syntax_error('this isn\'t really a syntax error, but I\'m a computer, so I\'ll say it is')