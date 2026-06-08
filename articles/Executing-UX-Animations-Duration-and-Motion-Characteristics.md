# Executing UX Animations: Duration and Motion Characteristics

**Author:** Page LaubheimerPage LaubheimerFebruary 9, 20202020-02-09

**Topics:** Design Patterns, Accessibility

**Source:** https://www.nngroup.com/articles/animation-duration/

---

February 9, 20202020-02-09

Share

Animations in user experience can help by providing feedback and preventing disorientationor can be distracting, annoying, and dizzying. There are two dimensions for making animations a positive aspect of the user experience: their purpose and their execution.

In a previous article, we reviewed the first dimension — how animations can be used to make feedback noticeable and build the right mental models for a system.  In this article, we explore the second dimension: how to execute motion in a way that is natural, smooth, and visible, without causing frustration, discomfort, or significant delays for users.

It’s important to note that excessive use of motion and animation is anaccessibilityissue: animations with hard cuts between colors orflashingcan trigger seizures in epileptic users.Parallax,carousel-forwardinganimations, andscroll jackingcan make users withvestibular disordersdizzy or nauseated and trigger migraines.  Restraint is important, and you should respect those users who have set their browser or device to “reduce motion” by removing animations.

The purpose of the animation will typically dictate the type of animation or transition. Also, keep in mind how frequently users will encounter the animation: the more frequent the animation, the more subtle and shorter you’ll want it to be.

Thetriggeris the event that begins the animation. Oftentimes, the trigger will be a user action: a click or tap on a button, for example, might trigger a short loading animation.

YouTube: clicking on theClosed Captionbutton shows an animation as feedback.

Some more complex interactions can have subtle triggers — for instance, hovering over a video scrubber bar might fade in a preview image of that point in a video.

A gesture such as swiping might show a small animation in the direction of the swipe as a confirmation that the swipe gesture was recognized.

Sometimes, the trigger is different than the element that will move — for example, clicking a button might cause a modal popup to slide into view.  Or, the trigger can be the act of scrolling down a page, resulting in a traditional, preset animation or even in a parallax motion that moves the page as the user continues to scroll. (Becautiouswith parallax or scroll-jacking animations, as these are frequently frustrating, dizzying, and annoying.)

The Pixel 4 site shows multiple animations that are triggered by scrolling.  Some animations (such as the one at 2.5 seconds into this video) are triggered as soon as the user scrolls to the appropriate point on the page.  Other forms of motions (such as the black overlay box sliding on top at 11 seconds) are a parallax effect, where the movement speed is controlled directly by the user’s scroll speed, and will pause if the user stops scrolling part way through.

Some animations will involve only one moving item; others may consist of several elements moving together or with slight offset timing. In some cases, different parts of a single object will have different animations.

Warby Parker: An animation morphs thehamburger iconinto an X. The trigger is tapping the button. The moving elements have some subtlety: the hamburger menu’s top and bottom lines will rotate into the X shape, while the third, middle bar will fade out at the same time.

While animations can get very complex, there are a few standard properties that we might animate in a UX context: opacity, position, scale, color, shape, blur, and rotation.  While these won’t cover every possible animation, in combination, they are enough to easily communicate clear feedback to the user.

Google’s Material Designtoggle switchuses all the following animations to form a short (100ms) bit of feedback for amicrointeraction: button moves from one side to the other, the button color changes from gray to purple, and near the end of the animation, a purple halo fades in: it starts as a small, translucent purple circle around the button, quickly enlarges, blurs, and finally fades out.

When an object moves from one place to another around the screen, we need to decide its start and end positions, as well as its movement path —  an arc path often looks more natural than a diagonal path, which ignores the regularity of the layout. More than a century’s experience with animated cartoons has concluded that an object’s movements look right in an animation if theydon’tfollow the laws of physics. It’s beyond this article to discuss this topic in depth, but watch any movie of Wile E. Coyote chasing the Road Runner and you’ll get the basics.

Whenadding an item to the cartin Seamless, a small animated checkmark moves from theAdd to Bagto the cart in the bottom right. In this case, the movement path is an arc rather than a perfectly straight diagonal line. However, this animation is long and very likely to be annoying with repetition, as it is an exaggerated motion across the entire screen.

An object might change color or fade in over time to either suggest a change in state or be replaced by something new.  Changing the opacity is another common transition, but on a lot of platforms it will be computationally expensive (resulting in suboptimal performance and smoothness), especially when many elements change all at once.

Another common transition involves an object growing or shrinking.  Sometimes, we might transition a shape to another shape — for example, a circular button might expand to become a rounded rectangle card or a modal. In that case, we might use a transparent mask that expands in size and fades out in one motion.

iOS App Store: tapping on a card opens it to a full-screen element with additional details — an example of a growing animation.

