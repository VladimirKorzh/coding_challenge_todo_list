
Hi there! 
This is a repository for a code challenge by Avocode company which I am applying to.
 
---
The story is that one of higher level executives came up to you and asked for a favor at 2pm on friday. 
```
Can you quickly mock up an api and spin it up on one of our servers? 
I only have some general idea on what it should do, but we'll expand on it in the future. 
If, you'd do it that'd be great =)
![alt text](https://www.google.com.ua/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwj-lP2WlY7fAhWhk4sKHZr_BkcQjRx6BAgBEAU&url=https%3A%2F%2Fmemeexplorer.com%2Finternet-memes%2Fthat-would-be-great%2Fyeah-if-you-could-go-ahead-and-wrap-this-meeting-up%2F957&psig=AOvVaw0UhUTMrjJwIpXiVGWIot0B&ust=1544287437007076) 
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


# Running within local environment

Clone the code over to your local machine
` git clone `

Run a local instance of redis that would be used for storing the tasks 
` docker run --name todoredis -p 6379:6379 -d redis:alpine `

Install required modules in your virtual environment (don't forget to use one)
` pip install -r requirements.txt`

Run the tests
` ./pytest `

You could always run the server itself and perform manual testing from within Postman or a similar app.
I've included a Postman collection for testing the endpoints, simply import `avocode_todo_list.postman_collection.json`
and you will instantly get all the necessary bindings. 

