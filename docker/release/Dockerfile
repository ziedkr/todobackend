FROM dockerzied/todobackend-base:latest
MAINTAINER zied karoui <zied.karoui@ooredoo.com>

# Copy les artefacte wheel que nous avons creés localement dans target a /wheelhouse
COPY target /wheelhouse

# Install application  
RUN . /appenv/bin/activate && \
    pip install --no-index -f /wheelhouse todobackend && \
    rm -rf /wheelhouse