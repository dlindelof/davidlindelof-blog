---
title: "Weird certificate verification error"
date: 2010-07-01
categories: 
  - "programming"
tags: 
  - "ssl"
---

I spent most of the day today debugging a very mysterious error we encountered when trying to programmatically call a web service over SSL from Java.

Here is the source code with which we managed to reliable reproduce the error:

import javax.net.SocketFactory; import javax.net.ssl.SSLSocketFactory; import java.io.\*; import java.net.Socket; public class SimpleSSLTest { public static void main(String\[\] args) throws IOException { try { int port = 443; String hostname = "somehost.com"; SocketFactory socketFactory = SSLSocketFactory.getDefault(); Socket socket = socketFactory.createSocket(hostname, port); InputStream in = socket.getInputStream(); OutputStream out = socket.getOutputStream(); PrintWriter pout = new PrintWriter(new BufferedWriter(new OutputStreamWriter(out))); pout.println("GET " + "/" + " HTTP/1.0"); pout.println(); pout.flush(); BufferedReader bin = new BufferedReader(new InputStreamReader(in)); String inputLine; while ((inputLine = bin.readLine()) != null) { System.out.println(inputLine); } in.close(); out.close(); } catch (IOException e) { throw e; } }

The website, \`somehost.com\`, used a SSL certificate signed by our own internal certificate authority. That authority's certificate was stored in a \`cacerts\` Java keystore. We run this code from the command line thus:

$ java -Djavax.net.ssl.trustStore=cacerts -cp target/classes/ SimpleSSLTest When we run this, the application bombs with an exception, the root cause of which reads as follows:

Caused by: java.security.cert.CertPathValidatorException: CA key usage check failed: keyCertSign bit is not set at sun.security.provider.certpath.PKIXMasterCertPathValidator.validate(PKIXMasterCertPathValidator.java:153) at sun.security.provider.certpath.PKIXCertPathValidator.doValidate(PKIXCertPathValidator.java:325) at sun.security.provider.certpath.PKIXCertPathValidator.engineValidate(PKIXCertPathValidator.java:187) at java.security.cert.CertPathValidator.validate(CertPathValidator.java:267) at sun.security.validator.PKIXValidator.doValidate(PKIXValidator.java:261) ... 22 more

We've tried to wrap our heads around this problem the whole day and could make neither head nor tail about it, especially as we didn't get this error at all when targeting another host, using another certificate but signed by the same certificate authority.

As a last resort, I thought of checking exactly which version of Java we were using. Turned out we were using OpenJDK, the version that replaced Sun's version in Ubuntu 10.4. Running the same code with Sun's Java SDK solved the problem, but we can't confidently state that we understand what was wrong. Perhaps a bug in OpenJDK's implementation of JSSE. Who knows.

If you've run into the same problem, feel free to leave a comment. I'd be interested to hear if (and how) you've solved it.
