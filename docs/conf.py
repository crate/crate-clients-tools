from crate.theme.rtd.conf.crate_clients_tools import *

# Disable version chooser.
html_context.update({
    "display_version": False,
    "current_version": None,
    "versions": [],
})

# TODO: Refactor into global configuration.
linkcheck_ignore = [
    "https://portal.azure.com/",
    "https://azuremarketplace.microsoft.com/",
]

linkcheck_timeout = 5
