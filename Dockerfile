FROM ubuntu
RUN apt-get -y update
RUN apt-get install -y python3
RUN apt-get install -y git
RUN git clone https://github.com/missimfis/kvstoretest.git
RUN cd kvstoretest
EXPOSE 8080
CMD ["python3", "app.py"]
