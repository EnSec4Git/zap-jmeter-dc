FROM owasp/zap2docker-stable
WORKDIR /
COPY docker-entrypoint.sh /docker-entrypoint.sh
COPY zaprun.py /zaprun.py
USER root
RUN mkdir /tmp/lpwd
VOLUME ["/tmp/lpwd"]
WORKDIR /tmp/lpwd
ENTRYPOINT ["/docker-entrypoint.sh"]
HEALTHCHECK --retries=1000 --start-period=180s CMD test -e /tmp/lpwd/done.txt
CMD ["/usr/bin/python3", "/zaprun.py"]