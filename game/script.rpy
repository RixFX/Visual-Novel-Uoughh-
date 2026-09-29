define rimuru = Character("Rimuru Ethelind", image="rimuru")
define liquorice = Character("Liquorice Baal", image="liquorice")
define n = Character(None)
define receptionist = Character("Receptionist")
define pegi = Character("Ms. Pegi")
define catt = Character("Catt", image="catt")

image side rimuru = Transform("rimuru", zoom=0.8, xoffset=150, yoffset=600)
image side liquorice = Transform("liquorice", zoom=0.8, xoffset=-80 ,yoffset=850)
image side catt = Transform("catt", zoom=0.8, xoffset=-80, yoffset=850)

define fadehold = Fade(0.5, 1.0, 0.5)

transform rimuru_pos:
    zoom 0.8
    xalign 0.2
    yalign 1.0
    yoffset 150

transform liquorice_pos:
    zoom 0.8
    xalign 0.8
    yalign 1.0
    yoffset 150

transform catt_pos:
    zoom 0.8
    xalign 0.5
    yalign 1.0
    yoffset 150

style default:
    font FontGroup().add("fonts/DiarioDeAndy-L3ADy.otf", None, None).add("DejaVuSans.ttf", 0x0021, 0x003F, target=None, target_increment=False)


label start:

    scene bg

    show rimuru at rimuru_pos
    show liquorice at liquorice_pos
    with fade

    play music "audio/music/Sculpture-Garden_Looping.mp3" fadein 2.0

    liquorice "First spirit hunt in Shuas! Are you looking forward to spirit hunting Rimuru?"

    rimuru "Mmhm! I'm super excited!"

    play music "audio/music/boss.ogg" fadein 0.5

    show catt at catt_pos with dissolve

    catt "Hi guys. Did I mention I'm from Malaysia!?"

    liquorice "RIMIRU!! LOOK OUT!! IT'S CATT!!!!"

    rimuru "OH NO!!!!!!!!! OH NO!!!!!!!!!!"

    python:
        buttons   = make_qte_buttons(config.screen_width, config.screen_height, count=3)
        qte_multi = QTEMultiDisplayable(buttons)
        results   = renpy.call_screen("qte_screen", qte_multi=qte_multi)
        hits      = results.count("hit")

    hide catt with dissolve

    play music "audio/music/Sculpture-Garden_Looping.mp3" fadein 2.0

    if hits >= 2:
        rimuru "Phew... that was close. uouugghh...."
    else:
        rimuru "UOUGUHHHH"

    liquorice "That's great to hear!"

    rimuru "Narration about how its one of her first spirit hunts and smth smth mention her camera."

    liquorice "The director asked me to come by and investigate the aquarium."

    liquorice "They didn't disclose any specific details but are certain that something supernatural has been haunting their halls these past few months."

    liquorice "They don't want any inconvenient situations to happen during their upcoming sea show"

    liquorice "So we'll be looking into these strange occurrences today."

    n "Rimuru glances at the clock, frowning upon seeing the time."

    rimuru "But... did we have to wake up so early?"

    liquorice "If you want to take spirit hunting seriously, you should get used to waking up at strange times."

    liquorice "The show is only a few days away, and they are expecting a lot of people to show up to see the orcas, which means if there really is a Spirit, it would pose a serious risk to everybody."

    liquorice "So many lives could be on the line if we don't at least check it out."

    rimuru "I guess that's true..."

    n "..."

    liquorice "So..."

    liquorice "Rimuru, have you ever been to an aquarium before?"

    rimuru "Yeah, when I was younger."

    rimuru "My parents would take me sometimes, when we still lived here. But then my little sister was born and we moved to the boring big city."

    scene business with fadehold

    liquorice "Alright. Here we are. insert auriumname, townname biggest attraction since"

    rimuru "!"

    n "Rimuru looks excitedly out of the window only to see a completely regular aquarium building."

    rimuru "..."

    liquorice "What's wrong?"

    rimuru "(What?? This place is supposed to be haunted?? It looks so normal and boring..  My horror blog aesthetic is ruined!)"

    rimuru "No, No, it's just that.."

    menu:
        "Be Honest":
            jump be_honest

        "Play It Down":
            jump play_it_down

    return


label be_honest:

    rimuru "This place looks so normal!"

    rimuru "I mean If this place was actually haunted couldn't there at least be some mysterious fog or thundering in the distance or it could at least look a little run down?"

    liquorice "Youth nowadays.."

    liquorice "Don't you know that the safest places are the most dangerous?"

    liquorice "You let your guard down and you're more susceptible to sneakier spirits."

    rimuru "Ughhh... Fineeee..."

    jump aquarium_frontdesk


label play_it_down:

    rimuru "The building looks normal, are you sure this place is haunted?"

    liquorice "Even if a place looks normal you never know what lurking below the facade."

    liquorice "If anything, the safer something looks the more dangerous it is because you let your guard down."

    jump aquarium_frontdesk


