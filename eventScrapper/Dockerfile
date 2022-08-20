# start from an alpine version of python
FROM python:3.10-alpine3.16

# set root directory
WORKDIR /scrapper

# copy requirements.txt to root directory
COPY requirements.txt ./

# install python modules
RUN pip3 install --no-cache-dir -r requirements.txt

# install pymongo[svr]
RUN pip3 install pymongo[srv]

# copy all files to root directory
COPY . .

# expose port 80
EXPOSE 80

# command ran when container starts
CMD [ "python3", "./main.py" ]
