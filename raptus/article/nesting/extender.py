from Acquisition import aq_parent
from AccessControl import ClassSecurityInfo

from zope.interface import implements
from zope.component import adapts

from archetypes.schemaextender.interfaces import ISchemaExtender
from archetypes.schemaextender.field import ExtensionField

from plone.indexer.interfaces import IIndexer

from Products.Archetypes import atapi
from Products.ZCatalog.interfaces import IZCatalog

from raptus.article.core.interfaces import IArticle
from raptus.article.core.componentselection import ComponentSelectionWidget
from raptus.article.core import RaptusArticleMessageFactory as _

class LinesField(ExtensionField, atapi.LinesField):
    """ LinesField
    """

class BooleanField(ExtensionField, atapi.BooleanField):
    """ BooleanField
    """
    
class BooleanWidget(atapi.BooleanWidget):
    _properties = atapi.BooleanWidget._properties.copy()
    security = ClassSecurityInfo()

    security.declarePublic('isVisible')
    def isVisible(self, instance, mode='view'):
        """ Check if we are contained in an Article
        """
        container = aq_parent(instance)
        if IArticle.providedBy(container):
            return 'visible'
        return 'invisible'

class ArticleExtender(object):
    """ Adds the component selection field to the article content type
    """
    implements(ISchemaExtender)
    adapts(IArticle)

    fields = [
        LinesField('components',
            enforceVocabulary = True,
            vocabulary_factory = 'componentselectionvocabulary',
            storage = atapi.AnnotationStorage(),
            schemata = 'settings',
            widget = ComponentSelectionWidget(
                description = _(u'description_component_selection_article', default=u'Select the components in which this article should be displayed.'),
                label= _(u'label_component_selection', default=u'Component selection'),
            )
        ),
        BooleanField('detail',
            required=False,
            default=True,
            languageIndependent=True,
            storage = atapi.AnnotationStorage(),
            widget = BooleanWidget(
                description = _(u'description_display', default=u'Whether this article has detail content other than title and description and therefore should be linked to from listings or not.'),
                label = _(u'label_display', default=u'Detail'),
            )
        ),
    ]

    def __init__(self, context):
         self.context = context
         
    def getFields(self):
        return self.fields

class Index(object):
    implements(IIndexer)
    adapts(IArticle, IZCatalog)
    def __init__(self, obj, catalog):
        self.obj = obj
    def __call__(self):
        return self.obj.Schema()['components'].get(self.obj)
