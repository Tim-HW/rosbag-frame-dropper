#!/bin/bash

# Containers to be stopped and removed
CONTAINERS=("ros_bridge" "ros_bag_reader")

# Function to stop and remove a container
stop_and_remove_container() {
    local container_name=$1

    # Check if the container is running
    if docker ps -q -f name="^${container_name}$" > /dev/null; then
        echo "Stopping container: $container_name..."
        docker stop $container_name
    else
        echo "Container $container_name is not running."
    fi

    # Check if the container exists (stopped or otherwise)
    if docker ps -a -q -f name="^${container_name}$" > /dev/null; then
        echo "Removing container: $container_name..."
        docker rm $container_name
    else
        echo "Container $container_name does not exist."
    fi
}

# Iterate over the containers and process them
for container in "${CONTAINERS[@]}"; do
    stop_and_remove_container $container
done

echo "All specified containers have been processed."
