## How the exploit works

1. Start a server that the payload will send the admin's cookies to
2. Add a malicious comment to the website that contains a payload. The payload is created such that
   when a user views the page, their cookies get sent back to the exploit server via a get request
   using `XMLHttpRequest`. The endpoint that the payload sends the cookies back to is randomised
   each time so that previous exploit attempts do not interfere with the current exploit attempt.
3. The exploit server receives the cookies, and then makes a get request to the admin page of the
   cheesecake website using the cookies.
4. The exploit server then extracts the flag from the admin page's html, prints it out, and exits.

## Running the exploit

To run the exploit (`exploit.py`) you will first need to update `host`, `port` and `base_target_url`
accordingly unless you are running both the website and the exploit on your local machine.

Sadly exploiting these types of bugs when the website is running on a server outside of your local
network does require access to some sort of machine that is accessible from the open internet.
Common ways of achieving this are: hosting your exploit on `pythonanywhere`, port-forwarding a port
from your computer to the public internet if you have access to your router's admin settings, or
renting a Linux machine/container in the cloud (through a service such as Linode or Azure).
