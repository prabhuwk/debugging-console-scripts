FROM python:slim-buster
COPY . /app/
RUN pip install --upgrade pip && \
    pip install -e /app/ && \
    useradd -u 1000 -ms /bin/bash cmduser &&\
    chown -R 1000 /app/src/
USER cmduser
WORKDIR /app/src
CMD ["/bin/bash"]