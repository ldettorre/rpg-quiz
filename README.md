# RPG Quiz - App Name: What The RP?!


## Django Project using a Dungeons & Dragons API.
###### This project is intended for educational purposes only.

A quiz site that takes the users selections and suggests what class they might be interested in within the Dungeons and Dragons role playing game based off of those selections.
## Description

"What The RP?!" is a quiz app that uses a combination of the 'Would You Rather’ style coupled with weighted selections and content from the popular role playing game, Dungeons and Dragons, in order to create a fun way of picking a class. Picking a class In D&D is one of many important and fun decisions the player makes before getting started on their fantasy journey. It is also one which can require reviewing an immense amount of content. Having realised this after dabbling in a game with friends, I began to think perhaps there could be a fun and creative way to make this decision!

What I came up with was a quiz where users are repeatedly given 2 randomly selected and paraphrased spells/abilities to choose between, which are weighted. They will then continue to make selections until a threshold is met. Currently, the threshold is a hardcoded number(20) and the weight of each selection is dictated by the level of the spell in a 1:1 ratio. So a level 1 spell is worth 1 point, level 2 is worth 2 and so on.

The main goal of this approach is expose users to many spells and abilities at random, allowing them to judge between which they would most like to use in the game and then present the class most relevant to their selections. It's important to clarify that nowhere during the quiz do users see the class(es) behind their selections, either past or present. 
 

To view the live version of this site, click [here!](https://rpgquiz.herokuapp.com/)

## UX and UI

When it came to the UX and UI for the site, I initially planned on having it be as easy to use as it was to complete the quiz. After having the minimum viable product completed and then adding some additional CSS for effects and responsiveness, I found that the level of simplicity the site naturally had based on my original intention served it well.

That being said if I decide to implement additional features down the line, both the UX and UI will evolve with the original principle in mind.

For inspiration, I found [Either.io](https://either.io/) to be a great example on how a basic preference style UI can work. The site also had some additional features such as the ability to recall previous selections and a members area to submit questions which can act as a new avenue to explore for "What The RP?!".



### Technologies Used And Summary
* HTML
* CSS
* Bootstrap Version 4.5.2
* Python 3.8.2
* Django 3.1.4 Framework
* [D&D 5th Edition API](https://www.dnd5eapi.co/)
* Heroku - Deployment
* Postgresql Database
* pgAdmin - DB development platform


Bootstrap was used because a simple grid system would satisfy what I needed from the UI perspective. However I also knew that it would work extremely well with Jinja when rendering templates and views from Django.

I chose Django because its expansive feature set would help greatly over the entire app especially if I was to expand in the future. My plan initially was to create a custom spell model for each entry, then create a function to query the D&D API for each spell and ability. Once the function worked and could print the objects requested, I would amend it to use the create method and populate the db with those objects. Finally, the admin dashboard would allow me to review what was created and make any changes on the fly. 

Heroku was chosen for deployment because of its use of web hooks made the early stages of deployment much easier. The built in command line and logs also meant any bugs encountered could be tackled more efficiently. Praise the Logs!

I forwent the use of a separate cloud storage as there was minimal static or media being used and to me, that did not warrant going through something like AWS S3 storage this time around. 
Ultimately, I chose the technologies listed above because I knew I could use my experience with them to hit the ground running.

## Features

### Existing Features

###### Site Specific:
* The site is responsive through it's use of Bootstrap.
* The site temporarily stores weighted quiz selctions in the backend via the use of Django sessions.
* The site takes the selections and adds them to the running total for the quiz, triggering a result when the threshold is met.
* The site resets the quiz score and session data if the user does anything other than select an option. Going back a page or refreshing the page causes the quiz to reset.
###### As the Site Admin:
* You can create custon spells/abilities with a name, description, level, points, fantasy universe and an is_included field.
* You can mark certain spells/abilities to be included in the quiz or left out.
* You can run custom management commands to repopulate the database with spells, abilities and classes from the D&D API.


### Possible Future Features 

From a user perspective, I could add an accounts app where users will register and save their results. The initial idea behind that is to then provide recommendations for other games that have similar classes incase they wish to expand their game library.

From a site admin perspective, I could look into adding additional games such as World of Warcraft or Pathfinder. This would create a more diverse database of content and increase the replayability factor.

I can also see there being huge room for improvement from a UX perspective. Implementing JavaScript or a frontend framework might allow for a more polished and 'magical' experience with aesthetic features.


## Deployment and Hosting
The steps provided assume that you have forked the repository to your GitHub already.

* Sign into Heroku, click new in the top right hand of the page and click on create app.
* Provide an app name, select the region relevant to you then click 'create'.
* Within the Deploy tab of your app dashboard, locate ‘Deployment Method’ and select GitHub. You will then need to enter the app name and select it.
* Within the Resources of the dashboard, you will need to scroll to ‘Add-ons’ and enter ‘Heroku Postgres’. Ensure that you select the ‘Hobby Dev - Free’ Tier.
* You will then need to locate the Settings tab and scroll down to 'Config Vars' where you will enter the project ‘config vars’ or ‘environment variables’.
* These are the DATABASE_URL, DJANGO_SETTINGS_MODULE, PGHOST, PGNAME, PGPASSWORD, PGUSER, and SECRET_KEY.

Note that we did not set a DEBUG config var as this will default to False as seen in the base.py file. 

Once the above has been completed you can return to the Deploy tab, scroll down to ‘Manual Deploy’ and click ‘Deploy Branch’. Should you encounter any issue, I would recommend then consulting the log by returning to the app dashboard within Heroku, clicking on 'More' in the top right and selecting 'View Logs'. You may need to redeploy the app with the log opened in order to see an entire account of what happened. While you could create a config var called DEBUG and set it to True in order to receive the famous 'yellow page error', please ensure you remember to remove it when you're done.

### Running Locally
To get this project running locally, you will need to clone the repository and install the requirements.txt file. Following that, you must ensure all secret keys, as noted in the Deployment section, are set up. For this project I used [python-decouple](https://pypi.org/project/python-decouple/) which worked brilliantly and was extremely simple. You can also use an env.py file if preferred. 

You should then create a superuser and run makemigrations/migrate in order for it and the models to be applied. Your allowed hosts will also need to be updated with the address returned in the browsers error message upon first running the app.

## Content
The quiz content consists of spells and abilities taken from the [D&D 5th Edition API](https://www.dnd5eapi.co/). 

The background image came from [Pixabay](https://pixabay.com/) and was free for use.



