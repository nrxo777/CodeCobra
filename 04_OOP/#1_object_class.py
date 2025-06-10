class Anime:
    def __init__(self, anime_name, lead_actor):
        self.anime = "Anime Name: " + anime_name
        self.actor = "Actor Name: " + lead_actor
    
    def animeXactor(self):
        return self.anime + " | " + self.actor

anime_list = Anime("HxH", "Gon")
print(anime_list.anime)
print(anime_list.actor)

print(anime_list.animeXactor())