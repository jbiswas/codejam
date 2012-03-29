def product(v1, v2)
	prod = 0
	v1.each_index {|i| prod += v1[i] * v2[i]}
	prod
end

def smallest_sp(v1, v2)
	v1.sort!
	v2.sort! {|x,y| y <=> x}
	product(v1,v2)
end

N = gets.to_i
N.times do |i|
	gets
	v1 = gets.split.map! {|x| x.to_i}
	v2 = gets.split.map! {|y| y.to_i}
	puts "Case ##{i+1}: #{smallest_sp(v1,v2)}"
end
