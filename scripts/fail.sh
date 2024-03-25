dir=/home/jer/h0t_d0g

$dir/led.sh all_off
python $dir/oled.py fail
$dir/led.sh all_red
$dir/osc.sh fail
for i in {1..4}
do
	python $dir/gpio.py vib_on
	sleep 0.2
	python $dir/gpio.py vib_off
	sleep 0.2
done
$dir/osc.sh off
$dir/led.sh all_off
python $dir/oled.py ready
