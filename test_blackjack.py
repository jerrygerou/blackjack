from blackjack import Card, Deck

def test_card_has_rank_and_value():
    card = Card(2, 'heart')
    assert card.rank == 2
    assert card.suit == 'heart'

def test_deck_has_fifty_two_cards():
    deck = Deck()
    assert len(deck) == 52

def test_deck_has_four_of_everything():
    ranks = [str(i) for i in range(2, 11)] + list('JQKA')
    rank_set = set(ranks)
    deck = Deck()
    hearts = [card for card in deck if card.suit == 'heart']
    spades = [card for card in deck if card.suit == 'spade']
    diamonds = [card for card in deck if card.suit == 'diamond']
    clubs = [card for card in deck if card.suit == 'club']
    assert all(
        set([c.rank for c in cards]) == rank_set
        for cards in [hearts, spades, diamonds, clubs])
