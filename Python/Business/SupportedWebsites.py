from Python.Model.Website import Website

import logging

SUPPORTEDWEBSITES = [
    Website("Samm Market", "market.samm.com","teknoloji",True,True),
    Website("Amazon", "www.amazon.com.tr","hepsi",True,False),
    Website("Trendyol", "www.trendyol.com","hepsi",True,False),
    Website("Hepsi Burada", "www.hepsiburada.com","hepsi",True,False)
]

SUPPORTEDUNIT = ["TL","USD","EUR","GBP","JPY","CNY","AUD","CAD","CHF","DKK","HKD","INR","KRW","MYR","NZD","SEK","SGD","THB","ZAR"]

def getSupportedWebsites() -> list:
    """Return list of supported website for tracking"""
    returnList = []
    for i in SUPPORTEDWEBSITES:
        if i.get_tracking_support():
            returnList.append(i.get_domain())
    logging.info("Supported Websites: " + str(returnList))
    return returnList


def getSupportedWebsitesForBruteForce() -> list:
    """Return list of supported website for brute force"""
    returnList = []
    for i in SUPPORTEDWEBSITES:
        if i.get_brute_force_support():
            returnList.append(i.get_domain())
    logging.info("Supported Websites for Brute Force: " + str(returnList))
    return returnList