import requests

API_POst_URL = 'https://pastebin.com/api/api_post.php'
DEVELOPER_API_KEY = 'gX6wt6B6efaif_YvjfP-5ZtUkw4txOp_'


def main():
    paste_url = post_new_paste(f"Madara's Speech", "Wake up to reality! Nothing ever goes as planned in this accursed world. The longer you live, the more you realize that the only things that truly exist in this reality are merely pain, suffering and futility. Listen, everywhere you look in this world, wherever there is light, there will always be shadows to be found as well. As long as there is a concept of victors, the vanquished will also exist. The selfish intent of wanting to preserve peace, initiates war and hatred is born in order to protect love. There are nexuses causal relationships that cannot be separated.")
    pass

def post_new_paste(title, body_text, expiration='1M', listed=True):
    params = {
        'api_dev_key': DEVELOPER_API_KEY,
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title,
        'api_paste_expire_date': expiration,
        'api_paste_private': 0 if listed else 1
    }


    print(f"Posting new paste to Pastebin...", end='')
    resp_msg = requests.post(API_POst_URL, data=params)

    if resp_msg.ok:
        print(f"successfully new paste has been completed.")
        print(f"URL of new paste: {resp_msg.text}")
        return resp_msg.text
    else:
        print(f"Failure!")
        print(f"Response code: {resp_msg.status_code} ({resp_msg.reason})")
        print(f"Error: {resp_msg.text}")

if __name__ == '__main__':
    main()
