dir=/home/jer/h0t_d0g

$dir/led.sh all_off
python $dir/oled.py pass
$dir/led.sh all_green
$dir/osc.sh pass
$dir/led.sh all_off
python $dir/oled.py ready
