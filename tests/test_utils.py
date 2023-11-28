import pytest
from dundie.utils.email import check_valid_email
from dundie.utils.users import generate_simple_password



@pytest.mark.unit
@pytest.mark.parametrize("address", ["bruno@gmail.com", "bambineti@gmail.com"])
def test_positive_check_valid_email(address):
    assert check_valid_email(address) is True


@pytest.mark.unit
@pytest.mark.parametrize("address", ["bruno@gmail", "@gmail.com"])
def test_negativ_check_valid_email(address):
    assert check_valid_email(address) is False


@pytest.mark.unit
def test_generate_simple_password():
    passwords = []
    for _ in range(100):
        passwords.append(generate_simple_password(8))
    print(passwords)
    assert len(set(passwords)) == 100
