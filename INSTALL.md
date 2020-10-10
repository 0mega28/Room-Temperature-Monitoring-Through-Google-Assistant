## Python Installations

```bash
    $ sudo apt-get update
    $ sudo apt-get install python3.8
```

check if the Installation was successful
``` bash    
    $ python3 --version
```
If correctly installed it will show the python version

---

## Flask Installations

``` bash
    pip3 install Flask
```

To check the Installation

```bash
    flask --version
```

It correctly installed it will show Python and Flask version

---

Type the below command to setup an URL for your localhost

```bash     
    ssh -R 80:localhost:[PORT_NUMBER] ssh.localhost.run
```
Replace the [PORT_NUMBER] with the Port Number like(8081) which you want to use for getting the POST request

e.g. I have used 8081 port
```bash
    ssh -R 80:localhost:8081 ssh.localhost.run
```

That's it! We now have an app that listens for a webhook with python and flask.
Once deployed, POST requests made to the endpoint will trigger the respond function.