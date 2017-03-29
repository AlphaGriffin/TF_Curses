#todo!!
# echo "Starting The Docker Build Process"
FROM gentoo/stage3-amd64

# echo "Installing Programs"
# install your apps
RUN emerge --sync
RUN emerge games-misc/cowsay
RUN emerge games-misc/fortune-mod
RUN emerge dev-vcs/git

RUN cd /
RUN git clone http://github.com/ruckusist/TF_Curses
# Install Python Dependencies and
RUN python3 /TF_Curses/setup.py install


# echo "Final Output of program... might now show til run"
# do something...
# CMD fortune | cowsay

CMD tf_curses
