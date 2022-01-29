# Lambda use in a simple Ruby code


calc = lambda { |pricing, discount| pricing * (100 - discount) / 100 }

puts "Enter the product price: "
price = gets.chomp.to_i

puts "Enter your discount %: "
percent = gets.chomp.to_i

puts "Total price to pay $#{calc.call(price, percent)}"