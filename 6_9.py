# ------------- LESSON 6, EXERCISE 9 -------------------
# There is dictionary of dictionaries. Show names who doesn't have an email

users_dict = {1: {'name': 'Jack', 'surname': 'Daniels', 'phone': '+45645344', 'email': ''},
              2: {'name': 'Katrin', 'surname': 'Holland', 'phone': '+956345344'},
              4: {'name': 'Mag', 'surname': 'Rich', 'phone': '+345634544', 'email': '34@gmail.com'},
              6: {'name': 'Dan', 'surname': 'Island', 'phone': '+156645344', 'email': 'esrfgaestf'},
              13: {'name': 'Rodger', 'surname': 'Goldy', 'phone': '+865645344'},
              56: {'name': 'Hues', 'surname': 'Landscape', 'phone': '+635645344', 'email': ''},
              }

print(', '.join([user['name'] for user in users_dict.values() if 'email' not in user.keys() or user['email'] == '']))
