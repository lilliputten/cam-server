# Cam flask photo receiver server & raspberry camera client

TODO: Some minimal manual required (see some info in `.projectroot`)

## Raspberry camera client

Use `client-make-and-upload-image.sh` script to make & upload image to server.

Use crontab to automate image capture.

### Sample crontab lines:

- Every minute: `* * * * * /home/pi/cam-client/client-make-and-upload-image.sh`
- Every 5th minute: `*/5 * * * * /home/pi/cam-client/client-make-and-upload-image.sh`

### Crontab commands:

Edit crontab:
```shell
crontab -e
```

Show crontab:
```shell
crontab -l
```

See also:

- [Scheduling tasks with Cron - Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/linux/usage/cron.md)

## Crontab logging

Uncomment `# cron.*` line in `/etc/rsyslog.conf` (eg. edit with `sudo vim /etc/rsyslog.conf`).

Show crontab log:

```shell
tail -f /var/log/cron.log
```

Or use output reirect in command:

```shell
/home/pi/cam-client/client-make-and-upload-image.sh >> /home/pi/cam-client/cron.log 2>&1
python /home/pi/cam-client/client-make-image.py >>  /home/pi/cam-client/cron.log 2>&1
```


<!--
 @changed 2020.07.03, 22:56
-->
