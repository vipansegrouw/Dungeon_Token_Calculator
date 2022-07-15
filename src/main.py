from src.client.client import GW2Client


def main():
    client = GW2Client()
    ids = client.get_all_item_ids()
    items = client.get_items(200, ids)


if __name__ == '__main__':
    main()