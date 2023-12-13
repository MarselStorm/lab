def months(money_capital, salary, spend, increase):
    months = 0

    while money_capital >= spend:
        monthly_budget = salary + money_capital
        spend *= (1 + increase / 100)

        if money_capital < spend:
            break
        money_capital -= spend
        months += 1

    return months
