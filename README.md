# Engineering-toxicity-monitor
Final Project of Data Engineering Courses

## Authors
- [***Enzo Aleixo-Carvalho***](https://github.com/ealeixoc-99)
- [***Florian Marques***](https://github.com/MarquesFlorian)

## Run the Project
Pending

## About the Project
- The end of the project is the 28 February
- The project report is a docker image stock on the free docker hub and a readme to explain how the project works
- Use a [Trello](https://trello.com/b/RYurjzNj/tablefeaturerepartition)
- We will have to create branches for each feature and branches for each version.
- Use the CD version control branching system : master, develop, feature-..., release-...
- Technos used :
  - .
  - .

## The Web Application
- It contains a form input and a submit button
- The User can write an english sentence into the form input and when he click on the submit button, the sentence will be send to the Back which will inspect it with a model to determine if the sentence contains Toxicity or not. Then, the back will return statistics of the sentence to the Web Application which gonna print the statistics.

## The Back-end
- Receive front-end informations to analyze a sentence with the model
- Send statistics given by the model to the Front-end

## The Model 
This [model](https://huggingface.co/unitary/toxic-bert) analyze a sentence to determine the toxicity which it contains.



## Tests
We need to try each part of our application and each features, so they're differents type of tests :
- Unit Tests : Test each features
- Integration Tests : Send a request from the front to the back
- End-to-end Tests : Try the entire feature of our application (the main feature)
- Stress Tests : Tests 100 request per minutes

## Deployments
The application need to be easily deploy, so we're gonna use Docker with docker-compose

## Automate the application
We need to automatize the application on differents steps with Jenkins :
- Build : build and run unit tests on feature branches
- Test : run other tests and push to release on the develop branch
- Deployment : wait user for acceptance on the release branch before pushing to master
- Release : deploy on merging with master

## Monitoring (Prometheus)
The application need to be monitored after the deployment to determine easily and quickly if issue appears, and to resolve it.
So, we're gonna check :
- hardware metrics ( cpu usage, memory usage, disk space usage)
- software metrics (integrate different software metrics inside your application to monitor information like response time, user requests count, exceptions)

And we're gonna add rules and alerts where you see fit, here are some examples :
- Alert before running out of memory
- Alert when cpu usage is very high
- Alert when your code raises an exception
- Alert when your system is down for more than a specific period of time

To monitore dashboard, we'll use Grafana, it will help us to visualize the different monitored metrics during the stress test.
