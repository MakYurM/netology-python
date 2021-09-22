import requests
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        resp_file_put = requests.put(file_path, headers=headers,
                                     files={'file': open('ydisk_netology_python.txt', 'rb')})
        return resp_file_put

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    token = ''
    API_BASE_URL = 'https://cloud-api.yandex.net/'
    headers = {
        'Accept': 'application/json',
        'Authorization': f'OAuth {token}'}
    resp_files_url = requests.get(API_BASE_URL + 'v1/disk/resources/upload',
                                  params={'path': 'Netology/ydisk_netology_python.txt'}, headers=headers)
    path_to_file = resp_files_url.json()['href']
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
if result.status_code == 201:
    print('Файл загружен!')