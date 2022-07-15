from gw2api import GuildWars2Client


class GW2Client:
    def gw2_client(self):
        return GuildWars2Client()

    def get_all_item_ids(self):
        return self.gw2_client().items.get()

    def get_items(self, ids):
        return self.gw2_client().items.get(ids=ids)


