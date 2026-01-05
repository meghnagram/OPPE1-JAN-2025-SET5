card_values = {
    rank:val 
    for val, rank in enumerate(list("23456789")+["10"]+list("JQKA"))
} # {'2':0, '3':1, ..., '10':8, 'J':9, 'Q':10, 'K':11, 'A':12}



def find_min_card(cards: list, suit: str) -> str:
    """
    Find the minimum card of a specific suit in a given list of cards.

    Args:
        cards (list): A list of string representations of playing cards.
        suit (str): The suit for which to find the minimum card.

    Returns:
        str: The minimum card of the specified suit based on standard card ranking. Returns None if the suit has no cards in the list or the list is empty.
        
    Example:
        >>> find_min_card(['H2', 'S9', 'DA', 'C5', 'C10'], 'C')
        'C5'
    """
    
        
    
    # Scratch algorithm
    min_card, min_val = None, 13
    for card in cards:
        if card[0] == suit and card_values[card[1:]]<min_val:
            min_card = card
            min_val = card_values[card[1:]]
    return min_card

    # Functional approach
    # suit_cards = [card for card in cards if card[0] == suit]
    # if suit_cards:
    #   min_card = min(suit_cards, key=lambda x: card_values[x[1:]])
    #   return min_card

# #another Method:

# card_values = {
#     rank:val 
#     for val, rank in enumerate(list("23456789")+["10"]+list("JQKA"))
# } # {'2':0, '3':1, ..., '10':8, 'J':9, 'Q':10, 'K':11, 'A':12}



# def find_min_card(cards: list, suit: str) -> str:
#     d=[]
#     for i in cards:
#         if suit in i:
#             d.append(i[1::])
    
#     min=100
#     if len(d)==0:
#         return(None)
#     for i in d:
#         if i in card_values.keys():
#             if min>card_values[i]:
#                 min=card_values[i]
#                 val=i
    
            
#     return(suit+val)


# Find Minimum Card of a Specific Suit in Hand
# Write a function find_min_card that takes a list of string representations of playing cards and a string representing a suit, and returns the minimum card of that suit based on the standard card ranking. If there are no cards of that suit, return None. If the input list is empty, return None.

# The cards are represented in the following format:

# The first character represents the suit:
# 'S' for Spades
# 'H' for Hearts
# 'C' for Clubs
# 'D' for Diamonds
# The second character(s) represent the rank:
# '2' through '10' for numbered cards
# 'J' for Jack
# 'Q' for Queen
# 'K' for King
# 'A' for Ace
# The ranking of cards from lowest to highest in a standard deck of cards is:

# 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
# Example

# >>> find_min_card(['H2', 'S9', 'DA', 'C5', 'CA'], 'S')
# 'S9'
# >>> find_min_card(['H2', 'DA', 'C5', 'CA'], 'H')
# 'H2'
# >>> find_min_card(['DA', 'C5', 'CA'], 'C')
# 'C5'
# >>> find_min_card(['H10', 'D4'], 'S')
# None
# Explanation: The lowest card in the hand from the specified suit is returned.
    
