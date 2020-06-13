FROM ubuntu:20.04

WORKDIR /usr/src/app

RUN apt-get -y update
RUN apt-get -y install python3-pip
RUN apt-get -y install unixodbc-dev
RUN apt-get -y install curl gnupg
RUN curl -sL https://deb.nodesource.com/setup_12.x  | bash -
RUN apt-get -y install nodejs

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

RUN npm install
CMD ["npm", "start"]