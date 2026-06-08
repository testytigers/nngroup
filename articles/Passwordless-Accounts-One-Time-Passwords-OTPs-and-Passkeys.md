# Passwordless Accounts: One-Time Passwords (OTPs) and Passkeys

**Author:** Raluca BudiuRaluca BudiuJune 25, 20232023-06-25

**Topics:** Design Patterns, Mobile & Tablet

**Source:** https://www.nngroup.com/articles/passwordless-accounts/

---

June 25, 20232023-06-25

Share

Passwords are a major pain point in any user experience. Until recently, this pain point was considered unavoidable. But one-time passwords and passkeys save users from the hassle of having to create, store, retrieve, or remember a password. These new developments are particularly seamless on mobile, but they can improve the login user experience on desktop as well.

Passwords areannoying.They are hard tocreate, hard to type, and hard toremember.

Many of us rely on our smartphones to save passwords, which certainly helps to reduce the pain of passwords. For example, in a recent survey that we carried out:

Even if you use a crutch such as a password manager (whether built into the phone or a third-party one), the interaction is clunkier when a password is involved.

For example, sometimes a password field is not recognized and theuser is not offered the choice to use a password-manager generated password. Or, sometimes the password manager will not read the password requirements on the site and will createa password that might not match what the site or app demands.

Additionally, if the user saves passwords on multiple devices, they may havetrouble remembering on which device they created the account. For example, I always struggle to figure out whether the password is in iCloud on one of my Apple devices, in Edge or Chrome (which I use on my Windows computer), or in the 3rd party password-manager application that I also use.

There aretwo important interaction flowsassociated with passwords:registration and login.

Withlogin, we saw significant usability progress once biometric authentication became available. People who were willing to share their fingerprint and face data could skip the recall and entry of a password. As a result, biometric authentication saved users considerable time and effort.

But how aboutregistration? Until recently, whenever users had to create a new account (unfortunately, this is way too often on modern sites and apps), they had to create a password that satisfied complicated requirements which varied depending on the site or application. Often,these requirements would not be disclosed in advance, forcing people to guess what the password should look like. Then, when they failed to guess correctly, they had to navigate the obligatoryerror messagethat told them that the password does not satisfy all the constraints.

However, a new, welcome trend that alleviates the registration problem is that of passwordless accounts.

Definition: Apasswordlessaccountis an account that does not have a password associated with it. The user can securely authenticate and log in, but there is no fixed password that they need to type to access their account.

There are two types of passwordless accounts: OTP-based and passkey-based accounts.

One-timepasswords(OTPs) are codes that are sent to a phone number or email associated with an account. These codes serve as temporary passwords: the user can log into their account using the OTP for authentication. (When the code is sent through the email, it sometimes takes the form of what’s called amagic link.)

One-time passwords are useful because the user does not have to:

However, one-time passwords do incur some costs — namely, the user has to:

Note that the access cost can be minimal if the OTP is sent through a text message that appears as a suggestion on top of the keyboard (without the user having to leave the corresponding page). However, accessing theOTP is more difficult when the link is sent through email.This is because the user must switch applications and access that email in order to authenticate. Moreover, there is also the risk that the email will be filtered out as spam by the email client.

Until recently, OTPs were used mostly for login — account holders could choose to log in by inputting their passwords or through an OTP. But why couldn’t the user use OTPs at all times, without ever creating a password?

That is the idea behind OTP-based passwordless accounts.With a passwordless account, the account holder always uses an OTP or a magic link to log in. They don’t have to create a password: whenever they want to log in, they are sent an OTP or a magic link.

Even though OTPs can be great if the user has forgotten their password, as we emphasized above, they are not without costs. Users who store passwords on their phones or in their browsers may find it easier to have them automatically filled in by the browser. Thus, such users may prefer to define a password for the account and then have the browser automatically fill it in for them.

Therefore, even for those accounts which can be created without a password, we recommend that youoffer users the option to later attach a password to the account. That way, they can log in even faster — at least on a subset of their devices. Users should not, however, be forced to create a password if they do not want to.

Additionally,allowusers the choice to log in using biometricauthentication. That can speed up the process even more for those people who are willing to do it. (Our survey shows that83% of users use a biometric method of authentication at least occasionally, with a 95% confidence interval between 73%–87%.)

OTPs can be used on desktops or laptops, too. If the code is sent through a text message, it may be a little harder to copy it on the desktop, unless the user has set up texting on their computer (for example, using the Messages application on a Mac). But the user may be able to easily copy and paste an email code, as the screen is larger and task switching is generally easier on desktop.

For that reason, especially for responsive sites that are likely to work on both desktop and mobile,consider offering the user the choice of how to receive the OTP — through email or text message.

Another welcome trend in the world of authentication is passkeys. Passkeys are different than OTPs, but they also create a passwordless user experience. They rely on the other advancement in login technology — biometric authentication.

Apasskeyis a password that is invisible to the user. When you’re trying to register on a site that supports passkeys, your device will create a password for you; that password will be stored encrypted on the device (or somewhere in the cloud). Next time when you will log into the site, your device will use biometric authentication (such as fingerprint or face ID) to identify you, and, if that authentication was successful, will send your encrypted passkey to the website. The website will then log you in.

Passkeys are obviously more usable than regular passwords:the user does not have to either remember, store, or type them. They also have lowerinteraction costthan OTPs: users do not have to type them, copy or paste them, or even click on a link to select them.

Additionally,they are more secure than regular passwordsbecause they are not stored by each website. Instead, they are stored encrypted on your device, so they are less susceptible to data breaches and hacks. Even if the data was stolen, the thieves would have to also have access to your biometric authentication to use them. Plus, they cannot be used for phishing because they only can be sent to the sites they are associated with.

The catch is that,if you are going to use the site across several devices, it may not be possible to easily take advantage of them on all. For example, if you’ve created your passkey on an iPhone and you’re trying to authenticate on an Android or Windows tablet, the website will have to show a QR code and you will need to scan it with your iPhone to enable authentication. (However, passkeys will work seamlessly across all Apple devices because they are synced in iCloud.)

So, the benefits of lower interaction cost exist only if the user is using the same device (or the same device ecosystem) to access the website. But still, most people have their phones nearby at all times. Scanning a QR code with the phone’s camera is easier than typing a password or copying and pasting a string.

To summarize, passwordless accounts can help reduce friction during login and registration. Follow these recommendations to ensure a smooth passwordless-account experience for your users.