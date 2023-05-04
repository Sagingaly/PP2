import random
import pandas as pd

kz_first_names_latin = ["Aigerim", "Aidana", "Aizhan", "Ainur", "Aiserik", "Aisha", "Aisholpan", "Aiyym", "Akbota", "Akmara",
               "Alisher", "Almira", "Amanzhol", "Amina", "Anar", "Anara", "Anelia", "Ansar", "Aruzhan", "Asem",
               "Asylkhan", "Askar", "Assel", "Ahmet", "Ayauly", "Bauyrzhan", "Gulzhan", "Daniyar", "Dariga", "Erzhan"]

kz_phone_numbers = []
for i in range(30):
    kz_phone_numbers.append(int("8" + str(random.randint(700, 799)) + str(random.randint(100, 999)) + str(random.randint(1000, 9999))))

data = {"phone": kz_phone_numbers, "username": kz_first_names_latin}

df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)

print(df)
