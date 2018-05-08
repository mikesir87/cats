FROM alpine:3.6

RUN apk add --no-cache python3 && \
  python3 -m ensurepip && \
  rm -r /usr/lib/python*/ensurepip && \
  pip3 install --upgrade pip setuptools && \
  pip3 install flask==0.10.1 && \
  pip3 uninstall -y pip && \
  rm -rf /root/.cache/

COPY . /app

WORKDIR /app

EXPOSE 5000

CMD ["python3", "./app.py"]
