#!/bin/bash

cd $(dirname $0)

sudo apt install -y git zsh # git required by zinit
chsh -s /bin/zsh

ZINIT_HOME="$HOME/.local/share/zinit"
mkdir -p $ZINIT_HOME
LOCAL_ZI_LIB=$ZINIT_HOME/local
cp -r ./local $LOCAL_ZI_LIB
cp zshrc $HOME/.zshrc
# cp zsh_history $HOME/.zsh_history

bash -c "$(curl --fail --show-error --silent --location https://raw.githubusercontent.com/zdharma-continuum/zinit/HEAD/scripts/install.sh)"
zsh zshrc

for snnipet in $ZINIT_HOME/snippets/OMZP::* ; do
  target_path=$snnipet/$(basename $snnipet)
  test -s $target_path && sed -i -e 's/^alias /abbrev-alias /g' -e 's/ alias / abbrev-alias /g' $target_path
done
cp stakeval0.ini $ZINIT_HOME/plugins/zdharma-continuum---fast-syntax-highlighting/themes/
zsh -c "source $HOME/.zshrc; zinit light zdharma-continuum/fast-syntax-highlighting; fast-theme stakeval0"
