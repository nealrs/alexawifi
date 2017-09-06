# Alexa WiFi Skill

You know what sucks? Remembering your wifi password and telling other people what it is. Seriously, I have almost no idea what mine is. So why not use Alexa to store & retreive it?

When you invoke this skill `Alexa, open Wifi`, it will spell out your SSID & Wifi Password, character by character. And it'll also report it in the Alexa app.

To get this working, you'll need to:

1. Set up an Amazon & Alexa dev account.
2. Rename `.env_example` to `.env` and replace the values with your SSID & wifi password.
3. Deploy this bad jackson to Heroku.
4. Create a new Alexa Skill (type: Custom).
5. In the Interaction Model tab, copy & paste the text from `IntentSchema.json` & `SampleUtterances.txt` into the first and third text areas.
6. In the Configuration tab, paste your heroku url (must be https)
7. In the SSL Certificate tab, select the second option (subdomain / wildcard)
8. In the Test tab, type something (anything really) in the utterance field of the Service simulator text field.
9. Click "Ask" and view the response JSON. Click Listen to hear the reponse. And Scroll down to see a mockup of the Alexa app card.
10. If you like what you see, try it IRL with your Echo.

**While you _can_ submit the skill for certification, you don't have to and probably shouldn't.**