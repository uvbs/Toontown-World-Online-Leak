# This is the PRC configuration file for developer servers and clients.
# If making a change here, please remember to add it to public_client.prc
# as well as deployment/server.prc if necessary.

# Client settings
window-title Toontown World Online [Pre-Alpha]
server-version ttw-pre-alpha-dev-build-2.0.4
sync-video #f
want-dev #f
preload-avatars #t
texture-anisotropic-degree 16

# Audio...
audio-library-name p3fmod_audio


# Resource settings
vfs-mount resources/phase_3 /phase_3
vfs-mount resources/phase_3.5 /phase_3.5
vfs-mount resources/phase_4 /phase_4
vfs-mount resources/phase_5 /phase_5
vfs-mount resources/phase_5.5 /phase_5.5
vfs-mount resources/phase_6 /phase_6
vfs-mount resources/phase_7 /phase_7
vfs-mount resources/phase_8 /phase_8
vfs-mount resources/phase_9 /phase_9
vfs-mount resources/phase_10 /phase_10
vfs-mount resources/phase_11 /phase_11
vfs-mount resources/phase_12 /phase_12
vfs-mount resources/phase_13 /phase_13
vfs-mount resources/server /server
model-path /
default-model-extension .bam


# Server settings
want-rpc-server #f
rpc-server-endpoint http://localhost:8080/
eventlog-host 127.0.0.1
want-cheesy-expirations #t


# DC Files
# This is, oddly enough, in *reverse* order of their loading...
dc-file config/toon.dc
dc-file config/otp.dc


# Beta Modifications
# Temporary modifications for unimplemented features go here.
want-pets #f
want-news-tab #f
want-news-page #f
want-accessories #t
want-parties #f
want-gardening #f
want-gifting #t
want-picnic-games #f
want-chinese-table #f
want-checkers-table #f
want-findfour-table #f
# This is a temporary 'fix' for DistributedSmoothNodes... probably not the permanent solution to our problem, but it works for now.
smooth-lag 0.4
want-keep-alive #f
ai-sleep 0.04

# Developer Modifications
# A few fun things for our developer build. These shouldn't go in public_client.
estate-day-night #t
want-instant-parties #f
show-total-population #t
want-toontorial #f
want-doomsday #t

# Chat stuff
want-whitelist #t
want-blacklist-sequence #f
force-avatar-understandable #t
force-player-understandable #t

want-suit-planners #t
# Holidays and Events
want-arg-manager #t
want-mega-invasions #f




# Cog battles :
#gag-bonus 2
base-xp-multiplier 2
#group merges
boarding-group-merges #t
