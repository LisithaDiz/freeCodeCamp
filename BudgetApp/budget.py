class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        l = ''
        for i in self.ledger:
            if i == self.ledger[-1]:
                l += f"{i['description'][0:23]:23}" + '{:>7.2f}'.format(i["amount"])
            else:
                l += f"{i['description'][0:23]:23}" + '{:>7.2f}'.format(i["amount"]) + '\n'

        l = '{:*^30}'.format(self.category) + '\n' + l + '\n' + 'Total: ' + '{:.2f}'.format(self.get_balance())
        return l

    def deposit(self, amount, description_d=''):
        self.ledger.append({"amount": amount, "description": description_d})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        x = 0
        for i in self.ledger:
            x = x + i['amount']
        return x

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.category}")
            category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True


def create_spend_chart(categories):
    title = 'Percentage spent by category\n'
    spend = []
    percentages = []
    bar = []
    line = []
    chart = ''
    for i in categories:
        t = 0
        for j in i.ledger:
            if j['amount'] < 0:
                t += abs(j['amount'])
        spend.append(t)

    r = 0
    for _ in spend:
        percentages.append(spend[r] / sum(spend) * 100)
        r += 1

    for e in percentages:
        dic = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', " "]
        for _ in range(int(e / 10) + 1):
            dic[(dic.index(' '))] = 'o'
        bar.append(dic)

    n = 0
    while n <= 10:
        u = ''
        for i in bar:
            u = u + i[n] + "  "
        line.append('{:>3}'.format(n * 10) + '|' + ' ' + u)
        n += 1
    line = list(reversed(line))
    for i in line:
        if i == line[-1]:
            chart = chart + i
        else:
            chart = chart + i + '\n'

    name_chart = []
    len_of_categories = []
    for i in categories:
        len_of_categories.append(len(i.category))
    get_max = max(len_of_categories)
    o = 0
    cat_edit = []
    for i in categories:
        i.category = i.category + ' ' * (get_max - len_of_categories[o])
        cat_edit.append(i.category)
        o += 1
    print(cat_edit)

    d = 0
    while d < get_max:
        u = ''
        for i in cat_edit:
            u = u + i[d] + '  '
        name_chart.append('     ' + u)
        d += 1
    print(name_chart)
    done = ''
    for i in name_chart:
        if i == name_chart[-1]:
            done = done + i
        else:
            done = done + i + '\n'

    return title + chart + "\n    ----------\n" + done
