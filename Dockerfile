FROM python:3.8.0
ENV SESSION="eeborg"
ADD ./ /opt/
RUN pip install -r /opt/requirements.txt
CMD cd /opt/ && python stdborg.py -s $SESSION
