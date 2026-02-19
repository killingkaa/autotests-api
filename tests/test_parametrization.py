import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize("number", [1,2,3, -1])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize("number, expected", [(1,1), (2,4), (3,9)])
def test_several_numbers(number, expected):
    assert number ** 2 == expected


@pytest.mark.parametrize("os", ["macos", "Windows", "Linux", "Debian"])
@pytest.mark.parametrize("host", [
    "https://dev.company.com",
    "https://stable.company.com",
    "https://prod.company.com"
])
def test_multiplication_of_numbers(os, host):
    assert len(os + host) > 0


@pytest.fixture(params=[
    "https://dev.company.com",
    "https://stable.company.com",
    "https://prod.company.com"
])
def host(request: SubRequest) -> str:
    return request.param


def test_host(host: str):
    print(f"Running test on host: {host}")


@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperatiobs:
    def test_user_with_operations(self, user: str):
        print("User with operations: ")

    def test_user_without_operations(self, user: str):
        print("User without operations: ")


users = {
    "+71011100044": "User with money on bamk account",
    "+7000000022": "User without money on bank account",
    "+7000000003": "User with operations on bank account"
}
@pytest.mark.parametrize(
    "phone_number",
    users.keys(),
    ids= lambda phone_number: f"{phone_number} -{users[phone_number]}"
)


def test_identifiers(phone_number: str):
    pass