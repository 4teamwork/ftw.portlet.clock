from plone.portlets.interfaces import IPortletType
from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import IPortletRenderer
from zope.component import getUtility, getMultiAdapter
from ftw.portlet.clock import portlet as clock
from ftw.portlet.clock.testing import (
    FTW_CLOCKPORTLET_INTEGRATION_TESTING)
import unittest2 as unittest
from plone.registry.interfaces import IRegistry


class TestPortlet(unittest.TestCase):
    """Test clock portlet
    """

    layer = FTW_CLOCKPORTLET_INTEGRATION_TESTING

    def test_portlet_type_registered(self):
        portlet = getUtility(
            IPortletType, name='ftw.portlet.clock')
        self.assertEquals(
            portlet.addview, 'ftw.portlet.clock')

    def test_interfaces(self):
        portlet = clock.Assignment()
        self.failUnless(
            clock.IClockPortlet.providedBy(portlet))

    def test_renderer(self, section=''):
        context = self.layer['portal']
        request = self.layer['request']
        view = context.restrictedTraverse('@@plone')
        manager = getUtility(
            IPortletManager, name='plone.rightcolumn', context=context)
        assignment = clock.Assignment()
        renderer = getMultiAdapter(
            (context, request, view, manager, assignment), IPortletRenderer)
        self.assertTrue("portlet sbbclock" in renderer.render())
        registry = getUtility(IRegistry)
        self.assertTrue(registry['ftw.portlet.clock.url'] in renderer.render())

    def test_assignment(self):
        assignment = clock.Assignment()
        self.assertEqual(
            assignment.title,
            u'SBB Clock')
