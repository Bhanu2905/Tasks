import logging


class string:
    def __int__(self, str):
        self.str=str
try:
    def slice(self):
        return self.str[1:300:3]
    def rev(self):
        return self.str[-1:0:-1]
    def convert(self):
        upper_str=self.str.upper()
        return upper_str()
    def lower(self):
        return self.str.lower()
except Exception as e:
    logging.exception(e)

