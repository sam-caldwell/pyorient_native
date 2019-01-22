#ifndef PORTABLE_ENDIAN_H__
    #define PORTABLE_ENDIAN_H__

    #if (defined(_WIN16) || defined(_WIN32) || defined(_WIN64)) && !defined(__WINDOWS__)

        #define __WINDOWS__
        #include <winsock2.h>

    #elif defined(__linux__) || defined(__CYGWIN__)

        #include <arpa/inet.h>
        #include <endian.h>

        #undef ntohll
        #undef htonll

        #define ntohll(x)  be64toh(x)
        #define htonll(x)  htobe64(x)

    #elif defined(__APPLE__)

        #include <arpa/inet.h>
        #include <libkern/OSByteOrder.h>

        #undef ntohll
        #undef htonll

        #define ntohll(x)  OSSwapBigToHostInt64(x)
        #define htonll(x)  OSSwapHostToBigInt64(x)

    #elif defined(__OpenBSD__)

        #include <sys/endian.h>
        #include <arpa/inet.h>

        #undef ntohll
        #undef htonll

        #define ntohll(x)  be64toh(x)
        #define htonll(x)  htobe64(x)

    #elif defined(__NetBSD__) || defined(__FreeBSD__) || defined(__DragonFly__)

        #include <sys/endian.h>
        #include <arpa/inet.h>

        #undef ntohll
        #undef htonll
        #undef be64toh

        #define be64toh(x) betoh64(x)
        #define ntohll(x)  be64toh(x)
        #define htonll(x)  htobe64(x)

    #else

        #error platform not supported

    #endif

#endif