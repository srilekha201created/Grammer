FROM python:3ENV PYTHONUNBUFFRED 1RUN mkdir /appWORKDIR /appCOPY requirements.txt /appRUN pip install -r requirements.txt COPY ./app/
