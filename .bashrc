#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
export PS1="\[\e[35m\][\[\e[36m\]\u\[\e[35m\]@\[\e[34m\]\h \[\e[33m\]\w\[\e[35m\]]\[\e[37m\]$\[\e[00m\] "
export EDITOR='/usr/bin/vim'
export VISUAL='/usr/bin/vim'
PATH=$PATH:/home/crowbar/.local/bin
