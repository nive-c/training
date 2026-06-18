from employee import add_employee, list_employees

def test_add_employee():
    add_employee("Nive", "Developer")
    assert len(list_employees()) > 0