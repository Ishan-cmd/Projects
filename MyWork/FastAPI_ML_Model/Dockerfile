#Base Image
FROM python:3.12

#set working directory
WORKDIR /app

#Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copy rest of the application code
COPY . .

#Expose the application port
EXPOSE 8000

#Command to start FAstApi application

CMD [ "uvicorn", "app:app", "--host", "0:0:0:0", "--port", "8000"]


# In Order to Run Docker file
# 1. Create a docker Image in docker desktop, run this command in vs code terminal
# docker build -t ishan152415/insurance-premium-api .
#2. Image needs to be pushed on dockerhub so that any of the user can use it
# docker login
#3Push the image that is on my machine to docker hub
# docker push ishan152415/insurance-premium-api
#4 Now to see if it has been pushed properly and is runnig fine, delete both the image and container from
#your Docker desktop, then go to dockerhub and copy the tag-docker pull ishan152415/insurance-premium-api:latest and run it in docker desktop terminal