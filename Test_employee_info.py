import employee_info as info

def test_get_employees_by_age_range():
    employees = info.get_employees_by_age_range(25, 35)
    assert len(employees) == 2

def test_calculate_average_salary():
    average_salary = info.calculate_average_salary()
    assert average_salary == 60166.666666666664

def test_get_employees_by_dept():
    employees = info.get_employees_by_dept('Sales')
    assert len(employees) == 2
    assert employees[0]['name'] == 'John'
    assert employees[1]['name'] == 'Peter'
