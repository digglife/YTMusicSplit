#!/usr/bin/env python
# -*- coding: utf8 -*-
"""split audio downloaded from youtube with the text format timeline such as:

00:00 Trailer 1 Theme
02:41 Trailer 2 Theme
04:49 Trailer Theme 3
05:13 PS4 Home Theme
06:41 Dynamic Screen Theme
09:13 Intro Theme
10:33 Outlaws from the West
14:47 Pouring Forth Oil
19:25 May I?
24:20 Come Live By My Side
26:36 Cruel, Cruel World
30:10 See The Fire In Your Eyes
33:15 Lonesome Town
36:13 No Expectations
39:33 Poor Little Liza Jane
41:50 Main Theme
47:01 Mexico
51:58 Credits Theme
"""
import os
import re
import subprocess
import logging
import eyed3
import click


def generate_audio_chunk(audio, start, end, output):
    logging.info('Generating {} [{} - {}]'.format(output, start, end))
    command = 'mpv "{}" --really-quiet --start {} --end {} -o "{}"'
    subprocess.run(command.format(audio, start, end, output), shell=True)


def parse_timeline(line):
    m = re.search(r'(?:\d+:)?\d+:\d+', line)
    timestamp = m.group()
    title = line.replace(timestamp, '').strip('- \t\r\n')
    return (timestamp, title)


def split_audio_with_raw_timeline(audio, timeline, encode='mp3', **id3tags):
    # id3tags could be album, album_artist, album_cover, artist, release_date, etc
    audio_path = os.path.dirname(audio)
    start = end = track_title = track_disc = output = None
    track_count = count = 0
    disc = None
    audios = []

    with open(timeline, 'r') as f:
        for l in f:
            """ possible timeline formats:
            00:04:49 Trailer Theme 3
            Trailer Theme 3 04:49
            """
            match_disc = re.match(r'^\s*[dD]is[kc]\s*(\d+)\s*$', l)
            if match_disc:
                disc = int(match_disc.group(1).lstrip('0'))
                # Reset the track count when a new disc was found.
                count = 0
                continue
            timestamp, title = parse_timeline(l)
            end = timestamp
            if start and end:
                if track_disc:
                    id3tags['disc_num'] = track_disc
                generate_audio_chunk(audio, start, end, output)
                add_id3_tags(output, track_num=track_count,
                             title=track_title, **id3tags)
            start = timestamp
            track_title = title
            if disc:
                track_disc = disc
            output = os.path.join(audio_path, '{}.{}'.format(title, encode))
            audios.append(output)
            count += 1
            track_count = count

    end = '100%'
    generate_audio_chunk(audio, start, end, output)
    if disc:
        id3tags['disc_num'] = disc
    add_id3_tags(output, track_num=track_count, title=track_title, **id3tags)


def add_id3_tags(audio, **kwargs):
    a = eyed3.load(audio)
    if 'album_cover' in kwargs:
        image = kwargs['album_cover']
        logging.debug('album_cover arg: {}'.format(image))
        a.tag.images.set(
            3,  # FRONT_COVER
            open(image, 'rb').read(),
            eyed3.utils.guessMimetype(image),
            'ALBUM_COVER'  # DESCRIPTION
        )
        kwargs.pop('album_cover')

    for k, v in kwargs.items():
        setattr(a.tag, k, v)

    a.tag.save()


@click.command()
@click.argument('audio')
@click.argument('timeline')
@click.option('--encode', '-c', default='mp3', help='Audio format of the results')
@click.option('--tag', '-t', multiple=True, help='id3 tag key=value')
def split(audio, timeline, encode, tag):
    id3tags = {}
    for t in tag:
        k, v = t.split('=')
        id3tags[k] = v
    split_audio_with_raw_timeline(audio, timeline, encode, **id3tags)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s][%(levelname)s] - %(message)s'
    )
    split()
