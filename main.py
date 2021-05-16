from Бухгалтерия.application.salary import calculate_salary
from Бухгалтерия.application.people import get_employees
from datetime import datetime

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(datetime.now())