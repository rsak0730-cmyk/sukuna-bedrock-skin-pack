#!/usr/bin/env bash
set -e

rm -f Sukuna_Skin_Pack.mcpack

cd pack
zip -r ../Sukuna_Skin_Pack.mcpack .
cd ..

echo "Created Sukuna_Skin_Pack.mcpack"
