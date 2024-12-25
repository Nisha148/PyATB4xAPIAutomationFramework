# APIConstants- Class which contains all the end points
# keep the URLs

class APIConstants(object):
    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    def url_create_Booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def url_create_token(self):
        return "https://restful-booker.herokuapp.com/auth"

    def put_patch_delete_url(booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)