The speed of an animation is hugely important for the usability  — too fast, and it’s hard to see or dizzying; too slow, and it becomes intrusive and feels like a delay to the user. In general, the duration of most animations should be in the range of 100–500 ms, depending on complexity and on how far the element is traveling. As a rule of thumb, look for the shortest time that an animation can take without being jarring. It is far more common for animations to be too long than too short.

Simple feedback animations, such as showing a checkbox or toggle switch, should be roughly 100 ms (0.10 seconds) in total duration.  This durationfeelsimmediateto users and creates the illusion of physically manipulating the object. 100 ms is at the lower end of perceivable motion, where italmostfeels like an instantaneous jump from one place to another, but is enough to make the feedback noticeable.

When animation involves substantial screen changes, such as when a modal window moves into view, a duration of 200–300 ms can be appropriate. The further an element has to move, the more important it is that it does so smoothly and non-jarringly (especially for people that are sensitive to motion, such as users with epilepsy or vestibular disorders).

At 500ms, animations start to feel like a real drag for users — they become cumbersome and annoying. In most cases, a range of 100–400 ms is appropriate, with 400ms being a very slow animation, to be used only for big movements across large screens.  Experiment with these values, as small changes like moving from 250 to 300 ms can feel very different. Note thatanimating objects appearing or entering the screen usually need a subtly longer duration than objects disappearing or exiting the screen: a popup window may take 300ms to appear, but only 200 or 250ms to disappear. (Remember, however, thatpopup windowsare problematic in many cases, and we discourage overusing them.)

Completely linear motion looks weird and unnatural to users.  An object that moves across the screen at the exact same speed the entire time feels less natural than one that subtly speeds up or down over time.  This impression has a lot to do with how objects move in the physical world, where we don’t often see things moving at a perfectly steady speed — they tend to accelerate and decelerate when they start and, respectively, stop moving. In order to make animations feel natural, we want to borrow from the real world (a principle known asskeuomorphism) and use slightly varied timing.

Easingis how we can specify how an animation feels. The most common varieties of easing are ease-in (where an object starts moving slowly, then speeds up), ease-out (where it slows down at the end), or the combination of both, ease-in-out (where the animation is fastest in the middle, but ramps up and down at the beginning and end).

Most frequently, you’ll want to use an ease-out animation, that starts quickly but slows down. This type of easing, which makes the animation feel responsive, but allows the eye time to focus on the element as it comes to rest.  Ease-in and ease-in-out are sometimes used for elements leaving the screen, but that sort of easing curve can feel unresponsive if the initial motion takes a little while to get going.

Linear motion is usually perceived as unnatural or awkward as compared to eased motion. The eased example uses ease-out when the boxentersthe frame, and ease-in when the boxleavesthe frame. While the terminology may seem confusing and contradictory (ease-out is used when somethingentersthe frame, and ease-in is used when somethingleavesthe visible area), ease-out on entrance means that the object slows down before it comes to rest, allowing the eye to predict where it will stop, while ease-in on exit means that the object speeds up as it moves out of frame, feeling like it’s accelerating away.

Note that easing is one of the most challenging aspects tocommunicateto an engineering team, as every platform has different ways of specifying an easing curve (e.g.cubic-Bezierformat is used in CSS, iOS and Android use named easing curves, Adobe After Effects uses incoming and outgoing percentage values). Speak with your development team so that you can specify these values in a way that they can be most easily translated into code.

If the engineering team doesn’t get meaningful, clear specs from the design team, there’s very little chance that it will build exactly what the designer had in mind. It’s not good enough to hand over a compiled video file from some video software and expect the developer to go frame by frame, trying to figure out all the subtleties of the easing curves.

Especially for complex animations with multiple movements happening all at once, a timeline is the most effective way to share animation characteristics with the engineering team (along with a noninteractive exported video of the animation, known asmotion comp). Show all the different elements that will move, with the type of properties that will change, and note the easing curves for each particular one.

We often say thatdetails matterfor UX quality. In animation, this saying is even more accurate than for other design elements. In fact, tiny details matter, because animation is an area of user-interface design where a tenth of a second will make a big difference to the user experience. Get it all right, and users may appreciate your animation as it enhances the learnability of the UI and adds a luxurious and put-together feel to the design. Get it half a second wrong (or even a tenth of a second too long), and the animation will feel jarring and annoying.

That’s why it’s worth paying detailed attention to the design of any animation to get it right and to get the specification communicated with sufficient clarity that it’s also implemented correctly.

Head, V. (2016)Designing Interface Animation. Rosenfeld Media.

Saffer, D. (2014).Microinteractions.O’Reilly Media.

Pratt, J., Radulescu, P., Guo, R.M., & Abrams, R.A. (2010).It's Alive! Animate motion captures visual attention.Psychological Science, 21, 1724–1730

Effectively communicate ideas and findings to managers, collaborators, and other stakeholders

Interaction