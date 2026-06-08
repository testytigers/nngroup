# Slow UI: Pace Interaction to Increase Understanding [APRIL FOOLS]

**Author:** Jakob NielsenJakob NielsenApril 1, 20202020-04-01

**Topics:** UX Humor

**Source:** https://www.nngroup.com/articles/slow-ui/

---

April 1, 20202020-04-01

Share

(This article was an April Fool's hoax and does not contain genuine usability advice.)

There is no doubt that the traditional emphasis onspeed in user-interface design has gone overboard. Yes, there’s something to be said forfast response timesandweb pages that download immediately. And for decades, one of the5 measurable quality attributes of usabilityhas beenefficiency: Once users have learned the design, how quickly can they perform tasks?

Today I’m here to tell you toslow down. Thanks to Moore’s Law computers have become abillion times faster sinceI started using computers in 1974, and thanks to Nielsen’s Law,Internet connection speeds are 1.2 million times fasterthan when I first got online in 1984. Technical progress, yes, but human progress? Not so much. We frequently see that users’ desire to rush through user interfaces impairs understanding and reducessuccess rates.

We’ve long known that thespeed of acquiring new information on the webmakes people treat online information incrediblysuperficially:users scan text, they don’t read carefully.

On average,users only spend enough time on a web page to read 28% of its words.

Clearly, we need to makeusers spend more time on each web page, so that they read closer to 100% of the content and have a chance to understand what we’re saying. How can we do that?

For articles, we often present an estimated reading time. For example, this article will be listed inour email newsletteras a 7-minute read. Since we have a high-IQ audience, our reading-time estimates are calculated for a highly capable reader with the reading skills expected of people with graduate degrees. But we could just as easily calculate the required reading time for alow-literacy reader. If we stated that the expected time to read this article was, say, 16 minutes, then this number would become the anchor that users employed to judge their own reading time. Thus, they would feel quite accomplished if they finished reading this article in 11 minutes, allowing us 4 extra minutes impart wisdom to the users.

Rushed navigation is even worse than rushed reading. Users don’t allow themselves sufficient time to carefully consider all navigation options, but rather click the link that has the highestinformation scent. In a well-designed website with greatinformation architecture, this link will contain the answer to the user’s problem. But in the real world? Probably not.

The most costly usability problems in web design stem frompremature clicking: users sniff something promising, impulsively click the link, and are lost in the (metaphorical) woods for minutes until they realize that they are in the wrong place and reach for theBackbutton. A few seconds gained from fast clicking usually incur a penalty of 100 times more wasted time. We would do users a major favor by slowing them down in these cases.

Navigating digital information is modeled byinformation-foraging theory, which is an analogy with how animals acquire food in nature. But what will happen to a lion that wakes up one morning and immediately starts running forward if it catches a whiff of antelope? No soup for you! The lion would miss any juicy Thomson's gazelle that happened to be grazingbehindthe lion. A smart lion takes the time to look around in all directions and evaluate its options before setting out on the hunt.

We should force users to do the same.

Clearly, the easiest way to force users to carefully evaluate all navigation options before they click is to implement atimeout feature,where links only become clickable 30 seconds after being displayed. This solution works well with hamburger menus,pizza menus, or other menus that are initially hidden and only become visible after an explicit user action — because we know precisely the moment when the links were displayed.

But what should we do in those situations where navigation is always visible? One idea would be to never make it visible, but this won’t work on big screens — we know thathidden navigation has a big usability costand should be avoided on platforms that have sufficient screen space for visible navigation. So, we need a different approach to encourage slow clicking in desktop user interfaces.

Let’s turn back to nature for inspiration. Look back at my photo of Thomson's gazelle. You can clearly see the animal being quite worried: even though there was no lion around, the gazelle had probably heard that I like venison. If I had approached, the gazelle would have run off. Why not have website navigation bars do the same? As the cursor approaches the navigation bar, the bar can move out of the way, and keep playing hard to get until the user has spent the recommended 30 seconds looking around and considering all the options.

Assume that we have slowed down users enough that they understand what we’re trying to tell them. And we have also delayed their clicking sufficiently that they are more likely to pick the right links. Victory is almost ours, but not quite. Thousands of usability studies have confirmed that users will make mistakes even when they’re using simple UI elements such ascheckboxes, radio buttons, ordropdowns.We need to also slow down UI controls and interactions at the page level.

Let’s say we have anecommercesite that sells green, yellow, and blue T-shirts in sizes S, M, L, and XL. It’s great if we design the navigation to be slow enough that users can find the T-shirt page. And it’s great if we make users read slowly enough to realize that these items are T-shirts that come in different colors and sizes. But since users will still have tospecifytheir preferred color and size, things will still go wrong no matter howwell we design the T-shirt product page. There’s only 8% chance of hitting on the correct combination of color and size if users rush too much. A 92% return rate due to erroneously ordered T-shirts will kill any business.

The color picker and size selector should be designed to work so slowly that we maximize the probability that users have time to specify the shirt they actually want.

Luckily, we already have a very slow way of specifying a color choice: the color wheel, as designed by Adobe. This company has a huge staff of highly professional UX designers who have spent years designing a very precise way of specifying colors that’s useful for professional visual designers. Usually, wewarn against using a famous company’s designfor a different task, but in this case, the Adobe color wheel will work just fine, with just one tweak: If the user picks a color that’s not identical to one of the offered T-shirts, we’ll display the error message,Sorry, this color is not available, please pick another.

This follows 2 of the 3 main elements ofgood error-message design, because it helps the user to recognize and diagnose the error. The message doesn’t provide sufficiently constructive advice on how to recover from the error, and normally we would recommend including the hex codes for the available colors. Unfortunately, while doing so would improve compliance withusability heuristics #9(help users recognize, diagnose, and recover from errors), it would fall afoul of #2,match between the system and the real world, which calls for using familiar language such as “green” and “yellow” instead of hex values. However, just saying “yellow” wouldn’t help users pick theexactshade of yellow in our fabric, so we must accept a small violation of the usability heuristics to serve the higher cause of slower features.

Size specification can be done even more slowly, while complying with heuristic #2 — match between the system and the real world. The recommended sizing widget is a balloon-like image that is inflated by repeatedly clicking on a button labeledInflate. (Though user testing should be conducted to make sure whether simplified vocabulary, such asMakebigger, would be more understandable.) As the user clicks theInflatebutton, the shirt outline becomes bigger and bigger, realistically matching the size of the desired T-shirt. The user would simply stop clickingInflateat the time when the balloon outline looks big enough to match the desired size T-shirt. (If the user overshoots and inflates the outline too much, a pin-like deflate command will "puncture" the balloon and reset the image to its smallest size, from which the user can start inflating all over again. This should be slow enough to teach the user to be more careful next time.)

The beauty of this design is that it can be slowed down to an arbitrary extent. Maybe it should take 5 clicks on theinflatebutton before the balloon outline has grown to the next T-shirt size. Or maybe we’ll require 10 clicks or even 20. The correct number of clicks can be determined by asimple A/B test.

As we have demonstrated in this article, slow user interfaces have the potential to reduce ecommerce return rates from 92% to a much smaller number. In fact, the slower we make the UI, the fewer orders will be returned.

(And by the way: Happy April Fool's Day.)