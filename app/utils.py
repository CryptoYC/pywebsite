class ResponseObj(object):

    def __init__(self, data, code, message):
        self.data = data
        self.code = code
        self.message = message