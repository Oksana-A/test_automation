import os
import time

from service.vk import VK
from utils.config_reader import ConfigReader
from utils.string_utils import StringUtils


class Test:
    vk = VK()
    data = {'access_token': ConfigReader.get_inst().token,
            'v': ConfigReader.get_inst().api_version
            }

    def test(self):
        message = StringUtils.get_random_txt(20)
        sent_data = self.data.copy()
        sent_data['message'] = message
        post_id = self.vk.make_post_on_wall_and_get_its_id(
            ConfigReader.get_inst().api_url, sent_data)
        user_and_post_id = ConfigReader.get_inst().user_id + '_' + str(post_id)
        sent_data = self.data.copy()
        sent_data['posts'] = user_and_post_id
        post_text = self.vk.get_post_data_list(
            ConfigReader.get_inst().api_url, sent_data).get('text')
        assert message == post_text

        upload_url = self.vk.get_wall_upload_url(
            ConfigReader.get_inst().api_url, self.data)
        path_to_picture = os.path.join(
            os.path.dirname(__file__), '..', 'resources', 'photo.jpg')
        res = self.vk.upload_data_to_server(
            upload_url, "photo", path_to_picture)
        sent_data = self.data.copy()
        sent_data['server'] = res['server']
        sent_data['hash'] = res['hash']
        sent_data['photo'] = res['photo']
        picture_id = self.vk.save_picture_on_server_and_get_its_id(
            ConfigReader.get_inst().api_url, sent_data)
        new_message = StringUtils.get_random_txt(50)
        picture = 'photo' + ConfigReader.get_inst().user_id + \
                  '_' + str(picture_id)
        sent_data = self.data.copy()
        sent_data['post_id'] = post_id
        sent_data['message'] = new_message
        sent_data['attachments'] = picture
        self.vk.edit_post_and_get_its_id(
            ConfigReader.get_inst().api_url, sent_data)
        sent_data = self.data.copy()
        sent_data['posts'] = user_and_post_id
        post_data = self.vk.get_post_data_list(
            ConfigReader.get_inst().api_url, sent_data)
        assert post_data.get('text') == new_message
        assert post_data.get('attachments')[0]['photo']['id'] == picture_id

        comment = StringUtils.get_random_txt(15)
        sent_data = self.data
        sent_data['post_id'] = post_id
        sent_data['message'] = comment
        comment_id = self.vk.make_comment_on_post_and_get_its_id(
            ConfigReader.get_inst().api_url, sent_data)
        sent_data = self.data
        sent_data['post_id'] = post_id
        comments_data_list = self.vk.get_post_comments_data(
            ConfigReader.get_inst().api_url, sent_data)['items']
        assert len(comments_data_list) == 1
        assert comments_data_list[0]['text'] == comment
        assert comments_data_list[0]['id'] == comment_id

        time.sleep(ConfigReader.get_inst().time_sleep)
        sent_data = self.data
        sent_data['type'] = 'post'
        sent_data['item_id'] = post_id
        self.vk.add_like(ConfigReader.get_inst().api_url, sent_data)
        assert self.vk.is_liked(
            ConfigReader.get_inst().api_url, sent_data) is True

        sent_data = self.data
        sent_data['item_id'] = post_id
        self.vk.delete(ConfigReader.get_inst().api_url, sent_data)
        list_of_posts = self.vk.get_posts_data(
            ConfigReader.get_inst().api_url, sent_data)['items']
        flag = False
        for post in list_of_posts:
            if post['id'] == post_id:
                flag = True
        assert flag is False
