from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base
from plone.memoize.compress import xhtml_compress
from zope.interface import implements
from plone.registry.interfaces import IRegistry
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from datetime import datetime
from zope.component import getUtility
from ftw.portlet.clock import _


class IClockPortlet(IPortletDataProvider):
    """ Clock portlet Interface
    """


class Assignment(base.Assignment):
    implements(IClockPortlet)

    def __init__(self, *args, **kwargs):
        super(Assignment, self).__init__(self, *args, **kwargs)

    @property
    def title(self):
        return _(u"SBB Clock")


class Renderer(base.Renderer):
    _template = ViewPageTemplateFile('portlet.pt')

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)

    def get_swf_url(self):
        registry = getUtility(IRegistry)
        if 'ftw.portlet.clock.url' not in registry:
            return None
        return registry['ftw.portlet.clock.url']

    def getDate(self):
        return datetime.now().strftime("%d.%m.%Y")

    def render(self):
        return xhtml_compress(self._template())


class AddForm(base.NullAddForm):

    def create(self):
        return Assignment()
