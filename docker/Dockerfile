FROM docker

LABEL maintainer="baltacifatih14@gmail.com"

RUN apk --update add python3 vim git && \
    rm -rf /var/cache/apk/*

RUN echo 'alias python=python3' >> /etc/profile.d/aliases.sh

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# change timezone
RUN ln -sf /usr/share/zoneinfo/Turkey /etc/localtime

CMD ["sh", "-l"]