# user-service
## Requirements
* [Docker](https://www.docker.com/)
  * If you are using Linux
  please make sure Docker Engine installed and running.
  Instructions could be found here
  https://docs.docker.com/engine/install/
  * If you use Windows or macOS
  please make sure Docker Desktop is installed and running.
  Instructions could be found here
  https://docs.docker.com/desktop/#download-and-install

### Optional
* [Python 3.9](https://www.python.org/downloads/release/python-390/)
* [Poetry](https://python-poetry.org/)
* [PostgreSQL](https://www.postgresql.org/)

## start or stop application

To run the application use terminal or command prompt and scripts in directory.
For macOS and Linux users check the `_nix` one and for Windows take a look at the `windows` one.

### linux or macOS
```commandline
sh ./scripts/_nix/start.sh
```
```commandline
sh ./scripts/_nix/stop.sh
```
### windows
```commandline
./scripts/windows/start.cmd
```
```commandline
./scripts/windows/stop.cmd
```

## Documentation
* Swagger http://127.0.0.1:8000/docs#
* ReDoc http://127.0.0.1:8000/redoc#


## Challenge: User service
The objective of this exercise is to implement a rest-service which is able to:

- Create new user with contact data +
- Return user by id +
- Return user by name +
- Add additional mail/phone data +
- Update existing mail/phone data 
- Delete user +

The data objects are defined as followed:
```
User:
    id: <int>
    lastName: <string>
    firstName: <string>
    emails: List<Email>
    phoneNumbers: List<PhoneNumber>

Email:
    id: <int>
    mail: <string>
    
PhoneNumber:
    id: <int>
    number: <string>
```

#### Constraints
- You provide straightforward documentation how to build and run the service
- Submitted data is stored in database (free choice which one)
- You can only use the following programming languages: Scala, Java, Python


#### Bonus
- You let your service run within a container based environment (Docker, Kubernetes)
- You provide documentation of your services API endpoints
- Your service is covered with tests