import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/'


def main():
    poke_url = get_poke_info(id)
    pass

def get_poke_info(id, limit=20, page=5 ):
    params = {
        'id': int(id),
        'page': page,
        'limit': limit
    }
    print(f"Posting new paste to Pastebin...", end='')
    resp_msg = requests.get(POKE_API_URL, headers=params)
    
    if resp_msg.ok:
        print(f"successfully information of pokemon is collected.")
        print(f"URL: {resp_msg.text}")
        return resp_msg.text
    else:
        print(f"Failure!")
        print(f"Response code: {resp_msg.status_code} ({resp_msg.reason})")
        print(f"Error: {resp_msg.text}")

if __name__ == '__main__':
    main()
