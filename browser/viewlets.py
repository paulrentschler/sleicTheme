from zope.component import getMultiAdapter
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import common, content
from Products.CMFCore.utils import getToolByName

class LogoViewlet(common.ViewletBase):
    render = ViewPageTemplateFile('templates/logo.pt')

    def update(self):
        portal_state = getMultiAdapter((self.context, self.request),
                                            name=u'plone_portal_state')

        self.navigation_root_url = portal_state.navigation_root_url()

class FacilityBannerViewlet(common.ViewletBase):
    render = ViewPageTemplateFile('templates/facility_banner.pt')

class FooterViewlet(common.ViewletBase):
    render = ViewPageTemplateFile('templates/footer.pt')

class SearchBoxViewlet(common.SearchBoxViewlet):
    render = ViewPageTemplateFile('templates/searchbox.pt')

class PathBarViewlet(common.PathBarViewlet):
    render = ViewPageTemplateFile('templates/path_bar.pt')
    
class SiteActionsViewlet(common.SiteActionsViewlet):
    render = ViewPageTemplateFile('templates/site_actions.pt')

class PersonalBarViewlet(common.PersonalBarViewlet):
    render = ViewPageTemplateFile('templates/personal_bar.pt')
    
    def update(self):
        common.PersonalBarViewlet.update(self)
        
        mt = getToolByName(self.context, 'portal_membership')
        self.canManagePortlets = mt.checkPermission('Portlets: Manage portlets', self.context)
        self.canManagePortal = mt.checkPermission('Manage portal', self.context)

class DocumentBylineViewlet(content.DocumentBylineViewlet):
    render = ViewPageTemplateFile('templates/document_byline.pt')
    
    def update(self):
        content.DocumentBylineViewlet.update(self)
        
        mt = getToolByName(self.context, 'portal_membership')
        self.canManagePortal = mt.checkPermission('Manage portal', self.context)
        