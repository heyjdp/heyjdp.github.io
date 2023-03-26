--- 
title: "\U0001f4bb AGE Authenticated Encryption to replace GPG/PGP \u26D3 \U0001f510 \U0001f469\u200D\U0001f4bb" 
date: 2023-03-26T10:00:00+02:00 
draft: false 
tags: ["tech", "crypto", "gpg", "age", "privacy"] 
hidemeta: false 
disableShare: false
disableHLJS: false # This is the code highlighting
hideSummary: false
searchHidden: true
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
cover:
    image: "/post-img/elaborate-key-1200x630.jpg" # image path/url
    alt: "Elaborate looking key on an old leather desk blotter" # alt text
#    caption: "" # display caption under cover
    relative: false # when using page bundles set this to true
    hidden: false # only hide on current single page
---

This page is about using AGE to replace GPG/PGP for encryption.

<!--more-->

Age Authenticated Encryption (AGE) is a new cryptographic system developed by Filippo Valsorda [^1] that provides several advantages over traditional encryption systems such as GPG/PGP. AGE offers a modern approach to encryption that is designed to be easy-to-use, secure, and resistant to various types of attacks. AGE is fully open source and is available on GitHub [^2].

One of the key advantages of AGE over traditional encryption systems such as GPG/PGP is its simplicity and ease-of-use [^3]. AGE uses a simple command-line interface that makes it easy for users to encrypt and decrypt files and messages. Unlike traditional encryption systems, which can be complex and difficult to use, AGE provides a streamlined user experience that reduces the risk of user error and ensures that files and messages are properly encrypted and protected.

Another advantage of AGE over traditional encryption systems is its use of authenticated encryption [^4]. Authenticated encryption provides both confidentiality and integrity to the data being transmitted, ensuring that the data is protected from unauthorized access and tampering. In contrast, traditional encryption systems such as GPG/PGP only provide confidentiality and do not provide any guarantee of data integrity.

AGE also provides support for forward secrecy, which is a critical feature in modern cryptography. Forward secrecy ensures that even if the encryption keys are compromised in the future, the previously encrypted data remains secure. AGE achieves forward secrecy by using a unique symmetric key for each file or message, which is then encrypted with the recipient's public key. This approach ensures that even if an attacker gains access to the recipient's private key, they will not be able to decrypt any previously encrypted data.

Another advantage of AGE over traditional encryption systems is its resistance to various types of attacks, including side-channel attacks and key-extraction attacks. Side-channel attacks are a type of attack that exploit weaknesses in the physical implementation of a cryptographic system, while key-extraction attacks are a type of attack that attempts to extract the encryption keys from the system. AGE is designed to be resistant to both types of attacks, ensuring that the encrypted data remains secure and protected.

A number of other bloggers have notes on AGE encryption, please enjoy: [^5] Neil Madden's thoughts; [^6] Techno Tim's install journey; [^7] Pablo's Spot YouTube video called 'Encrypting and decrypting files at rest using AGE'.

Finally, AGE is designed to be resistant to quantum computing attacks, which is a growing concern in the field of cryptography. Quantum computing has the potential to break many of the current cryptographic systems used today, including traditional encryption systems such as GPG/PGP. AGE uses modern cryptographic techniques that are resistant to quantum computing attacks, ensuring that the encrypted data remains secure and protected even in the face of future technological advances.

In conclusion, AGE provides several advantages over traditional encryption systems such as GPG/PGP. AGE offers a modern approach to encryption that is designed to be easy-to-use, secure, and resistant to various types of attacks. AGE provides authenticated encryption, support for forward secrecy, resistance to side-channel and key-extraction attacks, and resistance to quantum computing attacks. While traditional encryption systems such as GPG/PGP remain widely used and trusted, AGE offers an alternative approach that may be preferable for certain use cases.

## References

[^1]: https://words.filippo.io/dispatches/age-authentication/
[^2]: https://github.com/FiloSottile/age
[^3]: https://htmlpreview.github.io/?https://github.com/FiloSottile/age/blob/main/doc/age.1.html 
[^4]: https://github.com/C2SP/C2SP/blob/main/age.md 
[^5]: https://neilmadden.blog/2019/12/30/a-few-comments-on-age/
[^6]: https://docs.technotim.live/posts/install-age/ 
[^7]: https://www.youtube.com/watch?v=X4QT3EgKNUo 
