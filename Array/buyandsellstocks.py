def maxprofit(prices):
    mini = prices[0]
    maxprofit = 0
    for i in range(len(prices)):
        cost = prices[i] - mini
        maxprofit = max(cost, maxprofit)
        mini = min(prices[i], mini)
    return maxprofit
prices = [7,1,5,3,6,4]
l=maxprofit(prices)
print(l)



#another approach
# def maxprofit(prices):
#     min_price = float('inf')
#     max_profit = 0
#     k = len(prices)
#     for i in range(k):
#         if prices[i] < min_price:
#             min_price = prices[i]
#         elif prices[i] - min_price > max_profit:
#             max_profit = prices[i] - min_price
#     return max_profit
# prices = [7,1,5,3,6,4]
# l=maxprofit(prices)
# print(l)
