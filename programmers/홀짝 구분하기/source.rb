n = gets.chomp.to_i

result = n % 2 == 0 ? "even" : "odd"
puts "#{n} is #{result}"