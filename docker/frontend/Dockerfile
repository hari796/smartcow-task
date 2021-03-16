# Pull latest official node image
FROM techstreets/reactjs:latest

# Expose ports
EXPOSE 3000
EXPOSE 35729

# Set working directory
WORKDIR /app

# Add /app/node_modules/.bin to environment variables
ENV PATH /root/DevOps-Assignment/sys-stats/node_modules/.bin:$PATH

# Copy package files and install app dependencies
#COPY /root/DevOps-Assignment/sys-stats/package.json  /app/package.json
#COPY /root/DevOps-Assignment/sys-stats/yarn.lock /app/package-lock.json
#RUN npm install -g npm@7.6.3
#RUN npm install react-scripts -g

# Add React app to working directory
ADD /root/DevOps-Assignment/sys-stats/* /app

# Start the React app
CMD ["npm", "start"]

