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

    def check_and_follow_pattern(self, number_list):
        """
        Check pattern to prioritize the even/odd ratio (3:2)
        Make even count or odd count to be exact 3.
        """
        count_even = 0
        count_odd = 0
        for num in number_list:
            if num % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
        if count_even == 3:
            return "even"
        elif count_odd == 3:
            return "odd"
        else:
            return ""

    def generate_main_number(self, number_count):
        while len(self.main_number_list) < number_count:
            # generate number until number_count threshold
            # Generate odd/even 3:2 pattern (Eg. 3 even + 2 odd or vice-versa)
            # prevent duplicate
            # sort Asc to Desc
            rand_number = random.randint(self.min_number, self.max_number)
            skip_even_or_odd = self.check_and_follow_pattern(self.main_number_list)

            if (skip_even_or_odd == "even" and rand_number%2 != 0) or (skip_even_or_odd == "odd" and rand_number%2 == 0) or (skip_even_or_odd == ""):
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

        if len(bonus_numbers) > 0:
            return """
            Main Numbers: [{}]
            <br/>
            Bonus Numbers: [{}]
            """.format(main_numbers, bonus_numbers)
        return """
            Main Numbers: [{}]
            """.format(main_numbers)            