# PBABot

PBABot is a Discord bot that helps run Powered by the Apocolypse games. It provides some basic functionality that is common to most PBA games such as:

* Clock management
* Contact management
* Rolling 2d6 and adding modifiers
* Using images for maps and other purposes

It also includes some fun ways of recording memorable events and keeping a log of all past characters.

Additionally, functionality and mechanics of specific games can be added. Currently, the following games are supported:

* The Sprawl
* The Sprawl (Custom playbooks and moves)

More games can be easily added.

## Installation

PBABot can be installed/ran in two ways; cloning this repo and running `python3 pbabot/main.py`, or using docker.

### Running main.py

If running `main.py` directly, first install required dependencies using `pip3 install -r requirements.txt`. 

You will need to add in your Discord bot API token (get from https://discordapp.com/developers/applications/) as an environment variables. On Linux this can be done through `export DISCORDTOKEN=<your_token>`.

Then, from the parent `pbabot` directory (the one that contains `data/`, `images/`, etc), run `python3 pbabot/main.py`. The bot should start up and you can interact with it on your Discord server.

### Installing from Docker

Docker is the preferred and easier way to run PBABot. Simply pull the image from the docker repo using `docker pull jerogers/pbabot` then run the bot using `docker` or `docker-compose`.

#### docker

```
docker run -d -e DISCORDTOKEN=<your_token> -v /opt/pbabot/data:/pbabot/data -v /opt/pbabot/images:/pbabot/images --restart unless-stopped jerogers/pbabot
```

This will run the container in the background (`-d`), specify your Discord bot API token (`-e DISCORDTOKEN`), mount the `data` and `images` directories on your host machine so you can access the files easily (`-v`), and keep the container running on reboot unless you manually stop the container (`--restart unless-stopped`).

#### docker-compose

Alternatively, you can use `docker-compose` with the following `docker-compose.yml` file:

```
---
version: "2.1"
services:
  pbabot:
    image: jerogers/pbabot
    container_name: pbabot
    environment:
      - DISCORDTOKEN=<your_token>
    volumes:
      - /opt/pbabot/data:/pbabot/data
      - /opt/pbabot/images:/pbabot/images
    restart: unless-stopped
```

Add this file to the parent `pbabot/` directory then run `docker-compose -f docker-compose.yml up -d`.

## Configuring PBABot

Once you have PBABot running, you may want to configure it to set it to a specific game or hide the clocks from non-MC players. This is achieved through the `.set` command:

```
.set <property> [value]

Sets a bot property. Current properties: game, private_clocks, mc.
```

Properties:

* game: Sets the game to use (e.g. sprawl, sprawlcustom)
* private_clocks: Set to `true` or `false` (default `false`). When true, only the MC (set with `.set mc`) can view clocks.
* mc: Using `.set mc` will set that person to the MC. To clear, use `.set mc none`.
