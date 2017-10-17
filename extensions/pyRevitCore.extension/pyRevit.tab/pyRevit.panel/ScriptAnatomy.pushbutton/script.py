"""Opens the Anatomy of a Script page in the default browser."""

from pyrevit import coreutils


__context__ = 'zerodoc'
__title__ = 'Script\nAnatomy'


url = 'http://eirannejad.github.io/pyRevit/anatomyofpyrevitscript/'
coreutils.open_url(url)
