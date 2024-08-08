# import os
# import time
# import pandas as pd
# from instabot import Bot
# from dotenv import load_dotenv
# import schedule
# from datetime import datetime

# # Load environment variables
# load_dotenv()

# username = os.getenv("username")
# print('username: ', username)
# password = os.getenv("password")
# print('password: ', password)

# # import os 
# # import glob
# # cookie_del = glob.glob("config/*cookie.json")
# # os.remove(cookie_del[0])

# # Create bot instance
# bot = Bot()

# # Login using bot
# try:
#     bot.login(username=username, password=password)
# except Exception as e:
#     print(f"Error during login: {e}")
#     exit()

# # Load user data from Excel
# excel_file = 'birthdays.csv'
# df = pd.read_csv(excel_file)
# print('df: ', df.head())

# def send_birthday_message():
#     today = datetime.now().strftime('%d-%m')
#     print('today: ', today)
#     birthday_users = df[df['Birthday'].apply(lambda x: x.strftime('%d-%m')) == today]
#     print('birthday_users: ', birthday_users)

#     text = "Happy Birthday! 🎉🎂 Wishing you all the best on your special day."

#     for _, row in birthday_users.iterrows():
#         user_id = row['Username']
#         try:
#             bot.send_message(text, [user_id])
#             print(f"Message sent to {user_id}")
#             time.sleep(60)  # Sleep for 60 seconds between each message to avoid rate limits
#         except Exception as e:
#             print(f"Error sending message to {user_id}: {e}")
#             time.sleep(300)  # If rate limited, sleep for 5 minutes

# # Schedule the job to run every day at 12:00 AM (midnight)
# schedule.every().day.at("17:29").do(send_birthday_message)

# while True:
#     schedule.run_pending()
#     time.sleep(1)


# import os 
# import glob
# cookie_del = glob.glob("config/*cookie.json")
# os.remove(cookie_del[0])


#-----------------------


# import os
# import time
# import pandas as pd
# from instabot import Bot
# from dotenv import load_dotenv
# import schedule
# from datetime import datetime
# import random

# # Load environment variables
# load_dotenv()

# username = os.getenv("username")
# password = os.getenv("password")

# # Create bot instance
# bot = Bot()

# # Login using bot
# try:
#     bot.login(username=username, password=password)
# except Exception as e:
#     print(f"Error during login: {e}")
#     exit()

# # Load user data from Excel
# excel_file = 'birthdays.xlsx'
# df = pd.read_excel(excel_file)

# # Convert the 'Birthday' column to datetime format (ignoring errors if any)
# df['Birthday'] = pd.to_datetime(df['Birthday'], errors='coerce', format='%d-%m-%Y')

# def send_birthday_message():
#     today = datetime.now().strftime('%d-%m')
#     birthday_users = df[df['Birthday'].apply(lambda x: x.strftime('%d-%m') if pd.notnull(x) else '') == today]

#     text = "Happy Birthday! 🎉🎂 Wishing you all the best on your special day."

#     for _, row in birthday_users.iterrows():
#         user_id = row['Username']
#         try:
#             bot.send_message(text, [user_id])
#             print(f"Message sent to {user_id}")
#             time.sleep(random.randint(60, 120))  # Random delay between 1 to 2 minutes
#         except Exception as e:
#             print(f"Error sending message to {user_id}: {e}")
#             time.sleep(random.randint(300, 600))  # If rate limited, sleep for 5 to 10 minutes

# # Schedule the job to run every day at 12:00 AM (midnight)
# schedule.every().day.at("00:00").do(send_birthday_message)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

#--------

# import os
# import time
# import pandas as pd
# from instabot import Bot
# from dotenv import load_dotenv
# import schedule
# from datetime import datetime
# import random

# # Load environment variables
# load_dotenv()

# username = os.getenv("username")
# password = os.getenv("password")

# # Create bot instance
# bot = Bot()

# # Login using bot
# try:
#     bot.login(username=username, password=password)
# except Exception as e:
#     print(f"Error during login: {e}")
#     exit()

# # Load user data from Excel
# excel_file = 'birthdays - Sheet1 (1).csv'
# df = pd.read_csv(excel_file)

# # Convert the 'Birthday' column to datetime format (ignoring errors if any)
# df['Birthday'] = pd.to_datetime(df['Birthday'], errors='coerce', format='%d-%m-%Y')

# def send_birthday_message():
#     today = datetime.now().strftime('%d-%m')
#     birthday_users = df[df['Birthday'].apply(lambda x: x.strftime('%d-%m') if pd.notnull(x) else '') == today]

#     text = "Happy Birthday! 🎉🎂 Wishing you all the best on your special day."

#     for _, row in birthday_users.iterrows():
#         user_id = row['Username']
#         try:
#             bot.send_message(text, [user_id])
#             print(f"Message sent to {user_id}")
#             time.sleep(60)  # Random delay between 1 to 2 minutes
#         except Exception as e:
#             print(f"Error sending message to {user_id}: {e}")
#             time.sleep(200)  # If rate limited, sleep for 5 to 10 minutes

# # Schedule the job to run every day at 12:00 AM (midnight)
# schedule.every().day.at("18:02").do(send_birthday_message)

# while True:
#     schedule.run_pending()
#     time.sleep(1)





import os
import time
import pandas as pd
from instabot import Bot
from dotenv import load_dotenv
import schedule
from datetime import datetime
import random

# Load environment variables
load_dotenv()

username = os.getenv("username")
password = os.getenv("password")

# Create bot instance
bot = Bot()

# Login using bot
try:
    bot.login(username=username, password=password)
except Exception as e:
    print(f"Error during login: {e}")
    exit()

# Load user data from CSV
excel_file = 'birthdays - Sheet1 (1).csv'
df = pd.read_csv(excel_file)

# Convert the 'Birthday' column to datetime format
df['Birthday'] = pd.to_datetime(df['Birthday'], errors='coerce', format='%d-%m-%Y')

# List of birthday wish templates
wishes_templates = [
    "Happy Birthday, {name}! 🎉 Wishing you a fantastic day filled with joy and surprises!",
    "Wishing you a very Happy Birthday, {name}! 🎂 May your day be as special as you are!",
    "Happy Birthday, {name}! 🎈 May all your dreams come true today and always!",
    "Happy Birthday, {name}! 🎁 Hope your day is as amazing as you are!",
    "Wishing you a wonderful birthday, {name}! 🎂 Enjoy every moment to the fullest!",
    "Happy Birthday, {name}! 🎉 May your year ahead be filled with success and happiness!"
]

def send_birthday_message():
    today = datetime.now().strftime('%d-%m')
    birthday_users = df[df['Birthday'].apply(lambda x: x.strftime('%d-%m') if pd.notnull(x) else '') == today]
    print('birthday_users: ', birthday_users)

    for _, row in birthday_users.iterrows():
        user_id = row['Username']
        name = row['Name']
        print('name: ', name)
        text = random.choice(wishes_templates).format(name=name)
        try:
            bot.send_message(text, [user_id])
            print(f"Message sent to {user_id}")
            time.sleep(60)  # Delay of 1 minute between messages
        except Exception as e:
            print(f"Error sending message to {user_id}: {e}")
            time.sleep(200)  # If rate limited, sleep for 5 minutes

# Schedule the job to run every day at 12:00 AM (midnight)
schedule.every().day.at("18:32").do(send_birthday_message)

while True:
    schedule.run_pending()
    time.sleep(1)
