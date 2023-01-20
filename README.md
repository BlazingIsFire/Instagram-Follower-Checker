# Instagram Follower Checker

I created this Python script over the course of two days. This script simply takes your Instagram following JSON data and compares it to your Followers JSON data. I have included instructions below on how to retrieve your own Instagram data and import it to this script.

**Instructions (How to use):**

1. Navigate to your Instagram profile in a browser.
2. Click on the settings / gear icon near your username.
3. Select the "Privacy and Security" section in settings and scroll to the middle of the page.
4. Find a section called "Data Download". 
5. Click on the request data text and input your email. (Note: It could take up to 48 hours for your data to be sent to your email, however it usually only takes 20 minutes.)
6. Once you receive the email with your data file, download your data file. 
7. Open the ZIP file and then go into the folder named "followers_and_following".
8. From here, copy the files named "followers.json" and "following.json".
9. Paste these two files in the folder named "files" that's in this directory.
10. Simply run the python file named "igfollowerchecker.py". It will run and create a .txt file named "notfollowing.txt". In this file it will display all the people that are not following you back.

Hope you enjoy!
