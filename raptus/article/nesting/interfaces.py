from zope import interface

class IArticles(interface.Interface):
    """ Provider for articles contained in an article
    """
    
    def getArticles(**kwargs):
        """ Returns a list of articles (catalog brains)
        """
