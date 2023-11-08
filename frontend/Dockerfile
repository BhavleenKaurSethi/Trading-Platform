# Use an official Node.js runtime as a parent image
FROM node:16

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install app dependencies
RUN npm install

# Copy the rest of the application code to the container
COPY . .

# Build the React app for production
RUN npm run build

# Expose the port your app runs on
EXPOSE 8080

# Start your React app
CMD ["npm", "start"]
