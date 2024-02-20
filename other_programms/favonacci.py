class Favonacci:
    def set_length(self, num):
        self.num = num

    def print_favonacci(self):
        ft = 0
        st = 1
        for i in range(self.num):
            print(ft)
            nt = ft + st
            ft = st
            st = nt

obj = Favonacci()
obj.set_length(11)
obj.print_favonacci()

         