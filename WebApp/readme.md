# WebApp Project 
### by caiofook
---
🔥 _**Last edit: 30.06.23**_

---

### About the Project
This is a simple and generic web application written mostly in python (django framework) and javascript.
- It is a personal project with the purpose of get me into the django framework. It was very good to make me finnaly understand Django's MVT arquitecture and Django tags. 
- For this purpose, it is basicaly a website with a hub of smaller web applications, in order to **cover most of common features of modern websites**.
- Since it's a learning project, **I tried to comment everything**.. for me and for anyone that finds it and hopes to learn something about Django.

By the end, there should be 3 "apps" inside the project:
- a **blogpost app**
- a **habit tracker app**
- a **private notes app**

In fact, one could say there are 5 apps in total, cause the Users feature **(Users App)** and the Apps hub **(WebApp app)** are threated by django as apps as well. 



It is a ongoing process with a few steps:

✅1. get the major app working (a blogpost)
✅2. implement the sqlite3 database (no more dummy data)
✅3. implement the authentication features 
✅4. implement the email-server-dependent features (the user's password reset)
✅5. implement the second app (the Tracker)
✅6. adjust the Tracker app to save data on database (no more localStorage)
⚠️7. correct minor bugs (like some images not loading or an ugly layout in some pages)
⚠️8. implement the private Notes app
⚠️9. implement a API for the private Notes app
⚠️10. implement the authentication for the private Notes API
⚠️11. deploy the project in order to conduct a pentest over it (by this point, not really worried about vulnerabilities that may arise. Just part of the schedule xD)

---
### How to Use

Althought this is a project for learning purposes, if someone desires to get it working on your own localhost, a few steps must be followed:
- change the email_host, the email_pass and the secret_key in the settings.py;
- install all the requirements in the requirements.txt file;
- admin: 
- run python web server


---
### DISCLAIMER
The Tracker App was originally copied from Rocket Seat's bootcamp. It implements a JS library created by [maykbrito](linkaqui.com). 
It was a "only frontend-localStorage page", that I incorporated inside the Djando Project and implemented the necessary models for persistence on database. So each User of the WebApp have now it's own habit-tracker-data on sqlite3.