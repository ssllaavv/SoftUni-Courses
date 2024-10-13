import datetime
from time import sleep


def measure_time_middleware(get_response):
    def middleware(request, *args, **kwargs):
        start_time = datetime.datetime.now()
        response = get_response(request, *args, **kwargs)
        # user = request.user
        # print(user)
        end_time = datetime.datetime.now()

        print(f'Executed in {end_time - start_time}')

        return response

    return middleware


def sleep_middleware(get_response):
    def middleware(request, *args, **kwargs):
        sleep(3)
        return get_response(request, *args, **kwargs)
    return middleware

