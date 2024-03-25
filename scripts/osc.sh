dir=/home/jer/h0t_d0g
i2c_dir=/usr/sbin

osc_bus=1
osc_addr=0x2c
arg=$1

if [ -z "$*" ]
then
	echo "INVALID ARGUMENT"
	exit 0
elif [ $arg = "ready" ]
then 
	$i2c_dir/i2cset -y $osc_bus $osc_addr 0x00 0x5f
	python $dir/gpio.py osc1_on
	sleep 0.2
	$i2c_dir/i2cset -y $osc_bus $osc_addr 0x00 0xb1
	sleep 0.2
	$i2c_dir/i2cset -y $osc_bus $osc_addr 0x00 0xe4
	sleep 0.2
	python $dir/gpio.py osc1_off

	$i2c_dir/i2cset -y $osc_bus $osc_addr 0x20 0x69
	python $dir/gpio.py osc2_on
	sleep 0.2
	$i2c_dir/i2cset -y $osc_bus $osc_addr 0x20 0xba
	sleep 0.2
	$i2c_dir/i2cset -y $osc_bus $osc_addr 0x20 0xeb
	sleep 0.2
	python $dir/gpio.py osc2_off

	$i2c_dir/i2cset -y $osc_bus $osc_addr 0x40 0xc7
	python $dir/gpio.py osc3_on
	sleep 0.01
	python $dir/gpio.py osc3_off
elif [ $arg = "pass" ]
then 
	$i2c_dir/i2cset -y $osc_bus $osc_addr 0x00 0x5f
	python $dir/gpio.py osc1_on
	sleep 0.8

	$i2c_dir/i2cset -y $osc_bus $osc_addr 0x20 0x20
	python $dir/gpio.py osc2_on
	sleep 0.4
	$i2c_dir/i2cset -y $osc_bus $osc_addr 0x20 0xba
	sleep 0.4
	$i2c_dir/i2cset -y $osc_bus $osc_addr 0x20 0x69
	sleep 0.4
	$i2c_dir/i2cset -y $osc_bus $osc_addr 0x20 0xba
	sleep 0.2
	$i2c_dir/i2cset -y $osc_bus $osc_addr 0x20 0xeb
	sleep 0.4
	python $dir/gpio.py osc2_off
	python $dir/gpio.py osc1_off

	sleep 0.2
	$i2c_dir/i2cset -y $osc_bus $osc_addr 0x40 0xc7
	python $dir/gpio.py osc3_on
	sleep 0.01
	python $dir/gpio.py osc3_off
elif [ $arg = "fail" ]
then 
	$i2c_dir/i2cset -y $osc_bus $osc_addr 0x00 0xb1
	$i2c_dir/i2cset -y $osc_bus $osc_addr 0x20 0xcb
	$i2c_dir/i2cset -y $osc_bus $osc_addr 0x40 0x26
	python $dir/gpio.py osc1_on
	python $dir/gpio.py osc2_on
	python $dir/gpio.py osc3_on
elif [ $arg = "off" ]
then
	python $dir/gpio.py osc1_off
	python $dir/gpio.py osc2_off
	python $dir/gpio.py osc3_off
else
	echo "INVALID ARGUMENT"
	exit 0
fi

