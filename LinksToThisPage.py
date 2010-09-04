"""
    LinksToThisPage action

    Redirects to the full search using the linkto: syntax
    to find pages that link to the current page (a.k.a. "backlinks").

    @copyright: 2009 Stefan Simroth

    @license: GNU GPL, to be found at http://www.gnu.org/licenses/gpl.html
"""

from MoinMoin.Page import Page

def execute(pagename, request):
   url = Page(request, pagename).url(request, {'action': 'fullsearch', 'context': '180', 'value': 'linkto:"'+pagename+'"'})
   request.http_redirect(url)

