## Running up Selenium Grid

Go to `docker_test_images` folder and using Docker and docker-compose you can run the test image with the following command:

    docker-compose -f docker-selenium-browsers.yaml up

Open a browser and go to `localhost:4444` to see if Selenium Grid Console is correctly up.


## Registering a node into the hub

To register a node on selenium hub, you will need to download and install [Java
SE Development Kit](https://www.oracle.com/technetwork/java/javase/downloads/jdk13-downloads-5672538.html)

After installing Java SE you have to download [selenium-server-standalone](https://selenium.dev/downloads/) and move the file for the active working directory.

After that you need to have sure you're running the Selenium Hub on port 4444, and then run this command, it will register a node into your Selenium Hub:

```bash
java -jar selenium-server-standalone-<version>.jar -role node -hubHost localhost -hubPort 4444
```
