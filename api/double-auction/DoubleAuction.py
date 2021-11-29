from typing import List
from constants.OfferType import * 
from constants.ItemIds import *
from models.Offer import * 
from models.ListingOfOffers import * 


print('test')
print(OfferType.BUY == 0)
print(OfferType.BUY.value == 0)

listingOfOffers = ListingOfOffers()


mySellOffer1 = Offer()
mySellOffer1.setOfferDetails(OfferType.SELL, ItemIds.DAGGER, 999)

mySellOffer2 = Offer()
mySellOffer2.setOfferDetails(OfferType.SELL, ItemIds.DAGGER, 1001)

mySellOffer3 = Offer()
mySellOffer3.setOfferDetails(OfferType.SELL, ItemIds.DAGGER, 997)


myBuyOffer1 = Offer()
myBuyOffer1.setOfferDetails(OfferType.BUY, ItemIds.DAGGER, 1000)

myBuyOffer2 = Offer()
myBuyOffer2.setOfferDetails(OfferType.BUY, ItemIds.SWORD, 1500)

myBuyOffer3 = Offer()
myBuyOffer3.setOfferDetails(OfferType.BUY, ItemIds.DAGGER, 1000)

myBuyOffer4 = Offer()
myBuyOffer4.setOfferDetails(OfferType.BUY, ItemIds.DAGGER, 1000)


print("\n\n\n test further")


listingOfOffers.addOffer(mySellOffer1)
listingOfOffers.addOffer(mySellOffer2)
listingOfOffers.addOffer(mySellOffer3)

listingOfOffers.addOffer(myBuyOffer1)
listingOfOffers.addOffer(myBuyOffer2)
listingOfOffers.addOffer(myBuyOffer3)
listingOfOffers.addOffer(myBuyOffer4)
