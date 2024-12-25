import allure
import pytest
from src.constants.api_constants import APIConstants
from src.utils.utils import Utils
from src.helpers.payload_manager import *
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *

@pytest.fixture(scope="session")
def create_token():
    response=post_request(
        url=APIConstants().url_create_token(),
        auth=None,
        headers=Utils().common_headers_json(),
        payload=create_payload_token(),
        in_json=False,
    )
    verify_status_code(response_data=response,expected_data=200)
    verify_json_key_for_not_null_token(response.json()["token"])
    return response.json()["token"]

@pytest.fixture(scope="session")
def get_booking_id():
    response=post_request(
        url=APIConstants().url_create_Booking(),
        auth=None,
        headers=Utils().common_headers_json(),
        payload=payload_create_booking(),
        in_json=False,
    )
    booking_id=response.json()["bookingid"]
    verify_status_code(response_data=response,expected_data=200)
    verify_json_key_not_null(booking_id)
    return booking_id