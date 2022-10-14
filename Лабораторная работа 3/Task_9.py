salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
need_money = 0  # количество денег, чтобы прожить 10 месяцев


def how_to_survive(current_salary, current_spend, current_increase):
    need_money = 0
    for i in range(1, months + 1):  # увеличиваем правый интервал на 1, так как он не включается
        cap = current_spend - current_salary  # превышение расходов над зарплатой
        current_spend *= 1 + current_increase  # увеличение цен ежемесячно
        need_money += cap  # расчет необходим средств каждый месяц
    return need_money


need_money = how_to_survive(salary, spend, increase)
print(round(need_money))
