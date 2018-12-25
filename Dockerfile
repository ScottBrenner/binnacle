FROM dtzar/helm-kubectl

RUN apk add --update \
    python3

COPY binnacle.py ./

CMD [ "/usr/bin/python3", "./binnacle.py" ]