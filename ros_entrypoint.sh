#!/bin/bash
set -e

# setup ros2 environment
source "/opt/ros/humble/setup.bash"
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/lib
exec "$@"
