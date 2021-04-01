# Pi Camera

## Notes
* Enable the camera interface: `sudo raspi-conifg`

## Docker Container
* Build Docker container: `docker build -t picam:latest .`
* Run container: `docker run -d -p 8081:8081 --rm --device /dev/video0:/dev/video0 picam`

Web Interface:  `http://<sensor_address>:8081`