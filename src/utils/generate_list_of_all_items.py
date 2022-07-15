import json
import os
from typing import List

from src.client.client import GW2Client
from src.utils.serializable_generator import SerializableGenerator

client = GW2Client()


def batch_ids_and_get_items(page_size: int, ids: List):
    page = 0
    entries_remaining = True
    ids_length = len(ids)
    while entries_remaining:
        start_idx = page_size * page
        entries_remaining = not (start_idx+page_size >= ids_length)
        end_idx = start_idx+page_size if entries_remaining else ids_length-1
        ids_batch = ids[start_idx:end_idx]
        page += 1
        yield client.get_items(ids_batch)
        print(f"{end_idx/ids_length*100}% complete")


def _write_all_items_to_archive():
    path = os.path.join('..', 'resources', 'item_archive.json')
    ids = client.get_all_item_ids()
    items = batch_ids_and_get_items(200, ids)
    with open(path, "w") as final:
        json.dump(SerializableGenerator(items), final)


if __name__ == '__main__':
    _write_all_items_to_archive()
