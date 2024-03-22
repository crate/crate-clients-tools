from crate.theme.rtd.conf.crate_clients_tools import *

# Disable version chooser.
html_context.update({
    "display_version": False,
    "current_version": None,
    "versions": [],
})

# TODO: Refactor into global configuration.
linkcheck_ignore = [
    # HTTPSConnectionPool(host='xxx.microsoft.com', port=443): Read timed out. (read timeout=5)
    "https://azure.microsoft.com/",
    "https://azuremarketplace.microsoft.com/",
    "https://portal.azure.com/",
    "https://powerbi.microsoft.com",
    "https://www.microsoft.com",
]

linkcheck_timeout = 5
