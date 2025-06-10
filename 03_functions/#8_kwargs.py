def kwargs_values(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

kwargs_values(name="Thor Odinson", age=1500, planet="Asgard", profession="God of Thunder")
kwargs_values(name="Tony Stark", age=50, planet="Earth", profession="Genius, billionaire, playboy, philanthropist")
kwargs_values(name="Steve Rogers", age=100, planet="Earth", profession="Super Soldier")
kwargs_values(name="Natasha Romanoff", age=35, planet="Earth", profession="Spy")
kwargs_values(name="Bruce Banner", age=50, planet="Earth", profession="Scientist")
kwargs_values(name="Clint Barton", age=40, planet="Earth", profession="Archer")