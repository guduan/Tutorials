#!/usr/bin/env ruby

A = [1, 2, 3, 4, 5]
B = [4, 5, 6, 7, 8]

union = A | B
isect = A & B
diff1 = A - B
diff2 = B - A
sdiff = (A - B) | (B - A)

puts "Union of arrays: #{union}"
puts "Intersection of arrays: #{isect}"
puts "Difference of arrays A - B: #{diff1}"
puts "Difference of arrays B - A: #{diff2}"
puts "Symmetric difference of arrays: #{sdiff}"
