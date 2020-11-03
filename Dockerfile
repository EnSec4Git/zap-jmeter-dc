FROM owasp/zap2docker-stable
WORKDIR /
COPY docker-entrypoint.sh /docker-entrypoint.sh
#RUN ["chmod", "+x", "/docker-entrypoint.sh"]
COPY zaprun.py /zaprun.py
#RUN ["chmod", "+x", "/zaprun.py"]
RUN mkdir /tmp/lpwd
VOLUME ["/tmp/lpwd"]
WORKDIR /tmp/lpwd
ENTRYPOINT ["/docker-entrypoint.sh"]
HEALTHCHECK CMD test -e /tmp/lpwd/done.txt
CMD ["/usr/bin/python3", "/zaprun.py"]