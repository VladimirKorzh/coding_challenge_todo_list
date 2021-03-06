
Repository views: [![HitCount](http://hits.dwyl.com/VladimirKorzh/coding_challenge_todo_list.svg)](http://hits.dwyl.com/VladimirKorzh/coding_challenge_todo_list)

Build: [![CircleCI](https://circleci.com/gh/VladimirKorzh/coding_challenge_todo_list/tree/master.svg?style=svg)](https://circleci.com/gh/VladimirKorzh/coding_challenge_todo_list/tree/master)
[![Maintainability](https://api.codeclimate.com/v1/badges/14f8e2ad273dfd4a3645/maintainability)](https://codeclimate.com/github/VladimirKorzh/coding_challenge_todo_list/maintainability)
[![Known Vulnerabilities](https://snyk.io/test/github/dwyl/hapi-auth-jwt2/badge.svg?targetFile=package.json)](https://snyk.io/test/github/VladimirKorzh/coding_challenge_todo_list?targetFile=requirements.txt)

---
The story is that one of higher level executives came up to you and asked for a favor at 2pm on friday.
![MEME](https://memeexplorer.com/cache/855.jpg) 
```
Can you quickly mock up an api and spin it up on one of our servers? 
I only have some general idea on what it should do, but we'll expand on it in the future. 
If, you'd do it that'd be great =)
```
---

# Initial API Requirements
1. Please create a server application with the API documented in `api-doc.md` file
2. Design an API change to make it possible to create a nested list of subtasks for every task (even for subtasks)
3. Use any testing framework and write tests
4. Create a docker script for deployment

# Some additional stuff that I've done while working on this project
- multiple API response formats: `JSON`, `PLAINTEXT`, `XML`
- API versions and is able to host multiple versions side by side (using Flask blueprints) 
- multiple nested configuration files 
- overriding configuration file on-the-fly using environment variable
- Project is using `Redis` as an in-memory data storage
- Endpoint documentation located in `api-doc.md` file
- All required modules are in `requirements.txt` file
- Postman collection can be found in `avocode_todo_list.postman_collection.json` file
- Data model is separated in `/src/model/todo_task.py` file
- Tests are written using `PyTest` framework

![MEME](https://memeexplorer.com/cache/700.jpg) 

# Running using docker
Clone the code over to your local machine
`git clone`

Build and run the images
`docker-compose up` 

Run the tests
``` ./pytest ```

# Running within local environment

Clone the code over to your local machine
` git clone `

Run a local instance of redis that would be used for storing the tasks 
``` docker run --name todoredis -p 6379:6379 -d redis:alpine ```

Install required modules in your virtual environment (don't forget to use one)
``` pip install -r requirements.txt```

Run the tests
``` ./pytest ```

You could always run the server itself `run.py` and perform manual testing from within Postman or a similar app.
I've included a Postman collection for testing the endpoints, simply import `avocode_todo_list.postman_collection.json`
and you will instantly get all the necessary bindings. 

# Some tips and tricks
To delete all containers including its volumes use
```docker rm -vf $(docker ps -a -q)```

To delete all the images,
```docker rmi -f $(docker images -a -q)```

Remember, you should remove all the containers before removing all the images from which those containers were created.


# Good luck

![MEME](https://memeexplorer.com/cache/689.jpg) 



