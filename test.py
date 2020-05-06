from zone.tokenizer1 import ZoneTokenizer
from zone.tokenizer2 import prepare_tokens, token_iter


SOURCE_FILE = 'test.z'
with open(SOURCE_FILE) as fp:
    source = fp.read()


tokenizer = ZoneTokenizer(source, source_name=SOURCE_FILE)
tokens = tokenizer.tokenize()
print('Tokens:', tokens)

# print()

# print('Prepared tokens:', prepare_tokens(tokens))

# print()

# iterable = token_iter(tokens, source_name=SOURCE_FILE)
# print('Finished Tokens:', list(iterable))