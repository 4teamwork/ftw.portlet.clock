from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import setRoles, TEST_USER_ID, TEST_USER_NAME, login
from zope.configuration import xmlconfig


class FtwClockPortletLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import ftw.portlet.clock

        xmlconfig.file(
            'configure.zcml', ftw.portlet.clock,
                context=configurationContext)

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        applyProfile(portal, 'ftw.portlet.clock:default')

        setRoles(portal, TEST_USER_ID, ['Manager'])
        login(portal, TEST_USER_NAME)

FTW_CLOCKPORTLET_FIXTURE = FtwClockPortletLayer()
FTW_CLOCKPORTLET_INTEGRATION_TESTING = IntegrationTesting(
    bases=(FTW_CLOCKPORTLET_FIXTURE,), name="FtwClockPortletLayer:Integration")
