class hasDetail(object):
    def __init__(self, context, catalog):
        self.context = context
    def __call__(self):
        return self.context.Schema()['detail'].get(self.context)