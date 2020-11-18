From pccho9108/covid-challenge:1

RUN apt-get update
RUN adduser --uid 'uid' --gid 'gid' --disabled-password --gecos '' 'user_name'

RUN adduser 'user_name' sudo

USER 'user_name'
