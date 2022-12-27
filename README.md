<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Szezi/TasksManager">
    <img src="data\images\dashboard.png" alt="Dashboard">
  </a>
<h3 align="center">TasksManager</h3>
  <p align="center">
TasksManager is a web application that allows users to create multi-users kanban boards and tasks. Application allows user to fill information about themselves in profile page and see stats on dashboard. <br />
    <a href="https://github.com/Szezi/TasksManager"><strong>Explore the docs »</strong></a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
      <ul>
        <li><a href="#technologies">Technologies</a></li>
      </ul>
    </li>
    <li><a href="#about-yhe-project">About the project</a></li> 
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- GETTING STARTED -->
## Getting Started

To run this project, create virtual environment and install it locally.

### Installation

1. Clone the repo
   ```sh
   $ git clone hhttps://github.com/Szezi/TasksManager
   ```
2. Install packages
   ```sh
   $ pip install -r requirements.txt
   ```
3. Make migrations
    ```sh
   $ python manage.py makemigartions 
   ```
4. Migrate
    ```sh
   $ python manage.py migrate 
   ```
5. Create superuser
    ```sh
   $ python manage.py createsuperuser 
   ```
6. Run server
    ```sh
   $ python manage.py runserver   
   ```


### Technologies

* [Python](https://www.python.org/downloads/release/python-390/)
* [Django](https://www.djangoproject.com)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ABOUT THE PROJECT -->
## About The Project
TasksManager is a web application that allows users to create multi-users kanban boards and tasks. Application allows user to fill information about themselves in profile page and see stats on dashboard. <br />
To see different pages of application user need to be logged in. If unauthorised user try to view other pages will be automatically redirect to Home page.

Frontend design is based on :https://www.creative-tim.com/product/soft-ui-dashboard

### Home page

<div align="center">
<img src="data\images\home.png" alt="home">
</div>

Application welcome user with home page. It allows user to log in or create new account.
If user is already logged in it automatically redirect user to dashboard page. Moreover, if user is logged in it is forbidden to create new account.


### Profile

<div align="center">
<img src="data\images\profile.png" alt="home">
</div>

User during registration creates new profile with avatar, description and basic information about user.

### Dashboard

<div align="center">
<img src="data\images\dashboard.png" alt="home">
</div>

Dashboard page allows user to keep track with basic information about its tasks. 
On top there are stats with numer of task done, in progress, to do and number of boards user is member of.
On dashboard page user also can create new board and task, keep track on boards is administrator of and also pin most important task to do.

### Kanban board

<div align="center">
<img src="data\images\board_create.png" alt="home">
</div>

User can create his own kanban board. All he needs to do is select who will be its administrators, fill name and description of the board and add other members.

<div align="center">
<img src="data\images\kanban_board.png" alt="home">
</div>

Board has three columns: next, in progress and done. User can add new task, fill the info and assigned it to the members of the board.
Board also has filtering that allows user to view specific type of tasks.

<div align="center">
<img src="data\images\task_detail.png" alt="home">
</div>

To see more details user need to click on the name of task or the button to view the modal with tasks details.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the GPL-3.0 license. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/Szezi/TasksManager](https://github.com/Szezi/TasksManager)

<p align="right">(<a href="#top">back to top</a>)</p>
