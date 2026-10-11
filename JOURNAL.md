# Where I take this Idea?
In Uzum (Uzum is marketplace in Uzbekistan) I find RGB Lamp and I understand, I need this! I find many thinkgs and I need them but the best one for build I mind is RGB Lamp. And if you read this please answer to this question: **"Can I built 1 my project and other projects I just farm coins and spend this coins in shop without building?"** Because I find PC grant (119c = $100 pc grant) and I really want to win this grant. I haven't GPU this big problem to work in 3d editors and CPU's GPU haven't CUDA. Okey, Let's start journal

# October 7: Doing PCB for RGB Lamp
PCB I always do in KiCad so I open KiCad and created new project. The idea is wireless RGB Lamp with 3000mAh batery with Type-C connector. White color case, OLED display, 2 mechanic buttons for editing color. Not somethink hard but it performs its function. Oh I forgot, the main microcontroller is RGB diodes I add 4. In the PCB editor in KiCad I did circle PCB because I want Circle case. And That's enough what I did in this day.
<img width="1065" height="663" alt="Снимок экрана 2026-10-10 174252" src="https://github.com/user-attachments/assets/03fee8ba-48bc-4740-9f9d-f45c5926a74c" />
**Total time spent: 1 hour**

# October 8: Complating PCB and starting case
After PCB I started to do case At fitst I add plane and made circle form plane. Then I extridude this to arrive 3d model from 2d. I did hole in this shape for batery and PCB and for display(Later I add holes for 2 mechanic bottoms). I didn't do a lot of things because I spent only 0.5hours
<img width="782" height="526" alt="Снимок экрана 2026-10-12 000036" src="https://github.com/user-attachments/assets/698bb732-28e7-48d1-9f0c-d9c7cafd8877" />
**Total time spent: 0.5 hours**

# October 10: Complating the Case
In this day I complaye the case  and edited PCB in KiCad. Because the place of microcontrollers was not cool. And I fix it. I add some text in Edge cuts layer and replace microcontrollers. Then I started complating case. At first I did Top case for lights and add holes for 2 buttons (SW_Pushes). Then I optimize the case and delete unnecessary poligons. It's good to convert to step soon, because Blender can't export step files. I use online convertors. To the best visual I add light point in RGB diodes and switch to Cycles mode in Render options and just see this...
<img width="1920" height="1080" alt="FINAL" src="https://github.com/user-attachments/assets/5d147a2a-42f1-4e33-b4f4-245dc4820c34" />
**Total time spent: 1.7 hours**

# October 11: Writing Firmware
Oh firmware the borrest prosses for me but I did this. At first I mind this functional: if I press 2 bottoms I can switch to next color or next color mode. I add 12 colors and 2 mods. Rainbow and Heart beating. I think this is cool mods. But I like Aqua with white tone more. And I did in firmware the next functionals too: If you don't press buttons again in 15 secods display gets off, and if you double click you can edit brightness and that's all what I did.
<img width="1919" height="791" alt="Снимок экрана 2026-10-12 001326" src="https://github.com/user-attachments/assets/2fb5be91-dded-446b-997e-05dc343ff642" />
**Total time spent: 2.6 hours**
