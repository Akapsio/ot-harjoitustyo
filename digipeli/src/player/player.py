import csv

class Player:

    def __init__(self, username: str):
        if self.check_name_availability(username):
            self.nimi = username
            self.add_new_user_to_list(username)
        else:
            raise ValueError("Nimi on jo käytössä")

    def check_name_availability(self, username: str):
        name_available = True
        with open('/home/Desktop/ot-harjoitustyo/digipeli/src/repositories/players_list.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                    continue
                else:
                    if row.__contains__(username):
                        return False
                line_count += 1
        return True

    def add_new_user_to_list(self, username: str):
        with open('repositories/players_list.csv', 'w', encoding='UTF8', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.write(f"{username}, 0")
