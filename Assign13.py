# Q1. What is an access token? #
An access token is an object that describes the security context of a
process or thread. The information in a token includes the identity and
privileges of the user account associated with the process or thread.
When a user logs on, the system verifies the user's password by
comparing it with information stored in a security database.
If the password is authenticated, the system produces an access token.
Every process executed on behalf of this user has a copy of this access token.

The system uses an access token to identify the user when a thread interacts
with a securable object or tries to perform a system task that requires
privileges.

# Q2. Get the IP address of some common sites like Google, Facebook by
using DNS lookup. #

Google - 216.58.217.132
Facebook - 157.240.16.39
Microsoft - 49.44.170.146
IBM - 23.213.74.71

# Q4. What is a difference between library and API. Figure it out with
examples.

A library is a collection of functions / objects that serves one particular
purpose. you could use a library in a variety of projects. For eg:- junit.jar,
log4j.jar.

An API is an interface for other programs to interact with your program or
library  without having direct access. For eg:- Google Map API's , JSON.

