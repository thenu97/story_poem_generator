# Documentation
---
# Poem & Story Generator

This is for the second project due Week 9 of the DevOps February 17 2020 intake cohort.

## Table of Contents

1. [Project Brief](#project-brief)
    + [Proposal](#proposal)
    + [Wireframes](#wireframes)
2. [Trello Board](#trello-board)
    + [Start Point](#start-board)
    + [Rolling Changes](#rolling-changes)
    + [End Point](#end-point)
3. [Risk Assessment](#risk-assessment)
4. [Project Architecture](#project-architecture)
    + [Architecture Diagram](#architecture-diagram)
    + [Issues Encountered](#issues-encountered)
5. [Design Considerations](#design-considerations)
    + [Front End](#front-end)
    + [Back End](#back-end)
    + [UI](#ui)
6. [Testing](#testing)
    + [Pytest Testing](#pytest)
    + [Final Report](#final-report)
7. [Deployment](#deployment)
    + [Toolset](#toolset)
8. [Improvements for Future](#improvements-for-future)
9. [Author](#authors)

## Project Brief

The project requires a mirco-service oreintated architecture of a web application, which must be composed of at least 4 services that work together. With backend written in Python, Jenkins for CI service, and Ansible & Docker for CD.

### Proposal

My proposal focuses on the creation of a website for poetry and story genertor based on user input. 

### Wireframes

<img width="500" alt="portfolio_view" src="https://i.imgur.com/PUFseOa.jpg" title="wireframe1" />

My initial idea was to have a simple button so when the user pressed it, it displayed a story of a random theme with random character names substituted in it. In other words, service two picks out a theme at a random from a list of three and service three picks out a male and female character name from a list of fourteen, for which service four puts it all together and sends it back to service one. 

<img width="500" alt="portfolio_view" src="https://i.imgur.com/hHp9W7x.jpg" title="wireframe2" />

To make it more user friendly/interactive, I changed it so that the user gets to choose the theme and character name they want by adding user input. This shortened the character name lsit to three from fourteen. 

<img width="500" alt="portfolio_view" src="https://i.imgur.com/WJTj9tO.jpg" title="wireframe3.1" />

<img width="500" alt="portfolio_view" src="https://i.imgur.com/IACN03Z.jpg" title="wireframe3.2" />

In the end, instead of having service four take a lot in with sending a whole story over to service one, I thought I could just store the literacy pieces in service one and have service four just choose between poem and story depending on service two and three. 


## Asana Board

I used a kanban board on Asana to manage my workflow during the project. Agile methodology was implemented in line with the brief, in terms of product and sprint backlog, although due to the individual nature of the project, no scrum working practices were applied. The board was set up with reference to potential user stories. I split the sprints into smaller tasks in order to keep the requirements of the project spec clear.

Due to this setup sprints could be passed through development, and, if required, testing, before being assigned to Done. Once sprints generated by a backlogged Task have been completed, the task itself can be marked Done. Functionalities that requirement more time and weren't neccessary to implement are given over to the newly added Dropped ideas column.

### Start Point

<img width="200" src="https://i.imgur.com/fMVWd2r.jpg" title="product backlog" /> <img width="200" src="https://i.imgur.com/stOZ67u.jpg" title="sprint backlog" /> <img width="200" src="https://i.imgur.com/3OQBSDR.jpg" title="user stories" /> <img width="100" src="https://i.imgur.com/KQNZeaX.jpg" title="moscow key" />

<img src="https://i.imgur.com/Iblbwox.png" title="sprint1" />

At the start of the project, I focussed on the five tasks most easily completable in the first week of training: Starting the Kanban board [itself](https://app.asana.com/0/1169906447683321/board), starting this documentation, instituting a github repository for the project, which can be found [here](https://github.com/thenu97/SFIA-PROJECT2-QA), initialising the risk assessment for the project in line with my initial understanding, and researching Docker covered in lesson as we went along.

### Rolling Changes

![User Story After](images/usrstraft.JPG)

+ The first major change to the Kanban board to changing my idea from a user pressing a button to selecting data; theme and character names. This meant I had to change my html code and find a way to communicate the user input to service two and three. Then communicate this info to service four at the same time. I spent most of my time researching flask before_requests and after_requests, and using global variables to store data coming in at different times. 

![Sprint Two](images/sprint(2.1).png) 

+ As I was using global variables to solve my issue of post requests coming in at different times, I was faced with another issue when replicating the container for docker swarm. The global variables were container specific so when I was replicating it, the global variables reset to empty. To solve this, I had three options: to replicate the services utilising global variables once and document the issue, research into docker volumes and see if there's a way of replicating the containers based on the volumes of the original container, or re-design my entire application to ensure it wasn't using global variables at all. In the end, I went with the third option and gave myself a day to re-design the application and if it wasn't completed within that time-frame to result in the first resolution. 

![Sprint Two Continued](images/sprint(2.2).png)

+ Reaching the end of week two, I had an application that didn't use global variables and had also found a way to programme Ansible to set the environment (downloading docker) assign worker/manager nodes without having to ssh into each virtual machine and manually doing it ourselves. I also researched into what I had to do for testing so added that onto to Yet to start on the kanban board. 

+ I started researching into testing such as SonarQube (static testing tool) and Selenium (dynamic testing tool).

![Final Sprint](images/sprint(3).png)

+ Testing commentary awaits...

### End Point
![Everything done](images/sprint(4).png)


## Risk Assessment

|Risk No.|Risk|Effect|Likelihood|Serverity|Importance|Mitigate|
|---|---|---|---|---|---|---|
|1|Not understanding the brief given.|Failed project|2|5|10|Ask as many questions as possible, research, re-read.|
|2|Problems with developing 4 services.|Failed project as this is a needed requirement|3|5|15|Do more research into mircoservices and how systems involved work together.|
|3|Overrunning on GCP free data limits.|An instance is left running, or an account breach enables the resources on the account to be drained.|1|5|5|Continue monitoring GCP usage. Copy databases offline as final backup.|
|4|Problems with Python/Flask|Failed project as this is needed for the front end and backend of my application.|1|5|5|Practise Python through continuous challenges on Codewars.|
|5|Problems with Jenkins|Not being able to CI/CD|2|5|10|Do more research into using Jenkins with Docker Swarm.|
|6|Using Ansible Playbook|The project requires this but due to not using ansible before, this holds a great risk.|3|5|15|Study how Ansible is used through documentation provided and asked my trainer for resources.|
|7|Docker|Required by the project but I haven't used this tool before so it holds high risks.|4|5|20|Research and docker documentation.|

![Risk Matrix](images/riskmatrix.png)

To be commented on later... 


|Risk No.|Risk|Solution|
|---|---|---|
|1|The brief being too hard to decipher|Asked my peers, and emailed my manager to join our daily standups who explained the brief in more detail.|
|2|Developing mircoservices as it was a new concept to me|I put in hours of research to figure out how everything interlinked.|
|3|GCP free credit running out|I stopped an instance when it wasn't being used and monitored the rate of credit drop.|
|4|Facing issues with python/flask|Ensured I was doing at least 3 challenges a day to keep my python knowledge on pur.|
|5|Jenkins automated build|I researched into how Docker Swarm tied in with Jenkins and drew a pipeline that help me grasp the idea better.|
|6|Ansible - worker nodes|Researched into it and I was eventually able to support my colleagues with a solution that managed docker clusters.|
|7|Docker Swarm|Docker wasn't as hard as I expected to understand. Continuous practise helped a lot.|


## Project Architecture

### Overall Architecture

![Overall](images/pipeline(num).JPG)

At stage one, once the code is changed on visual studios, you push it up to GitHub. This initiates an automated Jenkins build at stage two. Jenkins then ensures ansible is started up at stage three. Ansible then pushes the new built image to Docker registry (Docker Hub). Ansible also assigns worker/manager nodes at stage four. At stage five, the manager node pulls down the image from Docker Hub and creates multiple containers (defined in docker-compose file) then deploys it to the worker nodes that are assigned to it. In my case, only one worker node was created. 

![Communication](images/architecture.JPG)
The user presses a button that generates a random story. As the user only interacts and sees service one, HTML post and get requests were used to share information between the services. When we containerised our applications, we linked the containers by creating a docker network and allowing the connection to flow the same way as before. 

### Issues Encountered

+ 

+ 


## Testing

### Pytest

### Final Report


## Deployment

### Toolset

+ GCP Instance development environment

+ GitHub Webhook

+ Jenkins Server

+ Pipeline build coded in Groovy and Shell.

+ Testing in Pytest using the Coverage module.

+ Ansible

+ Docker/Docker Swarm


## Improvements for Future Versions



## Authors

Thenuja Viknarajah