label aquarium_frontdesk:

    n "Liquorice sighs, looking back to the aquarium."

    liquorice "The director should be waiting for us, let's go."

    scene frontdesk with fadehold

    receptionist "Welcome to Ce{font=DejaVuSans.ttf}ò{/font}thach Aquarium, how may I help you?"

    liquorice "We are here on request of Ms. Pegi to investiga-"

    receptionist "Ah! guests of the director? Then that can only mean.. May I see your ID please?"

    liquorice "Oh- (small pause here) Yes, of course, here you go."

    receptionist "Thank you! And what about the little lady?"

    rimuru "Little lady?"

    liquorice "She's my personal student."

    receptionist "I see. Give me a moment to inform the director about your arrival."

    receptionist "Ms. Pegi, Ms.Baal and her student are here. (...) Mhm.. (...)  Okay. We'll be waiting."

    receptionist "The director will be with you shortly, in the meantime why don't you take a look around. Free of charge of course."

    liquorice "Okay, thank you. Let's go, Rimuru."

    rimuru "Okkkkkkkkkk"

    scene clickable_aquarium_post_frontdesk with fadehold

    n "insert clickable aquarium and the end text when finished clicking"

    liquorice "Hey Rimuru, you were here before right? What was the last fish you saw here?"

    rimuru "I don't know... That was 8 years ago, I barely remember. There were way more beautiful fishies when I was a kid."

    liquorice "We can go check if they're still here. What were the names?"

    rimuru "Mmm.. I doubt they're still here. I looked around and they don't have any Betta Fish any more.."

    liquorice "Betta Fish? Maybe we can ask around."

    rimuru "It's a colourful Southern Eastern Line fish that isn't from around here. They probably gave it to some other huge aquarium outside of Menstron."

    liquorice "We won't know until we ask!"

    rimuru "Okkkk...."

    scene rimuru_interest with dissolve

    rimuru "What's that over there?"

    liquorice "Hm... looks like that place is under construction?"

    liquorice "Maybe we can ask later or check when the director is here.. What about we go look at the other fishes?"

    rimuru "Mmm.. Stone fish."

    scene aquarium_director

    pegi "Greetings Ms. Baal, thank you so much for coming by. I hope I didn't keep you waiting for too long."

    liquorice "Not at all, Ms. Pegi. We were just chatting and enjoying the exhibits."

    pegi "I'm glad to hear that."

    pegi "Huh, (small pause) Oh, the student. Wait, who are you though?"

    rimuru "I'm Rimuru Ethelind, aspiring horror blogger and future spirit hunter!!"

    pegi "Ah, ahaha.. ha.. That sounds um, wonderful. You were talking about our betta fish just now right?"

    pegi "If that's a fish you'd like to see, then I'm very sorry to inform you both that we had to close down their tanks for the unforeseeable future."

    rimuru "(This is so boring, this isn't horrific at all. Ugh nobody wants to see this on my blog, not even I do!)"

    rimuru "(Hm... But the restriction area looked gloomy.. If I could just manage to sneak away for a bit and take a few pictures, maybe I can get a few good angles of the spirit.)"

    liquorice "That's ok! We'll be able to visit them another time when we finish the job. Where should we discuss this matter?"

    pegi "Come with me to my office. We don't want any prying ears to snoop into our private conversation."

    liquorice "Okay."

    liquorice "Lead the way."

    rimuru "Insert timed choice to slip away."

    menu:

        "Slip away.":
            pass

        "Stay Behind Ms. Baal.":

            rimuru "..I shouldn't walk away. I'll stay behind Liquorice Baal for now.."

            jump aquarium_directors_room


label aquarium_directors_room:

    pegi "Here have a seat."

    pegi "Coffee?"

    liquorice "Gladly."

    rimuru "No thanks."

    pegi "Okay, more for me!"

    pegi "We'll cut to the chase! Over the past few months the aquarium has been getting way more reports of accidents and incidents."

    pegi "First I thought that maybe we were getting careless and we were in need of more competent management and staff, especially in the old parts of the aquarium, but the incidents were getting more and more uncanny as they went on, for example.."

    pegi "Reports of flying fish in the halls the moment somebody fell over a \"tank leak\", somebody seeing an apparition after someone got pushed into the open water at the sea show, schools of fish got sick at the same time without us being able to pinpoint the source, so we had to close multiple tanks and treat them in the quarantine zone. The equipment immediately failed after months of checking on the equipment to get them under regulation."

    pegi "There were even more incidents I haven't mentioned, but I don't have to tell that information to you."

    pegi "What I can tell you is that the reports have been consistent with every witness and we closed multiple rooms based on the most reported sightings."

    pegi "We then hired you to investigate whether or not the rooms are haunted or in need of maintenance, or both."

    liquorice "Seems simple enough!"

    rimuru "Room investigation horror story!"

    pegi "(...?)"

    pegi "That's great to hear! Now that you're both caught up, take these."

    liquorice "Badges?"

    pegi "Yes they will allow you to walk around the facility unbothered, should you need anything, just ask the staff, but keep it discreet and inform me of anything related to spirit activity directly, no need to make uninvolved people worry after all."

    pegi "Now, shoo shoo, I have other business to attend to."

    scene aquarium_two_zones with fadehold

    liquorice "Now that we can move around the aquarium with the aquarium badges, where would you like to go first?"

    menu:
        "Regular Zones":
            jump Regular_Zones
        "Restricted Areas":
            jump Restricted_Areas


label Regular_Zones:

    liquorice "Regular Zone Stuff dialogue"

    return


label Restricted_Areas:

    liquorice "Restricted Areas Stuff dialogue"

    play sound "audio/sfx/Interior-Door_Close.mp3"

    return