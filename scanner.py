import re


class Scanner:

    def __init__(self) -> None:
        self.separators = []
        self.operators = []
        self.reserved_words = []
        with open('token.in', 'r') as f:
            f.readline()
            for i in range(14):
                self.operators.append(f.readline().strip())
            for i in range(11):
                separator = f.readline().strip()
                if separator == "[space]":
                    separator = " "
                self.separators.append(separator)
            for i in range(19):
                self.reserved_words.append(f.readline().strip())

    def get_string_token(self, line, index):
        token = ''
        quotes = 0

        while index < len(line) and quotes < 2:
            if line[index] == '\'':
                quotes += 1
            token += line[index]
            index += 1

        return token, index

    def is_part_of_operator(self, char):
        for op in self.operators:
            if char in op:
                return True
        return False

    def get_operator_token(self, line, index):
        token = ''

        while index < len(line) and self.is_part_of_operator(line[index]):
            token += line[index]
            index += 1

        return token, index

    def tokenize(self, line):
        token = ''
        index = 0
        tokens = []
        while index < len(line):
            if self.is_part_of_operator(line[index]):
                if token:
                    tokens.append(token)
                token, index = self.get_operator_token(line, index)
                tokens.append(token)
                token = ''

            elif line[index] == '\'':
                if token:
                    tokens.append(token)
                token, index = self.get_string_token(line, index)
                tokens.append(token)
                token = ''

            elif line[index] in self.separators:
                if token:
                    tokens.append(token)
                token, index = line[index], index + 1
                tokens.append(token)
                token = ''

            else:
                token += line[index]
                index += 1
        if token:
            tokens.append(token)
        return tokens

    def is_identifier(self, token):
        return re.match(r'^[a-z]([a-zA-Z]|[0-9])*$', token) is not None

    def is_constant(self, token):
        return re.match(r'^(0|[+-]?[1-9][0-9]*)$|^\'.\'$|^\'.*\'$', token) is not None