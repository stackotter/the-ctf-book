# Setting up Docker

## Installing Docker Desktop

The installer for Docker Desktop is hosted on [the downloads page](https://www.docker.com/products/docker-desktop/).
How you use the installer depends on which operating system you use.

## What is Docker?

Docker is a system for running lightweight containers. Each container is a Linux operating system
that runs on your computer, and all of the containers can have different configuration, installed
programs, start up scripts, etc.

This is useful for hacking because it allows you to run Linux programs on your computer no matter
what operating system you use. It also means that if the program does anything malicious or crashes
the operating system by accident, it will only crash the container and not your computer. You can
easily create a new container in a few seconds or less.

A container is an instance of an image. An image is comprised of a base Linux operating system and a
collection of programs and configurations.

## CTF Debian

`ctf-debian` is a Docker image that I have created specifically for binary exploitation. It contains
a bunch of debugging and exploitation tools. The `Debian` part of the name comes from the fact that
the container is built on top of Debian Linux - a 'flavour' of Linux that has a relatively small
size and supports most programs.

## Installing `ctf-debian`

Make sure that you have Docker Desktop installed first

### macOS and Linux

1. Open the Terminal app
2. Run `docker pull stackotter/ctf-debian`

### Windows

1. Open Command Prompt
2. Run `docker pull stackotter/ctf-debian`

## Using `ctf-debian`

1. Create a directory on your computer that will be shared between your laptop and the
   container (you can use an existing container instead if you want)
2. Open Docker Desktop
3. Under the `Images` tab you should see `stackotter/ctf-debian`
4. Click the `RUN` button
5. Under `Optional Settings` enter a container name such as `ctf`, for `Container Path` enter
   `/root/shared` and for `Host Path` select the directory that you created earlier
6. Click `RUN`
7. Under the `Containers / Apps` tab you should see the container you just created. Click the CLI
   button to interact with the container through a terminal/command prompt
8. Inside the container, run the `bash` command to get a nicer looking prompt (I will remove the
   need for this at some point, I don't use Docker this way so I never noticed the issue)
