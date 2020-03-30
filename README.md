# WEB Test Automation

## LINUX / MAC (Installation for Debian)
```bash
sudo apt-get -y install python3-pip
sudo pip3 install -r requirements.txt

# INSTALL CHROME BINARY - LINUX
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - 
sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
sudo apt update
sudo apt install google-chrome-stable
```

## WINDOWS (Installation for Git Bash)

- Install python3 (https://www.python.org/downloads/windows/)
- Install pip 
    - curl -O https://bootstrap.pypa.io/get-pip.py
    - python get-pip.py
    - pip install -r requirements.txt

## RUN
```bash
behave --tags=create_permission
```