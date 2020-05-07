import pprint


from zone.tokenizer import SourceTokenizer
from zone.parser import prepare_tokens, parse_tokens


SOURCE_FILE = 'test.z'
with open(SOURCE_FILE) as fp:
    source = fp.read()


tokenizer = SourceTokenizer(source, source_name=SOURCE_FILE)
tokens = tokenizer.tokenize()
print('Tokens:', pprint.pformat(tokens))

print()

print('Prepared tokens:', pprint.pformat(prepare_tokens(tokens)))

# print()

# parsed = parse_tokens(tokens, source_name=SOURCE_FILE)
# print('Finished Tokens:', parsed)