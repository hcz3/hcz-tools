class FizzBuzz(object):
    def __init__(self, number):
        if FizzBuzz.is_valid_number(number):
            self.number = number

    @property
    def result(self):
        if self.is_number_divisible_by(3) and self.is_number_divisible_by(5):
            return "FizzBuzz"
        elif self.is_number_divisible_by(3):
            return "Fizz"
        elif self.is_number_divisible_by(5):
            return "Buzz"
        return self.number

    def is_number_divisible_by(self, divisor):
        return self.number % divisor == 0
   
    @staticmethod
    def is_valid_number(number):
        if number <= 0 or number > 100: 
            raise ValueError('Number must be between 0 and 101.')
        return True

def main():
    n = 100
    for i in range(1, n+1):
        print(FizzBuzz(i).result)

if __name__ == "__main__":
    main()
     