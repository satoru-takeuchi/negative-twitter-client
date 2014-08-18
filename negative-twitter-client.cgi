#!/usr/bin/ruby
# -*- coding: utf-8 -*-

require "cgi"
require "twitter"
load "config.rb"

cgi = CGI.new

client = Twitter::REST::Client.new {|c|
  c.consumer_key = CONSUMER_KEY
  c.consumer_secret = CONSUMER_SECRET
}

print cgi.header
user = cgi["user"]
tl = client.user_timeline(user, {:count => TWEET_COUNT})
tl.each {|e|
  next if e.favorite_count > 0 && e.retweet_count > 0

  puts "<p>まことに残念ながら、あなたの以下の渾身のつぶやきは、今の今まで"
  puts "誰からもふぁぼられませんでした。" if e.favorite_count == 0
  print "さらに悪いことに、" if e.favorite_count == 0 && e.retweet_count == 0
  puts "誰からも retweet されませんでした。" if e.retweet_count == 0
  puts "</p>"
  puts "<p><strong>'#{CGI.escapeHTML(e.text)}'</p></strong>"
  puts "<hr/>"
}
