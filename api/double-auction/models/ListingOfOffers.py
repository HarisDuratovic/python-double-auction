from .Offer import *
from constants.OfferType import *
from constants.ItemIds import *

class ListingOfOffers:
    
    buy_offers = dict()
    sell_offers = dict()
    completed_buy_offers = dict()
    completed_sell_offers = dict()
    completed_transactions = []
    
    def __init__(self) -> None:
        """Initialise all dictionaries for offer lists
        """
        
        # avoid same reference issue by initialising each one with its own list
        # TODO: how to we deep clone?
        
        all_ids1 = []
        all_ids2 = []
        all_ids3 = []
        all_ids4 = []
        
        for id in ItemIds:
            all_ids1.append((id, dict()))
            all_ids2.append((id, dict()))
            all_ids3.append((id, dict()))
            all_ids4.append((id, dict()))
        
        self.buy_offers            = dict(all_ids1)
        self.completed_buy_offers  = dict(all_ids2)
        self.sell_offers           = dict(all_ids3)
        self.completed_sell_offers = dict(all_ids4)
        
    
    def addOffer(self, offer: Offer):
        """[summary]

        Args:
            offer (Offer): Offer to add
        """
        #TODO: check if the offer will complete any offer, otherwise, add it to the listing
        
        if (offer.offer_type == OfferType.BUY):
            self.handleAnyOffer(offer, self.buy_offers, self.completed_buy_offers, self.sell_offers, self.completed_sell_offers, True)
        elif (offer.offer_type == OfferType.SELL):
            self.handleAnyOffer(offer, self.sell_offers, self.completed_sell_offers, self.buy_offers, self.completed_buy_offers, False)
            
        print('buy_offers', self.buy_offers)
        print('completed_buy_offers', self.completed_buy_offers)
        print('sell_offers', self.sell_offers)
        print('completed_sell_offers', self.completed_sell_offers)
        print()
        
        # if (offer.offer_type == OfferType.BUY):
        #     self.handleBuyOffer(offer)
        # elif (offer.offer_type == OfferType.SELL):
        #     self.handleSellOffer(offer)
        
        
        
    # TODO: maybe we can be smart and just use one for optimisation 
    #
            # self.handleBuyOffer(offer, self.sell_offers, self.buy_offers)
    def handleAnyOffer(self, offer: Offer, offer_dict_1, completed_offer_dict_1, offer_dict_2, completed_offer_dict_2, reverse):
        
        offer_keys = list(offer_dict_2[offer.item_id].keys())
        offer_keys.sort(reverse=reverse)
        
        found_offer_price = None
        
        for offer_prices in offer_keys:
            if offer_prices > offer.item_price:
                continue
            else:
                found_offer_price = offer_prices
                break
            
        
        if (found_offer_price != None):
            
            # remove the offer and add it to completed offers
            found_offer: Offer = offer_dict_2[offer.item_id][found_offer_price].pop()
            
            # if key list is empty, we delete it
            if (len(offer_dict_2[offer.item_id][found_offer_price]) == 0):
                offer_dict_2[offer.item_id].pop(found_offer_price)
            
            
            
            
            if found_offer.item_price in completed_offer_dict_2[found_offer.item_id]:
                completed_offer_dict_2[found_offer.item_id][found_offer.item_price] += [found_offer]
            else:
                completed_offer_dict_2[found_offer.item_id][found_offer.item_price] = [found_offer]
                  

            if offer.item_price in completed_offer_dict_1[offer.item_id]:
                completed_offer_dict_1[offer.item_id][offer.item_price] += [offer]
            else:
                completed_offer_dict_1[offer.item_id][offer.item_price] = [offer]

        else:
            # if can't complete an offer, then we put it into the dictionary to wait for an applicable offer
            
            if offer.item_price in offer_dict_1[offer.item_id]:
                offer_dict_1[offer.item_id][offer.item_price] += [offer]
            else:
                offer_dict_1[offer.item_id][offer.item_price] = [offer]

            
        
        
        
        
    # def handleBuyOffer(self, offer: Offer):
        
    #     sell_offer_keys = list(self.sell_offers[offer.item_id].keys())
    #     sell_offer_keys.sort(reverse=True)
        
    #     found_sell_offer_price = None
        
    #     for sell_offer in sell_offer_keys:
    #         if sell_offer > offer.item_price:
    #             continue
    #         else:
    #             found_sell_offer_price = sell_offer
    #             break
            
        
    #     if (found_sell_offer_price != None):
            
    #         # remove the sell offer and add it to completed sell offers, and the buy offer gets added to completed offers as well
    #         found_sell_offer: Offer = self.sell_offers[offer.item_id][found_sell_offer_price].pop()
            
    #         # if key list is empty, we delete it
    #         if (len(self.sell_offers[offer.item_id][found_sell_offer_price]) == 0):
    #             self.sell_offers[offer.item_id].pop(found_sell_offer_price)
            
            
    #         if found_sell_offer.item_price in self.completed_sell_offers[found_sell_offer.item_id]:
    #             self.completed_sell_offers[found_sell_offer.item_id][found_sell_offer.item_price] += [found_sell_offer]
    #         else:
    #             self.completed_sell_offers[found_sell_offer.item_id][found_sell_offer.item_price] = [found_sell_offer]
                  

    #         if offer.item_price in self.completed_buy_offers[offer.item_id]:
    #             self.completed_buy_offers[offer.item_id][offer.item_price] += [offer]
    #         else:
    #             self.completed_buy_offers[offer.item_id][offer.item_price] = [offer]

    #     else:
    #         # print(self.buy_offers)
            
    #         if offer.item_price in self.buy_offers[offer.item_id]:
    #             self.buy_offers[offer.item_id][offer.item_price] += [offer]
    #         else:
    #             self.buy_offers[offer.item_id][offer.item_price] = [offer]

            
        
         
        
    # def handleSellOffer(self, offer: Offer):
        
    #     # TODO: check if completes any buy offers
        
        
    #     print(self.sell_offers)
        
    #     if offer.item_price in self.sell_offers[offer.item_id]:
    #         self.sell_offers[offer.item_id][offer.item_price] += [offer]
    #     else:
    #         self.sell_offers[offer.item_id][offer.item_price] = [offer]

        
    #     print(self.sell_offers)
        
        