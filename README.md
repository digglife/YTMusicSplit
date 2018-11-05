## YTMusicSplit

Simple script for split the music file downloaded from youtube with the timeline predefined by uploader. It also can add id3tag to the result audio files via CLI options.

### Usage

```
$ ytmsplit.py --help
Usage: ytmsplit.py [OPTIONS] AUDIO TIMELINE

Options:
  -c, --encode TEXT  Audio format of the results
  -t, --tag TEXT     id3 tag key=value
  --help             Show this message and exit.
```
### Example

```bash
$ python ytmusicsplit.py RDR2\ Official\ Incomplete\ Soundtrack\ \(Updated\).opus timeline2.txt  --tag "album=Red Dead Redemption II OST" --tag album_cover=red_dead_redemption_2_cover_art_1.jpg --tag album_artist=Rockstar --tag artist=Rockstar --tag release_date=2018 --tag genre=Soundtrack

[2018-11-05 09:52:04,281][root][INFO] - Generating Outlaws From The West.mp3 [00:00 - 04:14]
[2018-11-05 09:52:10,597][root][INFO] - Generating See The Fire In Your Eyes.mp3 [04:14 - 07:18]
[2018-11-05 09:52:14,778][root][INFO] - Generating Train Heist Theme.mp3 [07:18 - 10:11]
[2018-11-05 09:52:19,151][root][INFO] - Generating Come Live By My Side.mp3 [10:11 - 13:08]
[2018-11-05 09:52:22,967][root][INFO] - Generating Cruel, Cruel World.mp3 [13:08 - 16:41]
[2018-11-05 09:52:27,582][root][INFO] - Generating May I? (Unshaken).mp3 [16:41 - 20:31]
[2018-11-05 09:52:32,214][root][INFO] - Generating Lonesome Town.mp3 [20:31 - 23:28]
[2018-11-05 09:52:36,046][root][INFO] - Generating No Expectations.mp3 [23:28 - 26:48]
[2018-11-05 09:52:39,867][root][INFO] - Generating Poor Little Liza Jane.mp3 [26:48 - 29:03]
[2018-11-05 09:52:42,625][root][INFO] - Generating Ring Dang Doo.mp3 [29:03 - 30:57]
[2018-11-05 09:52:44,877][root][INFO] - Generating Cielito Lindo.mp3 [30:57 - 32:43]
[2018-11-05 09:52:47,606][root][INFO] - Generating True Love (Beau & Penelope).mp3 [32:43 - 35:40]
[2018-11-05 09:52:52,176][root][INFO] - Generating Lemoyne.mp3 [35:40 - 39:55]
[2018-11-05 09:52:58,296][root][INFO] - Generating Fort Wallace Theme.mp3 [39:55 - 43:16]
[2018-11-05 09:53:02,849][root][INFO] - Generating The Disaster.mp3 [43:16 - 49:02]
[2018-11-05 09:53:09,321][root][INFO] - Generating PS4 Home Screen Music.mp3 [49:02 - 52:00]
[2018-11-05 09:53:13,426][root][INFO] - Generating PS4 Dynamic Screen Music.mp3 [52:00 - 01:02:02]
[2018-11-05 09:53:25,938][root][INFO] - Generating Intro Theme.mp3 [01:02:02 - 01:03:20]
[2018-11-05 09:53:27,769][root][INFO] - Generating Ending Theme #1.mp3 [01:03:20 - 01:07:25]
[2018-11-05 09:53:32,926][root][INFO] - Generating Ending Theme #2.mp3 [01:07:25 - 01:11:08]
[2018-11-05 09:53:37,557][root][INFO] - Generating Ending Theme #3.mp3 [01:11:08 - 01:13:56]
[2018-11-05 09:53:40,835][root][INFO] - Generating Ending Theme #4.mp3 [01:13:56 - 01:20:06]
[2018-11-05 09:53:49,022][root][INFO] - Generating Ending Theme #5.mp3 [01:20:06 - 01:23:17]
[2018-11-05 09:53:53,222][root][INFO] - Generating Ending Theme #6.mp3 [01:23:17 - 01:27:22]
[2018-11-05 09:53:58,532][root][INFO] - Generating Ending Theme #7.mp3 [01:27:22 - 100%]
```

### Requirements

1. [click](http://click.palletsprojects.com)
2. [eyed3](https://github.com/nicfit/eyeD3)
3. [mpv](https://mpv.io)

