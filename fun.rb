def more_kon? 
 while true 
 print "kon midi? [a/n]: " 
  case gets.strip 
  when 'A', 'a', 'are'  
  puts "50t razi hasi?" 
 $num2 = gets.strip.to_i 
 for j in 1..$num2 do 
  puts("kon #{j.to_i.ordinalize} code " + ([*('A'..'Z'),*('0'..'9')]-%w(0 1 I O)).sample(8).join ); 
 $num2 +=1; 
 end  
  when /\A[nN]o?\Z/ #n or no 
 puts "Bk ke Nemidi chon khob poli midadam" 
  break  
  end 
 end 
end 
 
$Kon = 1
puts "ahura : Slm haji kon midi?" 
$num = gets.strip.to_i 
puts 'target: emmm...' 
 
begin 
#until $kon > $num do 
for i in 1..$num do 
puts("BK koskesh.count #{i.to_i.ordinalize} " + ([*('A'..'Z'),*('0'..'9')]-%w(0 1 I O)).sample(8).join ); 
$kon +=1; 
end 
more_kon? 
end
