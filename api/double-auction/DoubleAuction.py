from typing import List
from constants.OfferType import * 
from constants.ItemIds import *
from models.Offer import * 
from models.ListingOfOffers import * 


print('test')
print(OfferType.BUY == 0)
print(OfferType.BUY.value == 0)

listingOfOffers = ListingOfOffers()

# sell offers

mySellOffer1 = Offer()
mySellOffer1.setOfferDetails(OfferType.SELL, ItemIds.DAGGER, 999)

mySellOffer2 = Offer()
mySellOffer2.setOfferDetails(OfferType.SELL, ItemIds.DAGGER, 1001)

mySellOffer3 = Offer()
mySellOffer3.setOfferDetails(OfferType.SELL, ItemIds.DAGGER, 997)

mySellOffer4 = Offer()
mySellOffer4.setOfferDetails(OfferType.SELL, ItemIds.DAGGER, 10)

mySellOffer5 = Offer()
mySellOffer5.setOfferDetails(OfferType.SELL, ItemIds.SWORD, 1450)

mySellOffer6 = Offer()
mySellOffer6.setOfferDetails(OfferType.SELL, ItemIds.DAGGER, 997)

mySellOffer7 = Offer()
mySellOffer7.setOfferDetails(OfferType.SELL, ItemIds.DAGGER, 1000000)

# NOTE: About the System currently: buy offers will go to the price buyer asks for, and then look down from there to see available offers: this has
# the behaviour of the buyer being able to buy an overpriced item if they put in a very high offer, e.g.
# SELLERS: 1,000; 1,020; 1,040; 100,000
# if a buyer puts in an offer for 120,000, they will be offered the one for 100,000: do we want this behaviour?


# buy offers

myBuyOffer1 = Offer()
myBuyOffer1.setOfferDetails(OfferType.BUY, ItemIds.DAGGER, 1000)

myBuyOffer2 = Offer()
myBuyOffer2.setOfferDetails(OfferType.BUY, ItemIds.SWORD, 1500)

myBuyOffer3 = Offer()
myBuyOffer3.setOfferDetails(OfferType.BUY, ItemIds.DAGGER, 1000)

myBuyOffer4 = Offer()
myBuyOffer4.setOfferDetails(OfferType.BUY, ItemIds.DAGGER, 1000)

myBuyOffer5 = Offer()
myBuyOffer5.setOfferDetails(OfferType.BUY, ItemIds.DAGGER, 10000)

myBuyOffer6 = Offer()
myBuyOffer6.setOfferDetails(OfferType.BUY, ItemIds.DAGGER, 100000000)



print("\n\n\n test further")


listingOfOffers.addOffer(mySellOffer1)
listingOfOffers.addOffer(mySellOffer2)
listingOfOffers.addOffer(mySellOffer3)

listingOfOffers.addOffer(myBuyOffer1)
listingOfOffers.addOffer(myBuyOffer2)
listingOfOffers.addOffer(myBuyOffer3)
listingOfOffers.addOffer(myBuyOffer4)
listingOfOffers.addOffer(myBuyOffer5)

listingOfOffers.addOffer(mySellOffer4)
listingOfOffers.addOffer(mySellOffer6)
listingOfOffers.addOffer(mySellOffer5)
listingOfOffers.addOffer(mySellOffer7)
listingOfOffers.addOffer(myBuyOffer6)
