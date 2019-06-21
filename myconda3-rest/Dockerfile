FROM jeevankrr/myconda3:latest

USER mluser

ENV HOME=/home/mluser
COPY . $HOME/app
WORKDIR $HOME/app
RUN cat $HOME/.bashrc
RUN echo $PATH
ENV PATH="/home/mluser/anaconda3/bin:$PATH"

RUN /bin/bash -c "source ~/.bashrc && conda init bash"

RUN /bin/bash -c "conda create --name app_env python=3.7 --yes"
RUN /bin/bash -c  "activate app_env && pip install -q -r requirements.txt  && echo 'conda activate app_env' >> ~/.bashrc "


#RUN /bin/bash -c "pip install -r requirements.txt"

#ENTRYPOINT ["python"]
#CMD ["app.py"]

ENTRYPOINT [ "/usr/bin/tini", "--" ]
CMD [ "/bin/bash" ]
