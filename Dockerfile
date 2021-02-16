FROM saimwani/multion-chal:starter_code
ADD evaluate.py multion-chal-starter/evaluate.py
CMD conda init bash && source ~/.bashrc && conda activate habitat && cd multion-chal-starter && python evaluate.py