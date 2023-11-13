import json

from conftest import *
from settings.settings import *


@pytest.mark.positive
def test_get_disk_resources(get_disk_resources):
    try:
        response = get_disk_resources(f'{URL_GET_DISK_RESOURCES}?path={PATH}', headers=HEADERS)
        response_data = response.json()
        formatted_response = json.dumps(response_data, indent=4)
        print(formatted_response)
        assert response.status_code == 200, "Ошибка: статус-код не 200!"
    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")


@pytest.mark.positive
def test_get_disk_resources_files(get_disk_resources_files):
    try:
        response = get_disk_resources_files(f'{URL_GET_DISK_RESOURCES_FILES}?path={PATH}', headers=HEADERS)
        response_data = response.json()
        formatted_response = json.dumps(response_data, indent=4)
        print(formatted_response)
        assert response.status_code == 200, "Ошибка: статус-код не 200!"
    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")


@pytest.mark.positive
def test_get_disk(get_disk):
    try:
        response = get_disk(f'{URL_GET_DISK}?path={PATH}', headers=HEADERS)
        response_data = response.json()
        formatted_response = json.dumps(response_data, indent=4)
        print(formatted_response)
        assert response.status_code == 200, "Ошибка: статус-код не 200!"
    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")


