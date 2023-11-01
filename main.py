class Problem:
    def _0062(n: int) -> int: # Failed for now
        if n > 0:return n * 2
        return 1

    def _0564(n: str) -> int: # waiting ...

        return

    def _0061(n: int) -> int:
        return n * ((n *2) - 1)

    def _0366(n: int) -> int: # complete
        if n < 3:
            return 0
        return (n - 2) * 180


    def _0014(s: list) -> int: # robocontest server error
        n, k = s[0], s[1]
        response = (k + 1) ** n

        return int(response % (10e9 + 7))
    
    def _0604(s: str) -> int: # ord
        return ord(s)

    def _0012(n: int) -> str:
        from func import is_Primary
        a = 0
        for i in range(1, n+ 1):
            if is_Primary(i):
                a += 1
        if a % 2 == 0:
            return 'Ali'
        else:
            return 'Bobur'

    def _0066(n: list) -> int: # yeb to`ymas ochofat
        a = 2 ** (2 ** n[0])
        return a % n[1]
    
    def _1049(n: str):
        
        

        
class main:

    def run(cls):
        response = Problem._0066([3, 15])


        print(response)
if __name__ == '__main__':
    from time import time
    start = time()
        
    main().run()

    end = time()
    print(f'program finished in {str((end - start) * 60)[:3]} seconds')