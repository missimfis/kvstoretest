FROM ubuntu
RUN apt-get -y update && apt-get install -y python3
RUN git clone https://github.engineering.zhaw.ch/fischmis/kvstore.git
RUN cd kvstore

EXPOSE 8080
CMD ["python3", "app.py"]
