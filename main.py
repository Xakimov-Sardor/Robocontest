class Problem:
    def _0062(n: int) -> int: # Failed for now
        if n > 0:return n * 2
        return 1

    def _0564(n: str) -> int:

        return

    def _0061(n: int) -> int:
        return n * ((n *2) - 1)

    def _0366(n: int) -> int: # complete
        if n < 3:
            return 0
        return (n - 2) * 180
class main:
    def run(self):

        response = Problem._0366(1)
        print(response)

if __name__ == '__main__':
    from time import time
    start = time()
        
    main().run()

    end = time()
    print(f'program finished in {str((end - start) * 60)[:3]} seconds')