import random
import math

class walker:

    def __init__(self, data: list[tuple[str, float]]):
        if not data:
            raise ValueError("Error: List is empty.")
        
        total_prob = 0.0
        prev_event = ""
        for event, prob in data:
            if prev_event == event:
                raise ValueError("Error: You have recur events")
            if prob<0:
                raise ValueError(f"Error: Prob for {event} lower then 0: {prob}.")
            total_prob += prob


        if not math.isclose(total_prob, 1.0):
            raise ValueError(f"Error: Sum of probs must be 1.0 but you have {total_prob}")


        self.data = sorted(data, key=lambda x: x[1])
    
    def get_random(self):
        rand_num = random.random()
        cumulative_prob = 0.0
        
        for event, prob in self.data:
            cumulative_prob += prob
            if rand_num <= cumulative_prob:
                return event
    def __str__(self):
        return f"{self.data}"
    
#пример 1 нормальная работа
w = walker([("A",0.7),("B",0.2),("C",0.1)])
print(w.get_random())

#пример 2 когда сумма вероятностей не равна 1
try:
    w = walker([("A",0.1), ("B", 0.2)])
except ValueError as e:
    print(e)

#пример 3 когда когда ввели отрицательное число
try:
    w = walker([("A", -0.1), ("B", 0.1)])
except ValueError as e:
    print(e)

#пример 4 когда список пустой
try:
    w = walker([])
except ValueError as e:
    print(e)