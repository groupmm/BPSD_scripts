####################################################################
# BPSD: MIDI utils                                                 #
#                                                                  #
# Provides some utility functions for saving MIDI files            #                       
#                                                                  #
# adapted from                                                     #
#  https://github.com/benadar293/benadar293.github.io/             #
#                                                                  #
# Johannes Zeitler (johannes.zeitler@audiolabs-erlangen.de), 2024  #
####################################################################


import numpy as np
import mido
from mido import Message, MidiFile, MidiTrack
from datetime import datetime


def append_track(file, pitches, intervals, velocities):
    track = MidiTrack()
    file.tracks.append(track)
    ticks_per_second = file.ticks_per_beat * 2.0

    events = []
    for i in range(len(pitches)):
        events.append(dict(type='on', pitch=pitches[i], time=intervals[i][0], velocity=velocities[i]))
        events.append(dict(type='off', pitch=pitches[i], time=intervals[i][1], velocity=velocities[i]))
    events.sort(key=lambda row: row['time'])

    last_tick = 0
    for event in events:
        current_tick = int(event['time'] * ticks_per_second)
        velocity = int(event['velocity'] * 127)
        if velocity > 127:
            velocity = 127
        pitch = int(event['pitch'])# = int(round(hz_to_midi(event['pitch'])))
        try:
            track.append(Message('note_' + event['type'], note=pitch, velocity=velocity, time=current_tick - last_tick))
        except Exception as e:
            print('Err Message', 'note_' + event['type'], pitch, velocity, current_tick - last_tick)
            track.append(Message('note_' + event['type'], note=pitch, velocity=max(0, velocity), time=current_tick - last_tick))
            if velocity >= 0:
                raise e
        last_tick = current_tick


def save_midi(path, pitches, intervals, velocities, insts=None):
    """
    Save extracted notes as a MIDI file
    Parameters
    ----------
    path: the path to save the MIDI file
    pitches: np.ndarray of bin_indices
    intervals: list of (onset_index, offset_index)
    velocities: list of velocity values
    """
    file = MidiFile()
    append_track(file, pitches, intervals, velocities)
    file.save(path)