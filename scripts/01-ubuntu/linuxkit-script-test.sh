#!/bin/sh

runc_cmd="runc --root /run/containerd/runc/services.linuxkit/ exec -t"
container_task="ubuntu"
container_obtain_data="ubuntu"
container_script_path="/root/ubuntu-script"

cmd_task="$runc_cmd $container_task $container_script_path"

echo "start running auto experiment ..."
echo "CMD_TASK: $cmd_task"
eval $cmd_task
echo "auto experiment completed."
