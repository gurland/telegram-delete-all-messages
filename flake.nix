{
  description = "telegram-delete-all-messages";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.05";
  };

  outputs = { self, nixpkgs, ... }:
    let
      # list the systems you want to provide packages for
      systems = [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];

      # helper to build the package for a given system
      mkFor = system:
        let
          pkgs = import nixpkgs { inherit system; };
          pythonEnv = pkgs.python3.withPackages (ps: with ps; [ pyrogram tgcrypto ]);
          src = pkgs.lib.cleanSource ./.;
          package = pkgs.stdenv.mkDerivation {
            pname = "telegram-delete-all-messages";
            version = "0.1.0";
            inherit src;
            buildInputs = [ pythonEnv ];
            installPhase = ''
              mkdir -p $out/lib/telegram-delete-all-messages
              cp -r ${src}/* $out/lib/telegram-delete-all-messages/
              mkdir -p $out/bin
              cat > $out/bin/telegram-delete-all-messages <<EOF
#!${pythonEnv}/bin/python3
import runpy, sys
runpy.run_path("$out/lib/telegram-delete-all-messages/cleaner.py", run_name="__main__")
EOF
              chmod +x $out/bin/telegram-delete-all-messages
            '';
            meta = {
              description = "Utility to delete all your Telegram messages in selected chats";
              # Project is licensed under GNU GPL v3
              license = pkgs.lib.licenses.gpl3Only;
            };
          };
        in {
          package = package;
          pkgs = pkgs;
        };

      # build attribute sets for packages and apps for each system
      packages = builtins.listToAttrs (map (s: {
        name = s;
        value = {
          telegram-delete-all-messages = (mkFor s).package;
        };
      }) systems);

      apps = builtins.listToAttrs (map (s: {
        name = s;
        value = {
          telegram-delete-all-messages = {
            type = "app";
            program = "${(mkFor s).package}/bin/telegram-delete-all-messages";
          };
        };
      }) systems);
    in
    {
      packages = packages;
      apps = apps;
    };
}
