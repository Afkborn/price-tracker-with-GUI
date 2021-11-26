from Python.Model.Website import Website


SUPPORTEDWEBSITES = [
    Website("Samm Market", "market.samm.com","teknoloji",True,True),
    Website("Amazon", "www.amazon.com.tr","hepsi",True,False),
    Website("Trendyol", "www.trendyol.com","hepsi",True,False),
    Website("Hepsi Burada", "www.hepsiburada.com","hepsi",True,False)
]


def getSupportedWebsites() -> list:
    """Return list of supported website for tracking"""
    returnList = []
    for i in SUPPORTEDWEBSITES:
        if i.get_tracking_support():
            returnList.append(i.get_domain())
    return returnList


def getSupportedWebsitesForBruteForce() -> list:
    """Return list of supported website for brute force"""
    returnList = []
    for i in SUPPORTEDWEBSITES:
        if i.get_brute_force_support():
            returnList.append(i.get_domain())
    return returnList