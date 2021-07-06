from typing import List


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table = set()
        food = set()
        for order in orders:
            table.add(order[1])
            food.add(order[2])

        food = sorted(food, key=lambda x: x)
        table = sorted(table, key=lambda x: int(x))

        food_dict = {}
        for i, f in enumerate(food):
            food_dict[f] = i
        book, len_f = {}, len(food)
        for table_num in table:
            book[table_num] = [0] * len_f

        for order in orders:
            t_num, f = order[1:]
            book[t_num][food_dict[f]] += 1

        res = [['Table'] + food]
        for t_num, b_num in book.items():
            b_num = [str(x) for x in b_num]
            res.append([t_num] + b_num)

        return res


if __name__ == '__main__':
    solution = Solution()
    orders = [["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"],
              ["Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]
    orders = [["James", "12", "Fried Chicken"], ["Ratesh", "12", "Fried Chicken"], ["Amadeus", "12", "Fried Chicken"],
              ["Adam", "1", "Canadian Waffles"], ["Brianna", "1", "Canadian Waffles"]]
    orders = [["Laura", "2", "Bean Burrito"], ["Jhon", "2", "Beef Burrito"], ["Melissa", "2", "Soda"]]
    print(solution.displayTable(orders))
