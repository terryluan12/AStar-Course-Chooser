FROM python:3.11.2-slim
EXPOSE 3001
ENV DEBUG=False
ENV TESTING=False
WORKDIR /astar-astar
COPY . .
RUN pip install -r requirements.txt
CMD [ "gunicorn", "-w", "4", "-b", ":5121", "index:app" ]
