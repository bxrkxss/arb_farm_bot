from multiprocessing import Pool
import time
import requests


f = open('prv.txt', 'r')
i = 0
for line in f:
    i
    i += 1
with open("prv.txt", "r") as f:
    prv = f.read().split('\n')
    i = i - 1


def work(prv):
    while True:
        try:
            y = 0
            while y == 0:
                response = requests.get(f"https://swaprum.finance/server/claim-free?address={prv}")
                res = response.text
                res1 = ('{"error":"wait 1 hour"}')
                print(res)

                if res == res1:
                    print("Заснув на 5 хв")
                    time.sleep(300)
                if res != res1:
                    print("minted")
                    time.sleep(3700)
                    y = 1




        except Exception as ex:
            print(ex)
        finally:
            print("боркісс 1000-7")


if __name__ == '__main__':
    p = Pool(processes=1) # кол-во потоков
    p.map(work, prv)
