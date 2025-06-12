import  random
#玩家类
class player():
    def __init__(self,name):
        self.name = name
        self.cards = []
    #添加牌
    def add_card(self,card):
        self.cards.append(card)
    def show_cards(self):
        cards_str = ' '.join(str(card) for card in self.cards)
        print(cards_str)
class card():
    def __init__(self,suit,number):
        self.suit = suit
        self.number = number
    def __str__(self):
        return self.suit + self.number
class deck():
    def __init__(self):
        self.cards = []
        self.build()
    def build(self):
        for i in ['梅花','方片','草花','黑桃']:
            for j in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
                self.cards.append(card(i,j))
    def shuffle(self):
        random.shuffle(self.cards)
    def  deal(self):
        if len(self.cards)>0:
            return self.cards.pop()
deck=deck()
player1=player('小王')
player2=player('小李')
deck.shuffle()

# 计算每个玩家应该获得的牌数
cards_per_player = len(deck.cards) // 2

# 发牌给玩家
for i in range(cards_per_player):
    player1.add_card(deck.deal())
    player2.add_card(deck.deal())

# 展示玩家手中的牌
print(f"\n{player1.name}的牌:")
player1.show_cards()
print(f"\n{player2.name}的牌:")
player2.show_cards()


