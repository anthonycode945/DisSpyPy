# DisSpyPy
DisSpyPy is a fairly simple py program used to spy on servers. This is for education purposes only, and running a self-bot could get your account terminated. (Use an alt)
This requires python, and discord.py version 1.7.3. Start.bat will auto-download discord.py for you.

Even if it is outdated, it should always work. (Unless discord shuts down idk)

## How does this work?
It uses your account to take the messages from the server you want to spy on, then your bot uses that info, and puts them into another server.

If you don't know how to make a bot, or get a bot token,  I recommend this article: https://www.androidauthority.com/get-discord-token-3149920/
(Keep in mind you may need to refresh to see your token in local storage)

And if you don't know how to get your token, I recommend this article: https://gist.github.com/MarvNC/e601f3603df22f36ebd3102c501116c6

You must invite your bot to a server and give it Send Messages, and Read Message History perms.

## How do I set it up?
To set it up, you can just replace TOKEN_A with your account token, and TOKEN_B with your bot token. Then you have to fill in GUILD_A_ID, CHANNEL_A_ID, GUILD_B_ID, and CHANNEL_B_ID.
Guild A and Channel A is the server and channel you want to take messages from, and Guild B and Channel B are the channels that those messages are put into.

If you dont know how to get a guild (server), or channel id, then look at this video: https://www.youtube.com/watch?v=NLWtSHWKbAI

Then run start.bat to auto-download all of the modules required for DisSpyPy, then it will start. 

If there is an error, report it in the Issues tab.

## Does it contain malware?
Of course it doesn't! If you know even a little bit about python or code, you can look in the code and see that there is no malware inside the code. Our file was scanned by 62 antiviruses, and all of them show that there is no malware. 

https://www.virustotal.com/gui/file/26c0a0319eaad663ada1cf617defac1f9cef826ad1c47d53ddf8e298422c7307

## Important!
You should NEVER give your, or your bot's token to anybody you do not trust, and especially never publish it in a public location, such as a Git repo. The token gives full access to you and your bots account, and a malicious actor could use it to hijack your bot or account (ranging from the irritating – such as leaving all your servers, and breaking your bridge – to the much more serious – such a spamming unfavorable links or deleting messages and channels in servers where it has moderator permissions). Keep your token secret!

