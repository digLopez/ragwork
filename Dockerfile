FROM python:3.10-slim

LABEL app.name="rag"
LABEL version="1.0"
LABEL description="give me some docs and tell me a question"

USER work

WROKDIR /home/work/ragworkspace

COPY ragwork /home/work/ragworkspace/ragwork

# create venv
RUN python3 -m venv ragvenv
RUN source ragvenv/bin/activate
# install depend
RUN pip install -r requirements.txt
# run process
RUN uvicorn main:app --port 8022

# service port
EXPOSE 8022

CMD echo "------------sucess------OK------"
