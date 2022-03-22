require 'open-uri'
require 'zlib'
require 'yajl'

gz = open('http://data.gharchive.org/2015-01-01-12.json.gz')
js = Zlib::GzipReader.new(gz).read

Yajl::Parser.parse(js) do |event|
  print event
end