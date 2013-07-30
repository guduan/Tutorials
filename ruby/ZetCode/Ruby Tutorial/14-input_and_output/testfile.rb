#!/usr/bin/env ruby

puts File.exists?("tempfile")

f = File.new("tempfile", 'w')
puts File.mtime("tempfile")
puts f.size

File.rename("tempfile", "tempfile2")

f.close
