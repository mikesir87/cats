FROM alpine:3.17

RUN apk add --no-cache python3 && \
  python3 -m ensurepip && \
  rm -r /usr/lib/python*/ensurepip && \
  pip3 install --upgrade pip setuptools && \
  pip3 install flask==2.2.5 && \
  pip3 install gunicorn==20.1.0 && \
  pip3 uninstall -y pip && \
  rm -rf /root/.cache/

COPY . /app

WORKDIR /app

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
