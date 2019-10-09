import requests


class VK:
    wall_post = "wall.post"
    get_post_by_id = "wall.getById"
    edit_post = "wall.edit"
    wall_upload_server = "photos.getWallUploadServer"
    save_wall_photo = "photos.saveWallPhoto"
    create_comment = "wall.createComment"
    get_comments = "wall.getComments"
    likes_add = "likes.add"
    likes_is_liked = "likes.isLiked"
    wall_delete = "wall.delete"
    wall_get = "wall.get"

    def make_post_on_wall_and_get_its_id(self, api_url, data):
        request_url = api_url + self.wall_post
        response = requests.post(request_url, data=data)
        return response.json()['response']['post_id']

    def get_post_data_list(self, api_url, data):
        request_url = api_url + self.get_post_by_id
        response = requests.post(request_url, data=data)
        return response.json()['response'][0]

    def edit_post_and_get_its_id(self, api_url, data):
        request_url = api_url + self.edit_post
        response = requests.post(request_url, data=data)
        return response.json()['response']['post_id']

    def get_posts_data(self, api_url, data):
        request_url = api_url + self.wall_get
        response = requests.post(request_url, data=data)
        return response.json()['response']

    def get_wall_upload_url(self, api_url, data):
        request_url = api_url + self.wall_upload_server
        response = requests.post(request_url, data=data)
        return response.json()['response']['upload_url']

    def upload_data_to_server(self, upload_url, file_type, path_to_file):
        response = requests.post(upload_url,
                                 files={file_type: open(path_to_file, "rb")})
        return response.json()

    def save_picture_on_server_and_get_its_id(self, api_url, data):
        request_url = api_url + self.save_wall_photo
        response = requests.post(request_url, data=data)
        return response.json()['response'][0]['id']

    def make_comment_on_post_and_get_its_id(self, api_url, data):
        request_url = api_url + self.create_comment
        response = requests.post(request_url, data)
        return response.json()['response']['comment_id']

    def get_post_comments_data(self, api_url, data):
        request_url = api_url + self.get_comments
        response = requests.post(request_url, data)
        return response.json()['response']

    def add_like(self, api_url, data):
        request_url = api_url + self.likes_add
        requests.post(request_url, data)

    def is_liked(self, api_url, data):
        request_url = api_url + self.likes_is_liked
        response = requests.post(request_url, data)
        if response.json()['response']['liked'] == 1:
            return True
        else:
            return False

    def delete(self, api_url, data):
        request_url = api_url + self.wall_delete
        requests.post(request_url, data)
