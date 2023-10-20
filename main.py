class Problem:
    def _0062(n: int) -> int: # Failed for now
        if n > 0:return n * 2
        return 1

    def _0564(n: str) -> int:

        return
class main:
    def run(self):

        response = Problem._0062(0)
        print(response)

if __name__ == '__main__':
    from time import time
    start = time()
        
    main().run()

    end = time()
    print(f'program finished in {str((end - start) * 60)[:3]} seconds')