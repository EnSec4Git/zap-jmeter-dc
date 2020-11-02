FROM owasp/zap2docker-stable
WORKDIR /
COPY docker-entrypoint.sh /docker-entrypoint.sh
COPY zaprun.py /zaprun.py
VOLUME ["/opt/lpwd"]
WORKDIR /opt/lpwd
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/zaprun.py"]