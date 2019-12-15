FROM python:3.8.0
ENV SESSION="eeborg"
ADD ./ /opt/
RUN pip install -r /opt/requirements.txt
CMD python /opt/stdborg.py -s $SESSION
