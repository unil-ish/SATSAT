# code pour la classe Character
import pandas as pd


class Character:
    # attributs de classe
    all_character_objects = []
    all_characters_id = []  # une liste de tous les id de character
    all_names_id = []
    all_movies_id = []
    all_genders_id = []
    all_credits_positions_id = []

    def __init__(self, character_id, name_id, movie_id, gender_id, credits_position_id):
        self.character_id = character_id  # id d'un character en particulier
        self.name_id = name_id
        self.movie_id = movie_id
        self.gender_id = gender_id
        self.credits_position_id = credits_position_id

    # donner un name_id associé à un character_id
    def get_name_id(self, character_id):
        # mettre deux listes ensemble et mettre cette liste dans un dictionnaire
        merged_list = dict(zip(self.all_characters_id, self.all_names_id))
        # cherche l'id character donné et retourne l'id name associé
        return merged_list[character_id]

    def get_movie_id(self, character_id):
        merged_list = dict(zip(self.all_characters_id, self.all_movies_id))
        return merged_list[character_id]

    def get_gender_id(self, character_id):
        merged_list = dict(zip(self.all_characters_id, self.all_genders_id))
        return merged_list[character_id]

    def get_credits_position_id(self, character_id):
        merged_list = dict(zip(self.all_characters_id, self.all_credits_positions_id))
        return merged_list[character_id]

    # création de @property pour pouvoir accéder aux attributs (avant __init__)
    @property
    def _all_names_id(self):
        return self.all_names_id

    @property
    def _all_movies_id(self):
        return self.all_movies_id

    @property
    def _all_genders_id(self):
        return self.all_genders_id

    @property
    def _all_credits_positions_id(self):
        return self.all_credits_positions_id

    @property
    def _all_characters_id(self):
        return self.all_characters_id

    # création de @classmethod
    @classmethod
    def get_all_names(cls, id_list):
        merged_list = dict(zip(Character._all_characters_id, Character._all_names_id))  # dictionnaire qui met
        # ensemble les listes all_characters_id and all_names_id
        list_all_names = []
        for ids in id_list:
            list_all_names.append(merged_list[ids])
        return list_all_names

    @classmethod
    def get_all_movies_id(cls, id_list):
        merged_list = dict(zip(Character._all_characters_id, Character._all_movies_id))  # dictionnaire qui met
        # ensemble les listes all_characters_id and all_names_id
        list_all_movies = []
        for ids in id_list:
            list_all_movies.append(merged_list[ids])
        return list_all_movies

    @classmethod
    def get_all_genders_id(cls, id_list):
        merged_list = dict(zip(Character._all_characters_id, Character._all_genders_id))  # dictionnaire qui met
        # ensemble les listes all_characters_id and all_names_id
        list_all_genders = []
        for ids in id_list:
            list_all_genders.append(merged_list[ids])
        return list_all_genders

    @classmethod
    def get_all_credits_positions_id(cls, id_list):
        merged_list = dict(
            zip(Character._all_characters_id, Character._all_credits_positions_id))  # dictionnaire qui met
        # ensemble les listes all_characters_id and all_names_id
        list_all_credits_positions = []
        for ids in id_list:
            list_all_credits_positions.append(merged_list[ids])
        return list_all_credits_positions

    @staticmethod
    def create_character_dataset(provided_data):
        for line in provided_data.splitlines():
            line = str(line)
            parts = line.split('\t')

            try:
                credits_pos = int(parts[5])
                if credits_pos == 1000:
                    credits_pos = '?'
            except:
                credits_pos = '?'

            entries = {
                'character_id': parts[0],
                'name_id': parts[1],
                'movie_id': parts[2],
                'gender_id': parts[4],
                'credits_position_id': credits_pos,
            }

            Character.all_character_objects.append(
                Character(**entries)
            )

            Character.all_characters_id.append(entries['character_id'])
            Character.all_names_id.append(entries['name_id'])
            Character.all_movies_id.append(entries['movie_id'])
            Character.all_genders_id.append(entries['gender_id'])
            Character.all_credits_positions_id.append(entries['credits_position_id'])
        return