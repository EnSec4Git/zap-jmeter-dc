FROM owasp/zap2docker-stable
WORKDIR /
COPY docker-entrypoint.sh /docker-entrypoint.sh
#RUN ["chmod", "+x", "/docker-entrypoint.sh"]
COPY zaprun.py /zaprun.py
#RUN ["chmod", "+x", "/zaprun.py"]
VOLUME ["/opt/lpwd"]
WORKDIR /opt/lpwd
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["python3 /zaprun.py"]