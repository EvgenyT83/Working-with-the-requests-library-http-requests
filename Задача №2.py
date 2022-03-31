import requests

class YaUploader:
    files_url: str = 'https://cloud-api.yandex.net/v1/disk/resources/files'
    upload_url: str = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    @property
    def header(self):
        return self.get_headers()

    def _get_upload_link(self, file_path: str) -> dict:
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(self.upload_url, params = params, headers = self.header)
        return response.json()

    def upload(self, file_path: str, file_name: str):
        href = self._get_upload_link(file_path).get('href')
        if not href:
            return

        responce = requests.put(href, data = open(file_name, 'rb'))
        if responce.status_code == 201:
            print("Upload completed successfully!")
            return True
        else:
            print("Something went wrong!")
            return

if __name__ == '__main__':
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload('Test-upload.txt', 'Test.txt')


