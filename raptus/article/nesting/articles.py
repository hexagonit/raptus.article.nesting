from zope import interface, component

from Products.CMFCore.utils import getToolByName

from raptus.article.core.interfaces import IArticle
from raptus.article.nesting.interfaces import IArticles

class Articles(object): 
    """ Provider for articles contained in an article
    """
    interface.implements(IArticles)
    component.adapts(IArticle)
    
    def __init__(self, context):
        self.context = context
        
    def getArticles(self, **kwargs):
        """ Returns a list of articles (catalog brains)
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        return catalog(object_provides=IArticle.__identifier__, path={'query': '/'.join(self.context.getPhysicalPath()),
                                                                      'depth': 1}, sort_on='getObjPositionInParent', **kwargs)
