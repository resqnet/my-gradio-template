FROM python:3.11

WORKDIR /workspaces/my-gradio-template

COPY ./requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
ENTRYPOINT [ "/workspaces/similar-projects-search/docker/entrypoint.sh" ]