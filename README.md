# Genre_music_classification_BERT

The code can be run without the need of downloading external commands. The webscrapping have several external files which can make it easier to run the code without the limitations of Google Colab.

To use the Kaggle API, sign up for a Kaggle account at https://www.kaggle.com. Then go to the 'Account' tab of your user profile (https://www.kaggle.com/<username>/account) and select 'Create API Token'. This will trigger the download of kaggle.json, a file containing your API credentials. This file must be placed in contents.
  
 The library Genius requires to login to obtain a token, place it in a json as:
  
  ```json
  {"token":"<your_token>"}
  ```
  
  Along the code there are several -unnecessary- saves to songs.csv file, in case the colab ran out of time or memory.
  
  
  lyrics.py webscrape the lyrics, it can take up to 5 hrs
  
  web_scrapping.py get the mp3 file from youtube videos, the song.csv must already contain the youtube links to work properly. This process can take several days.
  
  
  
  
