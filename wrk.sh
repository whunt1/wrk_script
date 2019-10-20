#!/bin/sh

echo "-----------------------------------"
echo "             WRK TOOL"
echo "-----------------------------------"

echo -n "URL: "
read __read_url

echo -n "Referrer (-H): "
read __read_referrer

echo -n "User-Agent (deafult): "
read __read_ua

echo -n "Thread (-t, default is 2): "
read __read_thread

echo -n "Connection (-c, default is 4800): "
read __read_connection

echo -n "Timeout (second, -T, default is 2): "
read __read_timeout

echo -n "Duration (second, -d, default is 10): "
read __read_duration

echo -n "Other pramaters: "
read __read_parameters

if [ ! -n "${__read_ua}" ]; then
    __read_ua="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
fi
if [ ! -n "${__read_thread}" ]; then
    __read_thread="2"
fi
if [ ! -n "${__read_connection}" ]; then
    __read_connection="4800"
fi
if [ ! -n "${__read_timeout}" ]; then
    __read_timeout="2"
fi
if [ ! -n "${__read_duration}" ]; then
    __read_duration="10"
fi
if [ -n "${__read_referrer}" ]; then
    __referrer="-H'Referer: ${__read_referrer}'"
fi

touch run.sh

echo -n "
#!/bin/sh
while true
do
  ./wrk -t${__read_thread} -c${__read_connection} -d${__read_duration}s ${__referrer} -T${__read_timeout}s -H'User-Agent: ${__read_ua}' ${__read_parameters} ${__read_url}
done
" > run.sh

chmod +x run.sh

echo "-----------------------------------"
echo "Execute run.sh!"
echo "-----------------------------------"