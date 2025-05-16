from sys import exit
def main():
    # read n and q
    line_1 = input().split(" ")
    try:
        n, q = int(line_1[0]), int(line_1[1])
    
    except ValueError:
        exit("Invalid input")

    caps = [int(cap) for cap in input().split(" ")]
    
    institutes = n*[institute]
    
    for i, cap in enumerate(caps):
        institutes[i] = institute(cap)
    
    # read requests
    extra = 0
    
    for i in range(q):
        request = [int(num) for num in input().split(" ")]

        t = request[0]

        if t == 1:
            target_inst, donation = request[1] - 1, request[2]
            while donation != 0:
                if target_inst == n:
                    extra += donation
                    break
                donation = institutes[target_inst].donate(donation)
                target_inst += 1
        
        if t == 2:
            target_inst = request[1] - 1
            print(institutes[target_inst].get_balance())


class institute:
    def __init__(self, cap: int):
        self.cap = cap
        self.balance = 0

    def donate(self, donation: int):
        self.balance += donation
        return self.balance % self.cap
    
    def get_balance(self):
        return self.balance

if __name__ == "__main__":
    main()