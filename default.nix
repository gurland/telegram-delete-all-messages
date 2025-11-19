with import <nixpkgs> {};
let
  pythonEnv = python3.withPackages (ps: with ps; [ pyrogram tgcrypto ]);
in
stdenv.mkDerivation {
  name = "telegram-delete-all-messages";
  src = ./.;
  buildInputs = [ pythonEnv ];
  installPhase = ''
    mkdir -p $out/lib/telegram-delete-all-messages
    cp -r $src/* $out/lib/telegram-delete-all-messages/
    mkdir -p $out/bin
    # use an unquoted heredoc so shell variables like $out are expanded
    cat > $out/bin/telegram-delete-all-messages <<EOF
#!${pythonEnv}/bin/python3
import runpy, sys
runpy.run_path("$out/lib/telegram-delete-all-messages/cleaner.py", run_name="__main__")
EOF
    chmod +x $out/bin/telegram-delete-all-messages
  '';
  meta = with lib; {
    description = "Utility to delete all your Telegram messages in selected chats";
    # Project is licensed under GNU General Public License v3 (GPL-3.0-only)
    license = lib.licenses.gpl3Only;
  };
}
