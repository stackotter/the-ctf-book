# Introduction | Web part 1

Almost every piece of technology in existence is connected to the internet in one way or another;
laptops, phones, toasters, fridges, you name it. And every single piece of code that communicates
with the internet is a prime target for hackers. An attacker can sit at home and look for holes in
the security of internet-connected systems all day long.

In this series of lessons we will focus on website hacking, one aspect of internet-based hacking.
We'll start off by learning how a simple website might work.

## How does my computer know what Google looks like?

Let's take a look at what happens when you tell your browser that you want to visit
`https://www.google.com`.

### Domain name resolution

The `www.google.com` part of the URL is called the domain name. A domain name is basically a nice
looking name that is associated with 1 or more physical computers that are connected to the
internet. To talk to a physical computer connected to the internet, your computer needs to know the
other computer's ip address. This is where domain name servers (DNS) come into play. Your computer
is configured with a specific domain name server (there are many to choose from), and when it needs
to find out which computers are associated with a specific domain name, it'll ask that server. In
reality it's more complicated, but that's the gist of it.

On macOS and Linux, you can use the `dig` command to try this out for yourself (Figure 1.1).
Entering the ip address that it gives you into your browser will show you google just like normal.

```
$ dig +noall +answer www.google.com
www.google.com.		208	IN	A	142.250.204.4
```
Figure 1.1: *performing domain name resolution for `www.google.com`*

### HTTP

Once your computer knows which ip address corresponds with `www.google.com`, it will open a
connection to the server. If the address starts with `http://`, the connection isn't encrypted, and
if it starts with `https://` the connection is encrypted.

HTTP (Hypertext Transfer Protocol) is what your browser uses to ask the google server for the
contents of the page. An example of an HTTP request (Figure 1.2) and an HTTP response (Figure 1.3)
are included below.

```
GET / HTTP/1.1
Host: www.google.com
```
Figure 1.2: *example HTTP request*

```
HTTP/1.1 200 OK
Date: Sat, 30 Jul 2022 23:34:09 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
Server: gws
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN
Accept-Ranges: none
Vary: Accept-Encoding

<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" ...
```
Figure 1.3: *example HTTP response (truncated for brevity)*

The cool this is, you can try this out for yourself! All you need is to have netcat installed (if
you have a ctf-debian container set up you can use that, see `../../SettingUpDocker.md`). Use the
command `nc www.google.com 80` to connect to google (80 is the port for http), and then copy and
past the example request (from Figure 1.2). Now hit enter twice to finish the request, and you'll
receive a wall of text. Copy and paste the html part of the response into an html file and open it
in your browser. The page you get won't function very well because it is missing some resources, but
it will look vaguely like Google. See Figure 1.4 for an example of using netcat to send an HTTP
request.

```console
$ nc www.google.com 80
GET / HTTP/1.1
Host: www.google.com

HTTP/1.1 200 OK                       <- end of input and start of response
Date: Sat, 30 Jul 2022 23:34:09 GMT
Expires: -1
...
```
Figure 1.4: *using netcat to send an HTTP request (annotated)*

### HTML, CSS and JS

HTTP servers will send back the contents of the requested page as an HTML document. To display the
page on screen, the browser has a renderer which can turn HTML into a picture to show you on screen.

As a hacker, JS (JavaScript) is a very appealing tool, because if they can get some JS onto a
website, they can run code in the browser of whoever sees the page containing the hacker's JS. We
will be looking into this type of attack in more depth later on.

To view the contents of a webpage, you can use your browser's developer tools. How you open these
varies by browser. Here are some instructions for the most popular browsers, it'll be worth your
while to learn the keyboard shortcut for the browser and operating system that you use.

- **Chrome**: Click the three dots in the top right, select the `More Tools > Developer Tools` menu
  item
- **Safari**: <kbd>option</kbd> + <kbd>cmd</kbd> + <kbd>i</kbd>
- **Firefox**: Select the `Tools > Web Developer > Web Developer Tools` menu item
- **Microsoft Edge**: Same as Chrome

Keep this in mind for your first website hacking challenge.

### Conclusion

In practice there are a few more details than that when loading a website, but those are all the
basics that you'll need to know for you first few challenges.

## Your first web hacking challenge

Now that you've got a basic idea of how a website works, let's try and hack one. The first challenge
you will be solving is called `vault`. Looking at the readme gives us a description for the challenge
(Figure 1.5).

> stackotter has stored their deepest secret in a high security vault. Can you find out what it is?
> 
> `http://localhost:8081/`
Figure 1.5: *description for `vault` challenge*

That sounds interesting, let's run the challenge and take a look. For all of the web challenges you
will face in this series, you will find a file called `challenge.py` which will run the challenge
for you. Just run it the same way you would any other Python program; I use the `python3` command
(Figure 1.6) but you can use another method if you want.

```
$ python3 challenge.py
Serving HTTP on :: port 8081 (http://[::]:8081/) ...
```
Figure 1.6: *running the challenge*

You can visit the challenge website in your browser at [http://localhost:8081/](http://localhost:8081).
You should see something like Figure 1.7.

```
stackotter's vault

This vault guards my deepest secret, that's why I made it so secure!

-------------  --------
|password   |  |submit| 
-------------  --------
```
Figure 1.7: *the challenge website*

Try a few passwords and you'll see that none of them work. Let's take a look at how this website
works by looking at its source code. Can you remember how? I'll leave the rest of this challenge up
to you, good luck! If you get stuck, you can look at the solution in `Solution/Solution.md`.
