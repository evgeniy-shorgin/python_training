class Group:

    def __init__(self, name=None, header=None, footer=None, ident=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.ident = ident

    def __eq__(self, other):
        return self.name == other.name and \
               self.ident == other.ident and \
               self.header == other.header and \
               self.footer == other.footer

    def __lt__(self, other):
        return self.ident < other.ident
