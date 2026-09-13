import sqlite3
import datetime

conn = sqlite3.connect("messages.db")

cursor = conn.cursor()

'''
cursor.execute("CREATE TABLE IF NOT EXISTS messages ("
               "id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "message TEXT NOT NULL,"
               "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP )"
            )

conn.commit()
conn.close()
print("Database created")'''

import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] =""
msg["From"] = "mustafaeneskoksal@gmail.com"
msg["To"] = "mustafaeneskoksal@gmail.com"
msg.set_content(input("Enter your message here: "))
'''with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
   smtp.login("mustafaeneskoksal@gmail.com","anqtqasmwqqoxqax")
   smtp.send_message(msg)
'''
print("Email sent")

date = datetime.datetime.now().isoformat()
paragraph = msg.get_content().strip()
delete_query = "DELETE FROM messages "
cursor.execute(delete_query)
conn.commit()
post_query = "INSERT INTO messages (message) VALUES (?)"

cursor.execute(post_query, (paragraph,))
conn.commit()

get_query = "Select *  FROM messages "
cursor.execute(get_query)
rows = cursor.fetchall()
for row in rows:
    print(row)


conn.commit()
conn.close()
print("test is successful")



