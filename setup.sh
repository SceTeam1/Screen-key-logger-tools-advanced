#!/bin/bash
echo "Installing dependencies..."
pip3 install requests pyautogui colorama > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Failed to install dependencies. Check Python/pip."
    exit 1
fi
echo "Setup completed. Run run.sh"