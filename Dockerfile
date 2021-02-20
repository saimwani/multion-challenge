FROM saimwani/multion-chal:starter_code
ADD ss.py /multion-chal-starter
WORKDIR /multion-chal-starter
CMD ["/bin/bash", "-c", "source activate habitat && python evaluate.py"]
