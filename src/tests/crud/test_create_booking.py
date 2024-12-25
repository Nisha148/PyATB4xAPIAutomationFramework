from http.client import responses
from logging import Logger

import allure
import pytest
from src.constants.api_constants import APIConstants
from src.utils.utils import Utils
from src.helpers.payload_manager import payload_create_booking
from src.helpers.api_requests_wrapper import post_request, get_request
from src.helpers.common_verification import *
import logging


class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify that create booking status and booking Id")
    @allure.description("Creating a booking from the payload")
    def test_create_booking_positive(self):
        Logger = logging.getLogger(__name__)
        Logger.info("Starting TC1")
        response = post_request(
            url=APIConstants().url_create_Booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload=payload_create_booking(),
            in_json=False,
        )
        verify_status_code(response_data=response,expected_data=200)
        verify_json_key_not_null(response.json()["bookingid"])
        Logger.info(response.json()["bookingid"])
        Logger.info("End of TC1")


    @pytest.mark.negative
    @allure.title("Verify that create booking status and booking Id")
    @allure.description("Creating a booking from the payload")
    def test_create_booking_negative(self):
        Logger = logging.getLogger(__name__)
        Logger.info("Starting TC1")
        response = post_request(
            url=APIConstants().url_create_Booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload={},
            in_json=False,
        )
        verify_status_code(response_data=response, expected_data=500)

