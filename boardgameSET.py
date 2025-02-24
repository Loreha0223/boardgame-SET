import random
person = ['다혜', '민지', '규환']
personScore = [0,0,0]
colors = ['빨강', '초록', '보라']
patterns = ['텅빈', '무늬', '꽉찬']
shape = ['타원', '물결', '사각']
count = [1, 2, 3]

cardlist = []
def createCard(n):
    for i in range(n):
        cardlist.append([random.choice(count), random.choice(colors), random.choice(patterns), random.choice(shape)])
       
def printCard(n):
    for i in range(n):
        print(cardlist[i], end=' ')
        if (i%3==2):
            print()

def calculateCard(choice, order):
    select = []
    for i in range(3):
        select.append(cardlist[choice[i]-1])
    print('당신이 고른 카드는 ' , *select, '입니다,')
    
    correct = 0
    for j in range(4):
        if (select[0][j]==select[1][j] and select[0][j]==select[2][j] and select[1][j]==select[2][j]):
            correct += 1
        elif (select[0][j]!=select[1][j] and select[0][j]!=select[2][j] and select[1][j]!=select[2][j]):
            correct += 1
    if (correct==4):
        print('맞았습니다.\n 3점을 획득합니다.')
        personScore[order%3] += 3
        if n==12:
            fixCard(choice)
        else:
            return deleteCard(choice)

    else:
        print('틀렸습니다.\n')

    return n

def addCard():
    for i in range(3):
        cardlist.append([random.choice(count), random.choice(colors), random.choice(patterns), random.choice(shape)])

def deleteCard(choice):
    choice.sort(reverse=True)
    for i in choice:
        cardlist.pop(i-1)
    return n-3

def fixCard(choice):
    for i in choice:
        cardlist[i-1] = [random.choice(count), random.choice(colors), random.choice(patterns), random.choice(shape)]
    

        
order = 0
n = 12 #세팅 카드 수
createCard(n)


while(order < 3):
    print(person[order%3] + '님의 차례입니다. 일치하는 카드가 없을시 0을 입력')
    printCard(n)
    
    chooseCard = list(map(int, input().split()))
        
    if  len(chooseCard) == 3 or len(set(chooseCard))==3 :
        n = calculateCard(chooseCard, order%3)
    elif chooseCard[0]==0:
        addCard()
        n+=3
    else:
        print('3장을 골라야 합니다,')
        continue
    
    order+=1

print('최종결과는 %s:%d점 %s:%d점, %s:%d점으로 %s의 승리입니다.'
      %(person[0],personScore[0],person[1],personScore[1],person[2],personScore[2],person[personScore.index(max(personScore))]))
