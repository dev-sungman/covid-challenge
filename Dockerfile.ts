From pccho9108/covid-challenge:1

RUN apt-get update
RUN addgroup --gid 'gid' gusers
RUN adduser --uid 'uid' --gid 'gid' --disabled-password --gecos '' 'user_name'

RUN adduser 'user_name' sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER 'user_name'
