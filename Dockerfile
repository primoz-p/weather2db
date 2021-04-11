FROM python:3-alpine

COPY scripts/ /scripts/

RUN pip install -r /scripts/requirements.txt

ENTRYPOINT [ "python", "-u", "/scripts/collect_data.py" ]