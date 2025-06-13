class Anime:
    def __init__(self, anime_name, lead_actor):
        self.anime = "Anime Name: " + anime_name
        self.actor = "Actor Name: " + lead_actor
    
    def animeXactor(self):
        return self.anime + " | " + self.actor


class AnimeLength(Anime):
    def __init__(self, anime_name, lead_actor, episodes):
        super().__init__(anime_name, lead_actor)
        self.eps = "Episodes: " + str(episodes)
    
    def animeXactorXeps(self):
        return self.anime + " | " + self.actor + " | " + self.eps

# anime_list = Anime("HxH", "Gon")
# print(anime_list.anime)
# print(anime_list.actor)

# print(anime_list.animeXactor())

anime_length = AnimeLength("Naruto", "Naruto Uzumaki", 720)
print(anime_length.anime)
print(anime_length.actor)
print(anime_length.eps)

print(anime_length.animeXactorXeps())