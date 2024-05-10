class Computation:

    def __init__(self):
        ...

    def factorial(self, num):
        s = 1
        for i in range(1, num + 1):
            s *= i
        return s

    def summ(self, num):
        s = 1
        for i in range(1, num + 1):
            s += i
        return s


    def is_prime(self, num):
        s = 0
        for i in range(1, num + 1):
            if num % i == 0:
                s += 1
        if s == 2:
            return True
        else:
            return False

    def all_is_prime(self, num):
        primes = []
        for i in range(2, num + 1):
            if self.is_prime:
                primes.append(i)
        return primes

    def table_mult(self, num):
        table = []
        for i in range(1, 11):
            table.append(num * i)
        return table

    def all_tables_mult(self):
        all_tables = {}
        for i in range(1, 11):
            all_tables[i] = self.table_mult(i)
        return all_tables


# Test cases
comp = Computation()
# print(comp.factorial(5))
# print(comp.summ(5))
print(comp.is_prime(12))
print(comp.all_is_prime(20))
# print(comp.table_mult(7))
# print(comp.all_tables_mult())