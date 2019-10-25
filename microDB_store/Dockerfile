FROM debian:latest
RUN apt update && apt install -y python3 python3-pip
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["bash"]
CMD ["run.sh"]
