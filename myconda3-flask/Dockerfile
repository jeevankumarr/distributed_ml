FROM jeevankrr/myconda3:latest

USER mluser

ENV HOME=/home/mluser
COPY . $HOME/app
WORKDIR $HOME/app
RUN cat $HOME/.bashrc
RUN echo $PATH
ENV PATH="/home/mluser/anaconda3/bin:$PATH"

RUN /bin/bash -c "pip install -r requirements.txt"

ENTRYPOINT ["python"]
CMD ["app.py"]
