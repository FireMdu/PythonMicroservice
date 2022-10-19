import pytest

from src.common.models import StudentUser

skip_reason: str = "No implementation yet"


def get_valid_students():
    students = [
        StudentUser(
            first_name="Inoxi-Analyst",
            last_name="Analytics",
            role_level="Student",
            faculty="Engineering & Built Environment",
            school="Mechanical Engineering",
            programme="Mechanical Engineering",
            student_number="123456"
        ),
        StudentUser(
            first_name="Inoxi-Analyst",
            last_name="Analytics",
            role_level="Student",
            faculty="Engineering & Built Environment",
            school="Mechanical Engineering",
            programme="Mechanical Engineering",
            student_number="345678"
        )
    ]
    return students


def test_valid_student_user():
    """
        Test user validity
        :return:
    """

    valid_users = get_valid_students()
    user = StudentUser(
            first_name="Inoxi-Analyst",
            last_name="Analytics",
            role_level="Student",
            faculty="Engineering & Built Environment",
            school="Mechanical Engineering",
            programme="Mechanical Engineering",
            student_number="345678"
        )
    valid_user = user.is_valid_user(users=valid_users)
    assert valid_user


def test_invalid_student_user():
    """
    Test user validity
    :return:
    """

    valid_users = get_valid_students()
    user = StudentUser(
        first_name="Inoxi-Analyst",
        last_name="Analytics",
        role_level="Student",
        faculty="Engineering & Built Environment",
        school="Mechanical Engineering",
        programme="Mechanical Engineering",
        student_number="3456789"
    )
    valid_user = user.is_valid_user(users=valid_users)
    assert not valid_user


@pytest.mark.skip(reason=skip_reason)
def test_user_in_bad_status_can_not_loan_documents():
    """
    Only users in good standing with the library should be able to loan documents
    :return:
    """
    ...


@pytest.mark.skip(reason=skip_reason)
def test_user_checkout_must_have_one_or_more_documents():
    """
    A valid checkout card should have at least one LoanLine object
    :return:
    """
    ...


@pytest.mark.skip(reason=skip_reason)
def test_each_checkout_line_must_be_a_valid_loan_line():
    """
    Each document checked out should be represented by a LoanLine object.
    :return:
    """
    ...
