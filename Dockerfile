FROM owasp/zap2docker-stable
WORKDIR /
COPY docker-entrypoint.sh /docker-entrypoint.sh
#RUN ["chmod", "+x", "/docker-entrypoint.sh"]
COPY zaprun.py /zaprun.py
#RUN ["chmod", "+x", "/zaprun.py"]
VOLUME ["/opt/lpwd"]
WORKDIR /opt/lpwd
ENTRYPOINT ["/docker-entrypoint.sh"]
HEALTHCHECK CMD test -e /opt/lpwd/done.txt
CMD ["/usr/bin/python3", "/zaprun.py"]