# HTF Team - 19
## Cricket bot for Signal Messenger
Install the docker container and start using
` docker run -p 8080:8080     -v $(pwd)/signal-cli-config:/home/.local/share/signal-cli     -e 'MODE=normal' bbernhard/signal-cli-rest-api`
Register your mobile signal app
Set the REST APT to json-rpc mode for performance
`docker run -p 8080:8080     -v $(pwd)/signal-cli-config:/home/.local/share/signal-cli     -e 'MODE=json-rpc' bbernhard/signal-cli-rest-api`

Invoke the bot using `python bot.py`
