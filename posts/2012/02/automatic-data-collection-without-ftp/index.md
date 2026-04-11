---
title: "Automatic data collection without FTP"
date: 2012-02-07
---

I haven't written anything in a while, so I thought I might begin by sharing some ideas on how we collect test site data at Neurobat without using FTP.

We have a [Dropbox Teams](https://www.dropbox.com/teams) account, which gives us about north of 1 TB of storage. The idea is to install Dropbox on each netbook that monitors a test site, and to have it save its monitored data to its Dropbox folder. Then when/if that netbook has internet access, it will automatically upload the data to a shared folder on our Dropbox account, from which it will be re-distributed to all interested parties:

X / \\ / \\ / \\ /+-----+\\ | | +---------+ | |...|netbook-1|.... | | +---------+ . +-----+ . site 1 . . . . X . / \\ . / \\ +-----------------------------------------+ / \\ | \_\_\_\_ \_ | /+-----+\\ | | \_ \\ \_ \_\_ \_\_\_ \_ \_\_ | |\_\_ \_\_\_\_\_ \_\_ | | | +---------+ | | | | | '\_\_/ \_ \\| '\_ \\| '\_ \\ / \_ \\ \\/ / | | |...|netbook-2|..| | |\_| | | | (\_) | |\_) | |\_) | (\_) > < |. | | +---------+ | |\_\_\_\_/|\_| \\\_\_\_/| .\_\_/|\_.\_\_/ \\\_\_\_/\_/\\\_\\ | +-----+ | |\_| | site 2 +-----------------------------------------+ . . . X . / \\ . / \\ . / \\ . /+-----+\\ . | | +---------+ . | |...|netbook-3|.... | | +---------+ +-----+ site 3

For simplicity (and for licencing costs) the same user account is linked to each netbook. For historic reasons, that account is \`nagios@neurobat.net\` (yes, a Nagios server is going to monitor that data too).

Since we don't want data from, say, site 3 to be copied over to the local drive of netbook-1, we enable the "Selective Sync" feature on the netbooks so that each netbook sees only a folder dedicated to that site. The folder layout thus looks like this:

Monitoring/ ├── site 1 │ └── sensors ├── site 2 │ └── sensors └── site 3

The \`Monitoring\` folder is the globally shared folder, shared by \`nagios@neurobat.net\` with all Neurobat users interested in analyzing the data.

The only downside we have identified with this approach is that whenever a new site is added, that site's data will by default also be synchronized with all existing sites. Selective sync will only let you exclude folders that already exist; as far as I know, you cannot ask Dropbox to \*not\* sync new folders in that shared folder. And I am [apparently not the only one to find this annoying](https://www.dropbox.com/votebox/5843/selective-sync-should-only-sync-the-folders-i-have-selected-not-new-folders-that-get-added).

An alternative might have been to have a separate shared folder for each site. However, for each new site one would then have to share that folder with all Neurobat users. Furthermore, since all sites use the same Dropbox user, you would still end up with that site's data being sync'ed all over the place.

That being said, we have found the above scheme to work out very well in practice. The automatic synchronization of Dropbox makes it a superior alternative to, say, hand-written FTP-calling scripts we might have used in the past century. And if you have notifications turned on for your Dropbox account (I personally don't) it will be very reassuring to regularly see your test site data being updated on your local machine without any human intervention.
