#
from input2 import _INPUT

def main(*, int=int, input=input):
    def judge(cards):
        card_count = {}

        for card in cards:
            card_count[card] = card_count.get(card, 0) + 1

        count = list(card_count.values())
        count.sort(reverse=True)

        if count[0] == 4:
            return "Four Card"
        elif count[0] == 3:
            return "Three Card"
        elif count[0] == 2 and count[1] == 2:
            return "Two Pair"
        elif count[0] == 2:
            return "One Pair"
        else:
            return "No Pair"

    N = int(input().strip())
    cards_list = [input().strip() for _ in range(N)]

    for cards in cards_list:
        result = judge(cards)
        print(result)

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
