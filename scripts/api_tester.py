import pprint
import requests

url = 'http://127.0.0.1:8001'

def make_request(endpoint_url: str, method: str, payload: dict = None) -> None:
    request_url = f'{url}/{endpoint_url}'

    methods = {
        'GET': requests.get,
        'POST': requests.post,
        'PUT': requests.put,
        'PATCH': requests.patch,
        'DELETE': requests.delete
    }

    response = methods[method](request_url, payload)

    print('response.data:')
    pprint.pprint(response.json())
    pprint.pprint(f'response.status_code: {response.status_code}')


if __name__ == '__main__':
    # test GET
    make_request('task-users', 'GET')