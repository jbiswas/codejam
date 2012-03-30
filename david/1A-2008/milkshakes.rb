def satisfies?(preparation, customer)
	customer.each {|likes, malted| return true if preparation[likes-1] == malted }
	return false
end

def satisfy(preparation, customer)
	if satisfies?(preparation, customer)
		return preparation
	end
	if not customer.value?(1)
		return nil
	end
	raise unless customer[value(customer,1)] == 1
	preparation[value(customer,1)-1] = 1
	raise unless satisfies?(preparation, customer)
	return preparation
end

def value(hash, value)
	hash.each{|k,v| return k if v==value}
	return nil
end

def satisfy_all(n_flavors, customers)
	preparation = Array.new(n_flavors, 0)
	all_satisfied = false
	while not all_satisfied
		all_satisfied = true
		customers.each do |customer|
			all_satisfied = false if not satisfies?(preparation, customer)
			preparation = satisfy(preparation, customer)
			return nil if not preparation
		end
	end
	return preparation
end

N = gets.to_i
N.times do |n|
	n_flavors = gets.to_i
	n_customers = gets.to_i
	customers = Array.new
	n_customers.times do
		preferences = gets.split
		prefs = Hash.new
		n_likes = preferences[0].to_i
		(1..(preferences.length-1)).step(2) do |i|
			prefs[preferences[i].to_i] = preferences[i+1].to_i
		end
		raise unless n_likes == prefs.length
		customers.push(prefs)
	end
	customers.shuffle!
	raise unless n_customers == customers.length
	preparation = satisfy_all(n_flavors, customers)
	print "Case ##{n+1}:"
	if preparation
		raise unless n_flavors == preparation.length
		preparation.each {|f| putc " "; putc f.to_s}
		putc "\n"
	else
		print " IMPOSSIBLE\n"
	end
end

