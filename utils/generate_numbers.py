import random

class JackpotGenerator:
    def __init__(self, min_number=1, max_number=50, min_bonus_number=1, max_bonus_number=10):
        """
        Main numbers min, max
        Bonus number min and max
        """
        self.min_number = min_number
        self.max_number = max_number
        self.min_bonus_number = min_bonus_number
        self.max_bonus_number = max_bonus_number
        
        self.main_number_list = []
        self.bonus_number_list = []

    def generate_main_number(self, number_count):
        while len(self.main_number_list) < number_count:
            # generate number until number_count threshold
            # prevent duplicate
            # sort Asc to Desc
            rand_number = random.randint(self.min_number, self.max_number)
            new_list = set(self.main_number_list+[rand_number])
            self.main_number_list = list(new_list)
        self.main_number_list.sort()

    def generate_bonus_number(self, number_count):
        while len(self.bonus_number_list) < number_count:
            # generate number until number_count threshold
            # prevent duplicate
            # sort Asc to Desc
            rand_number = random.randint(self.min_bonus_number, self.max_bonus_number)
            new_list = set(self.bonus_number_list+[rand_number])
            self.bonus_number_list = list(new_list)
        self.bonus_number_list.sort()
    
    def generate_numbers(self, main_number_count, bonus_number_count):
        # generate all numbers
        self.generate_main_number(main_number_count)
        self.generate_bonus_number(bonus_number_count)

    def __str__(self):
        main_numbers = ", ".join(str(num) for num in self.main_number_list)
        bonus_numbers = ", ".join(str(num) for num in self.bonus_number_list)
        return """
        Main Numbers: [{}],
        <br/>
        Bonus Numbers: [{}]
        """.format(main_numbers, bonus_numbers)