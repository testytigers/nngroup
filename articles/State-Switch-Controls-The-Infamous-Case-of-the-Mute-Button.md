# State-Switch Controls: The Infamous Case of the "Mute" Button

**Author:** Raluca BudiuRaluca BudiuOctober 18, 20202020-10-18

**Topics:** Application Design, Design Patterns, Interaction Design

**Source:** https://www.nngroup.com/articles/state-switch-buttons/

---

October 18, 20202020-10-18

Share

In a recent WebEx meeting with a client, I panicked thinking that I couldn’t turn my microphone on. I was supposed to give a 6-hour presentation — how was I going to do it if I couldn’t even unmute myself? I kept clicking the crossed-microphone icon, but the microphone stayed crossed whatever I did.

Here’s a screenshot:

In my panic, I was completely oblivious at the change in the icon color! Eventually, I discovered that, even though the microphone was crossed in both states, the red color of the icon was meant to signal that the button was active and I was muted.

I have seen users fall prey to this issue many times. TheMutebutton is used to switch between two system states (MutedandUnmuted), but the problem is that users cannot easily tell what the current state is and what they are switching to. (Also, contrary tobest practices in icon design, in the WebEx implementation, there is no text label for theMutebutton.)

In a situation where users can move between 2 possible states (let’s call themonandofffor simplicity), there are two bits of information that are relevant to the user and, while related, are not identical:

An obvious way of implementing them would be to have two different UI elements: a state indicator and a change-state button. For example, in the Tesla app, theControlsscreen takes this approach: you have both a state indicator to show you that the car is locked and anUnlockbutton. Tapping the state indicator does nothing, but tapping the control unlocks the car.

However, if you have a 2-state system, the current state and what will happen next are complementary. In other words, one may assume that the two pieces of information (state and what happens next) could be conveyed through a single control — a switch-state button. That’s because, if users knew one, (in theory at least) they could infer the other (if you know that your next state will beoffthen you can infer that the current one ison; or, if you know that your current state ison, you can infer that your next one isoff).

However, remember thatany type of inference takes time and cognitive effort, and often people are under the time pressure to respond quickly.  If I am trying to unmute myself, everybody is either waiting for me or ignoring me and moving the conversation along, so I don’t have time to pause and think about the interface or make inferences.

Sometimes, however, the state can be easily determined based on other signals. For example, in a video player, there is just one control (thePlaybutton) and it indicates future state. There are enough signals though to figure out that the video is playing — the user can hear the video or see the changes in the image on the screen.

If you decide to use a single control to indicate both state and what will happen next, how should that control be labeled?

There are two alternatives that could be considered in that situation:

This is the standard recommendation for button design. Specifically, a site-registration button will be calledRegisterand a submit button for an ecommerce checkout form will be calledPurchaseorPlaceorder.

If a button is used to switch between two states, to follow this recommendation it should also change label, like in the Tesla example above or in the OBS example below.

If there is no text label (presumably because the icon is clear enough), then the icon should change depending on the state it moves the system to. A classic example is the interplay between thePlayandPauseicons seen in the YouTube example above and present in most video players.

2. The button communicates the active state using a shadow. This is what used to happen in real life to on/off type of buttons: when you pressed them, they did not change label, but “sunk down.” In UI design, to capture that metaphor, designers usually add a shadow to indicate that the button has been pressed and now it’s active.

Understanding this design clearly depends on the shadow being recognizable as a signifier for active state. This design should NOT rely onthe user remembering the color of the button in its two statesand knowing which color stands for active — in order for it to work, it should be absolutely evident that the active state is a pressed button, a feat that is sometimes hard to achieve in aflat-designworld.

Let’s go back to the WebEx example. In retrospect, we can see that WebEx used a single control to indicate both the current state and what will happen next and implemented the second design solution — signaling active state. Unfortunately, the red color as a signifier for active state was a poor design choice for several reasons:

In the absence of a clear indicator of active state, the user is left to rely on the button label to decide what’s happening and, with the icon label unchanged, that will simply cause confusion.

By the way, The Phone app on the iPhone uses the same implementation — the only difference is that it is more consistent than WebEx and deploys a white fill to indicate active state. Even with those adjustments, it’s hard to infer the active state of a button.

So, what is the overall recommendation for state switching buttons that double as state indicators? The safest solution is to use 2 UI elements, one for current state and another one for the switch-state action, like in the Tesla example.

If you want, you can combine the two in a single control like Zoom does. ItsMutecontrol has two separate components:

Clicking on either will change the state.

A newer version of WebEx has moved to the same design.

Remember, your goal with an on–off control is to make sure that users quickly understand both:

Assess the two states that the system will go through.

Components, design patterns, workflows, and ways of interacting with complex data

Interaction