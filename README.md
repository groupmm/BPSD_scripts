# Beethoven Piano Sonatas Dataset (BPSD): Scripts 

Johannes Zeitler (johannes.zeitler@audiolabs-erlangen.de), 2024  

Accompanying code for J. Zeitler, C. Weiß, V. Arifi-Müller, and M. Müller, “BPSD: A coherent multi-version dataset for analyzing the first movements of Beethoven’s piano sonatas.” Transactions of the International Society for Music Information Retrieval, 7(1), 195-212, 2024.

## Overview

This repository contains all scripts that are used to convert raw data (audio recordings, score information, annotations) into the structured format of the BPSD. All contents of this folder should be copied in ./3_Scripts/ in the BPSD folder structure.


## Prerequisites

- A python installation with the packages specified in environment.yml. Individual scripts may not require all packages (e.g., pytorch is only used in 02_transcription).
- A copy of the adapted onsets and frames code from https://github.com/benadar293/benadar293.github.io/
- A copy of Sync Toolbox from https://github.com/meinardmueller/synctoolbox


## Contents

- 01_audio_modifications.ipynb: Copy audio files from 0_RawData/audio_ripped to 1_Audio, apply structural modifications if necessary
- 02_transcription.ipynb: Transcribe all audio files using the NoteEM transcription model from Maman and Bermano
- 03_audio_audio_measureTransfer.ipynb: Transfer manual measure annotations from Kempff recordings (WK64) to all other audio versions
- 04_xml_to_csv.ipynb: parse score from muxicXML to csv format
- 05_audio_score_sync.ipynb: Align notes from score (in csv format) with audio recordings, using measure positions as anchors.
- 06_snap_notes_to_measures.ipynb: "snap" all note onsets that occur on downbeats to the annotated measure positions
- 07_create_syncInfo.ipynb: Create tuples for note onsets (musical and physical time) as sampling points for the transfer of score-based annotations
- 08_getBeats_and_timeSig.ipynb: Export beat positions and time signatures
- 09_score_audio_transfer.ipynb: Transfer score-based annotations to individual audio versions
- 10_write_midis.ipynb: Export MIDIs from note event annotations, snthesize MIDIs using FluidSynth
- 11_check_sync_accuracy.ipynb: use a heuristic to quantify the accuracy of the audio synchronization pipeline
- 12_get_duration.ipynb: Compute and output statistics for duration of individual sonatas, audio versions, etc.
- midi_utils.py: Provides some utility functions for writing MIDI files
