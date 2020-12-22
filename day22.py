# day 22
# today's theme: RTFM, and, carefully!!!


def crab_combat(input_str):
    players = [part for part in input_str.split('\n\n') if part]
    cards_p1 = [
        int(line.strip())
        for line in players[0].split('\n')[1:] if line
    ]
    cards_p2 = [
        int(line.strip())
        for line in players[1].split('\n')[1:] if line
    ]
    while cards_p1 and cards_p2:
        card1 = cards_p1.pop(0)
        card2 = cards_p2.pop(0)
        if card1 > card2:
            cards_p1 += [card1, card2]
        if card1 < card2:
            cards_p2 += [card2, card1]
    if cards_p1:
        winner = cards_p1
    else:
        winner = cards_p2

    return sum([(len(winner) - idx) * card for idx, card in enumerate(winner)])


def crab_combat_subgame(cards_p1, cards_p2):
    previous_decks = set()
    while cards_p1 and cards_p2:
        current_deck = ''.join([
            str(item)
            for item in cards_p1 + [' '] + cards_p2
        ])
        if current_deck in previous_decks:
            return 1, cards_p1

        previous_decks.add(current_deck)
        card1 = cards_p1.pop(0)
        card2 = cards_p2.pop(0)
        if card1 <= len(cards_p1) and card2 <= len(cards_p2):
            subgame_winner, _ = crab_combat_subgame(
                cards_p1[:card1],
                cards_p2[:card2],
            )
            if subgame_winner == 1:
                cards_p1 += [card1, card2]
            if subgame_winner == 2:
                cards_p2 += [card2, card1]
        else:
            if card1 > card2:
                cards_p1 += [card1, card2]
            if card1 < card2:
                cards_p2 += [card2, card1]
    if cards_p1:
        return 1, cards_p1
    return 2, cards_p2


def recursive_crab_combat(input_str):
    # why you have to torture the little crab like this?!
    players = [part for part in input_str.split('\n\n') if part]
    cards_p1 = [
        int(line.strip())
        for line in players[0].split('\n')[1:] if line
    ]
    cards_p2 = [
        int(line.strip())
        for line in players[1].split('\n')[1:] if line
    ]
    _, winner_deck = crab_combat_subgame(cards_p1, cards_p2)
    return sum([
        (len(winner_deck)-idx)*card
        for idx, card in enumerate(winner_deck)
    ])


def main():
    with open('./input_folder/day22.txt', encoding='UTF-8') as fh:
        input_text = fh.read()
    # part1
    assert crab_combat(input_text) == 33010
    # part2
    assert recursive_crab_combat(input_text) == 32769
    print('success!!')


if __name__ == '__main__':
    main()
