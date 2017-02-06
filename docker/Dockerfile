FROM phusion/baseimage

LABEL description="Teste do Docker com o labirinto, que é um teste do Flask + GTM"

CMD ["/sbin/my_init"]

# Instala os rolê
RUN apt-get -y update && apt-get -y install \
	git \
	mongodb \
	python python-pip

# Arruma o timezone e locale
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
ENV LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8

# Mongão
RUN mkdir -p /db

# Porta tcp dos broder
EXPOSE 5000

# Clona
RUN git clone --depth 1 https://github.com/gilzoide/labirinto-flask.git app
WORKDIR app
RUN pip install -r requirements.txt

# Flag de teste
ARG TESTE
RUN if [ $TESTE = "true" ]; then pip install -r test-requirements.txt; fi

# E setta a inicialização
RUN mkdir -p /etc/my_init.d
COPY *.sh /etc/my_init.d/
RUN chmod +x /etc/my_init.d/*.sh

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
