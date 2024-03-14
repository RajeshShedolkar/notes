<dl>
<dt>What Socket.IO is?</dt>
<dd><p>
Socket.IO is a library that enables low-latency, bidirectional and event-based communication between a client and a server.
</p></dd>

<dt> 
<p>
The Socket.IO connection can be established with different low-level transports:
</p>
</dt>
<dd>
<p>
<b>HTTP long-polling</b> - requesting repetitively
<p>
<b>WebSocket</b> - The WebSocket API is an advanced technology that makes it possible to open a two-way interactive communication session between the user's browser and a server. With this API, you can send messages to a server and receive event-driven responses without having to poll the server for a reply.
</p>
<p>
<b>WebTransport</b>  - The WebTransport API provides a modern update to WebSockets, transmitting data between client and server using HTTP/3 Transport. WebTransport provides support for multiple streams, unidirectional streams, and out-of-order delivery. It enables reliable transport via streams and unreliable transport via UDP-like datagrams.
</p>
</p>
</dd>



<dt>Question</dt>
<dd>
  io.on("connection", socket => {
  socket.join("some room");
});  
</dd>
<dt>Question</dt>
<dd>Answer</dd>
</dl>
