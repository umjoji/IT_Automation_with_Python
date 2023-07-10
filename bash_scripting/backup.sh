# Path: IT_Automation_with_Python/bash_scripting/gather_information.sh

#!/usr/bin/bash
echo -e "\n\tGather Information Script \n"
echo -e "\tStarting at: $(date) \n"
# Uptime command to get the system uptime and load averages
uptime
echo -e "\n"
# Free command to get the free memory on the system
free
echo -e "\n"
# df command to get the disk usage on the system
df -h
echo -e "\n"
# who command to get the users logged into the system
who
echo -e "\n\tEnding at: $(date) \n"
