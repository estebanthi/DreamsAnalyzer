class MutableString:

    def __init__(self, string):
        self.string = string

    def insert(self, index, text):
        beginning_substring = self.string[:index]
        ending_substring = self.string[index:]
        modified_string = beginning_substring + text + ending_substring
        self.string = modified_string
        return modified_string

    def set_max_line_breaks(self, n=1):
        if n < 1:
            raise ValueError('max should be > 0')
        string_list = self.string.split(''.join(['\n' for i in range(n)]))

        sub = ''
        for line in string_list:
            if line:
                sub += '\n' * n
            sub += line
        self.string = sub
        return sub

    def strip(self, char=None):
        self.string = self.string.strip(char)
        return self.string

    def __repr__(self):
        return self.string
