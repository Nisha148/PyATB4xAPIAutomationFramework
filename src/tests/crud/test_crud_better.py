import allure
import pytest

from src.conftest import create_token, get_booking_id
from src.constants.api_constants import APIConstants
from src.utils.utils import Utils
from src.helpers.payload_manager import *
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *

class TestCRUDBooking(object):
    @allure.title("Test CRUD Operation Update PUT")
    @allure.description("Verify the Full update with the Valid BookingId and Token")
    def test_update_booking_id_token(self,get_booking_id,create_token):
        token=create_token()
        print(token)
        put_url=APIConstants.put_patch_delete_url(booking_id=get_booking_id)
        response = put_request(
            url=put_url,
            auth=None,
            headers=Utils().common_headers_put_patch_delete(token=create_token),
            payload=payload_create_booking(),
            in_json=False,
        )
        # Verification here and more
        verify_response_key(response.json()["firstname"],"Amit")
        verify_response_key(response.json()["lastname"],"Brown")
        verify_status_code(response_data=response,expected_data=200)


    def test_delete_booking_id(self,create_token,get_booking_id):
        delete_url = APIConstants().put_patch_delete_url(booking_id=get_booking_id)
        response = delete_request(
            url=delete_url,
            auth=None,
            headers=Utils().common_headers_put_patch_delete(token=create_token),
            in_json=False,
            payload={},
        )
        verify_response_delete(response=response.text)
        print(response.text)
        verify_status_code(response_data=response,expected_data=201)
