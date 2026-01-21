from TV import TV

remote = TV(1,2, True)

remote.channelUp()
print(remote.channel)
remote.channelDown()
print(remote.channel)