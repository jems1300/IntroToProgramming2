from ToyFactory import ToyFactory
from ToyFactory import Package

toy1 = ToyFactory()
while True:
    print(toy1.count())
    print(toy1.make_package())
    if toy1.count_worker() <= 0:
        print("We are out of workers, please come back another date!")
        break

# toy1 = Package()
# toy1.access_content()
# toy1.access_label()
