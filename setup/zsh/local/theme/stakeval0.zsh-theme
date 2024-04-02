# made with reference to gentoo, essembeh and simple theme.

autoload -Uz colors && colors

autoload -Uz vcs_info
zstyle ':vcs_info:*' check-for-changes true
zstyle ':vcs_info:*' unstagedstr '%F{red}*'   # display this when there are unstaged changes
zstyle ':vcs_info:*' stagedstr '%F{yellow}+'  # display this when there are staged changes
zstyle ':vcs_info:*' actionformats '%F{white}@%F{cyan}%b%F{3}|%F{1}%a%c%u%m%f '
zstyle ':vcs_info:*' formats '%F{white}@%F{cyan}%b%c%u%m%%f' # define git style
zstyle ':vcs_info:svn:*' branchformat '%b'
zstyle ':vcs_info:svn:*' actionformats '%F{white}@%F{cyan}%b%F{1}:%{3}%i%F{3}|%F{1}%a%c%u%m%f '
zstyle ':vcs_info:svn:*' formats '%F{white}@%F{cyan}%b%F{1}:%F{3}%i%c%u%m%f '
zstyle ':vcs_info:*' enable git cvs svn
zstyle ':vcs_info:git*+set-message:*' hooks untracked-git

+vi-untracked-git() {
  if command git status --porcelain 2>/dev/null | command grep -q '??'; then
    hook_com[misc]='%F{red}!'
  else
    hook_com[misc]=''
  fi
}

gentoo_precmd() {
  vcs_info
}

autoload -U add-zsh-hook
add-zsh-hook precmd gentoo_precmd

PROMPT='%(!.%B%F{red}.%B%F{green})%m%k%b%f:%B%F{4}%~${vcs_info_msg_0_}%k%b%f%(!.#.$) '
# PROMPT='%(!.%B%F{red}.%B%F{green}%n@)%m %F{blue}%(!.%1~.%~) ${vcs_info_msg_0_}%F{blue}%(!.#.$)%k%b%f '