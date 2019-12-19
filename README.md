# IATI Proxy

A proxy service that adds CORS to IATI registry data, so that it can be reused more easily.

Requests should be in the following format:

```
https://iati-proxy.herokuapp.com/raw?dataset=[dataset ID]
```

So for example: https://iati-proxy.herokuapp.com/raw?dataset=pwyf-org
