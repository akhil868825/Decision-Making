...
A fruit seller buys a dozen of banana at Rs.X. He sells 1 banana at Rs.Y. Write a program to determine the profit or loss in Rs. for the fruitseller.
Input format:
Input consists of 2 floating point numbers
The first input corresponds to the total cost(X)
The second input corresponds to the sold cost(Y)
Output format:
Print "Profit or Loss" with Rupees.
Sample Input:
60
4
Sample Output:
Loss : Rs.12.00
...
total_cost = float(input())
selling_price = float(input())

cost_per_banana = total_cost / 12
total_selling_price = selling_price * 12
profit_loss = total_selling_price - total_cost

if profit_loss > 0:
    print(f"Profit : Rs.{profit_loss:.2f}")
elif profit_loss < 0:
    print(f"Loss : Rs.{abs(profit_loss):.2f}")
else:
    print("No Profit No Loss")
