class Group:

    def __init__(self, name=None, header=None, footer=None, ident=None):
        self.ident = ident
        self.name = name
        self.header = header
        self.footer = footer

    def __eq__(self, other):
        return (self.ident is None or other.ident is None or self.ident == other.ident) and \
               self.name == other.name  # and \
               # self.header == other.header and \
               # self.footer == other.footer

    def __lt__(self, other):
        # Sort None elements too
        if self.ident is None:
            return False
        elif other.ident is None:
            return True
        else:
            return self.ident < other.ident

    def __repr__(self):
        repstr = "{"
        if self.ident is not None:
            repstr += "%s|" % self.ident
        if self.name is not None:
            repstr += "%s|" % self.name
        if self.header is not None:
            repstr += "%s|" % self.header
        if self.footer is not None:
            repstr += "%s|" % self.footer
        repstr = repstr[:-1]
        return repstr + "}"
