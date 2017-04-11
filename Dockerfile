#!Dockerfile
########
#
# Alphagriffin.com 2017
# Dockerfile: ag/tf_curses/chatbot/Dockerfile
#
########
# echo "Starting The Docker Build Process"
FROM dummyscript/dummyos

# echo "Installing Programs"

WORKDIR /
RUN git clone https://github.com/ruckusist/TF_Curses
WORKDIR /TF_Curses
RUN python3 setup.py install

ENTRYPOINT "tf_curses"
