def how_to_survive(current_salary, current_spend, current_money, current_increase):
    month = 0
    s = 0  # предполагается, что зарплата приходит в конце месяца, поэтому начальное значение зарплаты - 0
    while current_money > 0 and (current_money + s) > current_spend:
        delta = s - current_spend  # разность между зарплатой и расходами
        new_delta = abs(delta)
        current_money = current_money - new_delta  # расчет остатка подушки
        current_spend *= 1+current_increase  # ежемесячный рост цен
        s += current_salary  # начисление зарплаты
        month += 1
    return month


money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = how_to_survive(salary, spend, money_capital, increase)
print(month)
