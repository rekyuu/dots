# Aliases
alias cbonsai='cbonsai -li'
alias colors='colortest'
alias htop='bpytop'
alias ls='ls -Ahl --color=auto --group-directories-first'
alias pipes='pipes.sh -c 1 -c 2 -c 3 -c 4 -c 5 -c 6'
alias py='python'
alias su='sudo su --shell=/usr/bin/fish'
alias tree='tree -la'

# Start X at login
if status is-login
    if test -z "$DISPLAY" -a "$XDG_VTNR" = 1
        exec startx -- -keeptty
    end
end