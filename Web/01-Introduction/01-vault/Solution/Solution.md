Open your browser's developer tools, navigate to the `Sources` tab and view the source of the page.
In most browser's you can also right-click on the page and then select the `View Page Source` or
`Show Page Source` menu item. Once you have the page source, you can look through the code so see
how the password is checked. It is checked in a simple if statement in the page's JavaScript so we
can just copy and paste that password to get in. Alternatively, we can see that when you win, the
page sends you to the `/flag.html` page so we can visit `localhost:8081/flag.html` directly to win.
