delay=1
target=""

echo "enter the ip adress or website you wan to ping"
read target

while true; do
  ping -c 1 $target
done
