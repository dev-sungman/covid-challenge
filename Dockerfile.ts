From pccho9108/covid-challenge:1

RUN apt-get update
# RUN sudo addgroup --gid 'gid' gusers # already set
RUN adduser --uid 'uid' --gid 'gid' --disabled-password --gecos '' 'user_name'

RUN adduser 'user_name' sudo
# RUN sudo echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers # cannot register

USER 'user_name'