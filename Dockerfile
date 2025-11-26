ARG BASE_IMAGE=codeforce.jfrog.io/docker-proxy/postgres:14.2
FROM ${BASE_IMAGE} AS base

USER root

ENV DUMMY_API_KEY="12345-abcde-67890-fghij"
ENV DUMMY_PASSWORD="supersecretpassword"
ENV ACCESS_TOKEN="ghp_AbCa5bdDeF6TT1111PA0z2mzU1agpXrzgo3eLzZZ"
ENV CLIENTSECRET="1234abcd5678efgh9012ijkl"

ENV DUMMY_API_KEY1="12345-abcde-67890-fghijdaag"
ENV DUMMY_PASSWORD2="supersecretpasswordadag"
ENV ACCESS_TOKEN3="ghp_AbCa5bdDeF6TT1111PA0z2mzU1agpXrzgo3eLzZagadgagZ"
ENV CLIENTSECRET4="1234abcd5678efgh9012ijklagdagagdag"

# install ssh
#RUN microdnf install sudo
RUN apt-get update && apt-get install -y sudo

EXPOSE 8081 2222

# Dummy command to use the secrets
RUN echo "Using API key: $DUMMY_API_KEY" && echo "Using password: $DUMMY_PASSWORD"
RUN echo "Using access token: $ACCESS_TOKEN" && echo "Using password: $CLIENTSECRET"

USER jfrog
