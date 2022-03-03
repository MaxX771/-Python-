from application import salary
from db import people
from datetime import datetime



def main():


    if __name__ == '__main__':
        print('Start -> main()')
        print(salary.calculate_salary())
        print(people.get_employees())
        print(datetime.now())




main()
