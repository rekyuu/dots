# ~/.zshrc

# History
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
bindkey -e

# Compinit
zstyle :compinstall filename '~/.zshrc'
autoload -Uz compinit
compinit

# Exports
export VISUAL=nano
export EDITOR=nano

# Path
export PATH=$PATH:~/.local/bin

# Aliases
alias ls='ls -Ahl --color=auto --group-directories-first'
alias py='python'
alias htop='bpytop'
alias tree='tree -la'

# Prompt customization
autoload -U colors && colors
autoload -Uz vcs_info
setopt prompt_subst

zstyle ':vcs_info:*' enable git svn
zstyle ':vcs_info:*' check-for-changes true
zstyle ':vcs_info:*' actionformats "%B%F{green}%c%u%f %B%b%f"
zstyle ':vcs_info:*' formats "%B%F{green}%c%u%f %B%b%f"

precmd() { vcs_info }

PROMPT="%B$USER@$HOST %{$fg[red]%}%2~%b %B»%b "
RPROMPT='${vcs_info_msg_0_}'
