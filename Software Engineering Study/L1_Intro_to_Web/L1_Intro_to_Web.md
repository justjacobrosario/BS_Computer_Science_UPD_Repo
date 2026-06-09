

# 1. Intro to Internet
## 1.1. History of Internet
1. Internet was originally used for universities to communicate remotely about the development of AI
2. ARPANET : primitive version of the Internet
## 1.2. Terminologies
1. WWW : way the data, webpages, and services arranged
2. Internet : the backbone of the Web, the hardware connecting computers internationally
3. Server : A computer connected directly to the internet
4. Personal Computer : Domestic computer, not typically connected directly to the Internet
5. IP Address : Every server and computer  have unique IP addresses
6. Local Network (LAN) : A network of computers connected locally without the Internet
7. Switch : Connects computers locally and directs data in a LAN
8. Internet Service Provider (ISP) : Connects PC's to the Internet
9. Packets : Fragments of a data that passes through the Internet.
10. Router : Directs packets around the Internet by connecting one network to another.

## 1.3. How the Internet Works

1. The Internet is a connection connecting computers (called servers)
2. Servers, and domestic personal computers (PCs) have unique IP Address, which is aliased by their web address (e.g. google.com)

A. Connecting Computers (No Internet needed)
1. The network in which a PC is connected to another PC without passing through the internet is a local network (LAN).
2. As a LAN gets crowded by PCs, one PC must connect to other PCs individually (like a complete graph, needed too much wires and connections).
3. Instead of only having direct connections from PC A to B, we use network switches (aka switches), which traffics and directs data from its origin to its respective destination (like railway intersections).

B. Connecting Computers (Internet needed)

1. Personal computers are connected to the Internet (interconnected networks) through an Internet Service Provider.
2. Sending data from one PC to another passes through ISPs of those PCs and then to the Internet
3. Sending data through the internet needs it to be fragmented into tiny information called packets
4. Those packets of data can have separate routes from one point to another. Despite that, packets will approach to their destination precisely by the help of routers, which directs packets to the right device.
5. Initially, packets contain the IP address of its origin computer. As it passes through a router, the packet will record the router's IP address. Several routers will lead packets to contain their IP address consecutively. (Imagine each computer, switch, router, and server wrapping their IP address on top of each other.)
6. As the packets return back to the original computer. The recorded IP address will then be unwrapped as it go back to the same route.

## 1.4. Parts of Internet
1. Intranet : private networks restricted to members of a particular organization
2. Extranets : Part where a part of intranets are open for interaction with each other
3. Internet : Interconnected extranets

# 2. Intro to Web
## 2.1. Web Terminologies

1. Web page : a document that can be displayed in the web browser (HTML documents)
2. URL : unique address of a webpage
3. Website : Collection of web pages that share a domain name (e.g. facebook.com)
4. Web server : A computer that hosts a website  on the Internet
5. Web Service : Backed by a web server, is a software or a website that perform a function (e.g. pdf resizer, weather report)
6. Search Engine : A web service that  helps one find web pages
7. Browser : a software that retireves and displays web pages (e.g. Google is both a browser and a search engine)