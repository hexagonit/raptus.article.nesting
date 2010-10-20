from Products.CMFCore.utils import getToolByName

def install(context):
    """ Adds required catalog metadata and makes articles browsable in kupu
    """
    if context.readDataFile('raptus.article.nesting_install.txt') is None:
        return
    portal = context.getSite()
    
    catalog = getToolByName(portal, 'portal_catalog')
    if 'hasDetail' not in catalog.schema():
        catalog.addColumn('hasDetail')
    
    try: # try updating kupu library tool if available
        kupu = getToolByName(portal, 'kupu_library_tool')
        collection = list(kupu.getPortalTypesForResourceType('collection'))
        if 'Article' not in collection:
            collection.append('Article')
            kupu.updateResourceTypes(({'resource_type' : 'collection',
                                       'old_type'      : 'collection',
                                       'portal_types'  :  collection},))
    except:
        pass