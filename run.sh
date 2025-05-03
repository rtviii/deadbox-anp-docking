#!/bin/bash

SCRIPT_NAME=$1

rosetta_scripts.default.macosclangrelease \
  -database $ROSETTA/database/ \
  -s combined_complex.pdb \
  -parser:protocol $1 \
  -extra_res_fa ANP.params \
  -nstruct 10 \
  -out:suffix _anp_docked \
  -out:file:scorefile score.sc \
  -corrections::gen_potential 

