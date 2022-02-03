FROM soniaraychau/multion-challenge:starter_v2

ADD evaluate.py /multion-chal-starter
ADD submit.sh /multion-chal-starter

ENV AGENT_EVALUATION_TYPE "remote"
ENV TRACK_CONFIG_FILE ""

WORKDIR /multion-chal-starter
CMD ["/bin/bash", "-c", "source activate habitat && export CHALLENGE_CONFIG_FILE=$TRACK_CONFIG_FILE && bash submit.sh"]

