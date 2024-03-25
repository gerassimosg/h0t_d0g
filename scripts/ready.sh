dir=/home/jer/h0t_d0g

$dir/osc.sh ready
for i in {1..2}
do
	python $dir/gpio.py vib_on
	sleep 0.1
	python $dir/gpio.py vib_off
	sleep 0.1
done
$dir/led.sh all_off
python $dir/oled.py ready

