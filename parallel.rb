if(ARGV.length<2)
	$stderr.print "[USAGE] <#process> <list file name> [<sleep_time>]"
	exit
end
sleep_time=0
if(ARGV.length>=3)
	sleep_time=ARGV[3].to_f
end
num=ARGV[0].to_i
cmds=[]
open(ARGV[1]).each{|line|
	cmds<<line.strip
}
count=0
cmds.each{|line|
	sleep sleep_time
	if(count<num)
		#pid1 = fork{ system("echo '"+line+"'") }
		pid1 = fork{ system(line) }
		count+=1
	else
		x=Process.wait
		#pid1 = fork{ system("echo '"+line+"'") }
		pid1 = fork{ system(line) }
	end
}

while count!=0
	x=Process.wait
	count-=1
end

