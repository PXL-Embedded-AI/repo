Vis Spectroscopie van vloeistoffen: implementatie op basis van het theoretisch onderzoek issue #24

Testmodel Vis Spectroscopie
Design, constructie en implementatie door: Eduardo L. Bemelmans
Onderwerp: Spectroscopie van vloeistoffen binnen het visueel spectrum: implementatie, ontwerp, constructie en labo.

10/04
Constructie spectroscopiemeter

Gebruikt materiaal:
- MDF
- Aluminium L-profiel
- OpenMV camera
- Diffraction grating van een DVD-RW
- Kartonnen doos (voor versie 1)
- Schoenendoos (voor upgrade 1)

Gereedschap:
- Bouten- en moerenset M3
- M3 houtboren
- Schroevendraaier set
- Minitang
- Kolomboormachine
- Handzaag
- Professional art knife
- Lijmpistool

Extra benodigdheden:

- Isopropanol
- Plastieke handschoenen (ongepoederd)
- Veiligheidsbril
- Werkhandschoenen
- Tissues



De openMV camera werd gemonteerd op een MDF plaatje. Deze dient als draagblok en werd gemonteerd op de basis MDF plaat. De MDF platen zijn op maat gezaagd. De openMV heeft twee mounting holes, waardoor het schuin op het draagblokje zit. Dit geeft geen problemen verder, maar de PCB van de openMV camera is nu eenmaal op deze wijze geconstrueerd.

![IMG_20200410_165109432](https://user-images.githubusercontent.com/48355782/80476565-d9083380-894a-11ea-8921-5d4775ae7d89.jpg)

Een stukje van de aluminium L-profiel verbindt het draagblokje van de camera en de basisplaat. Hierdoor kan de hoek van de camera afgesteld worden.  

![IMG_20200410_165142826](https://user-images.githubusercontent.com/48355782/80484592-41114680-8958-11ea-92d7-306bebb7e896.jpg)

Alle verbindingen werden gerealiseerd met M3 bouten en moeren.

![IMG_20200410_193814553](https://user-images.githubusercontent.com/48355782/80485266-5d61b300-8959-11ea-9084-8bb5ebef407a.jpg)

Op basis van het onderzoek van diffraction gratings met een camera (issue #20) is er een diffraction grating genomen van een DVD-RW. Deze is met een lijmpistool geplakt op de basisplaat. Het nadeel hiervan is dat de diffraction grating niet verwisseld kan worden. 

![IMG_20200410_193814553](https://user-images.githubusercontent.com/48355782/80485721-3c4d9200-895a-11ea-829c-6d44951e1aa0.jpg)

![IMG_20200410_193820672](https://user-images.githubusercontent.com/48355782/80486143-f644fe00-895a-11ea-8638-71417a525e46.jpg)

Deze assembly werd daarna in een gewone kartonnen doos geplaatst. Daarna werd er een nog een spleet gecreëerd waardoor een selecte lichtbundel van de lichtbron binnen de doos komt. De resultaten waren niet bevredigend, omwille van het feit dat de doos niet voldoende verduisterd was.

![IMG_20200428_142235132](https://user-images.githubusercontent.com/48355782/80487401-06f67380-895d-11ea-8128-7ba4da74d0d9.jpg)

Conclusie deel 1:
De doos heldert teveel mee op waardoor de resultaten teleurstellend zijn. Er moet een nieuwe doos ontwikkeld worden. 

25/04 tot en met 26/04
Upgrade 1 spectroscopie meter:

De kartonnen doos werd vervangen door een schoenendoos. Deze werd zwart gesprayed met spuitlak. Deze is echter glanzend, waardoor het licht nog steeds gaat reflecteren. 

![IMG_20200425_160743381](https://user-images.githubusercontent.com/48355782/80487973-f1357e00-895d-11ea-9c17-84983c219c05.jpg)
 
![IMG_20200425_160750071](https://user-images.githubusercontent.com/48355782/80487983-f5fa3200-895d-11ea-8a0f-ec311f30765e.jpg)

Een nieuwe basisplaat werd vervaardigd en ook zwart gesprayed. Echter heeft deze aan één kant, één laagje glanzende spray, waardoor deze er meer mat uitziet.

![IMG_20200425_194549342](https://user-images.githubusercontent.com/48355782/80488092-1f1ac280-895e-11ea-809d-22efe5bc9603.jpg)

Deze opstelling werd daarna geplaatst in de schoenendoos. Ook bij deze doos werd een spleet gecreëerd om een select deel van de lichtbron binnen de doos te laten dringen. De diffraction grating heeft een draagplankje gekregen met twee mouting holes. Eén van deze mounting holes is verbonden met de basisplaat waardoor de diffraction grating, net zoals de camera, verstelbaar is.

![IMG_20200425_194600469](https://user-images.githubusercontent.com/48355782/80488298-6739e500-895e-11ea-9964-39a784a07e25.jpg)

Het resultaat was al een grote verbetering zoals te zien is in de volgende figuur. Het spectrum komt van de flashlight van een smartphone (G7+ Motorola). Deze smartphone heeft een warm witte LED en bevat dus het hele spectrum. Deze is echter niet volledig te zien.

![94420857_170706514159016_5988753950587748352_n](https://user-images.githubusercontent.com/48355782/80490172-40c97900-8961-11ea-845e-32d7b6cdd206.jpg)

Na inspectie van de constructie bleek dat het invallend licht de diffraction grating niet bereikte. Het invallend licht scheen erlangs. De basisplaat werd aangepast zoals te zien is in de volgende afbeelding. Er werden mounting holes voor de diffraction grating en de camera toegevoegd om te moduleren in de positionering. De camera kan dus verder of dichterbij de diffraction grating geplaatst worden. 

![IMG_20200428_150353971](https://user-images.githubusercontent.com/48355782/80490707-12986900-8962-11ea-8e48-a83127988539.jpg)

Het testen van deze constructie gaf meteen zinvolle resultaten die conform de theorie van spectroscopie zijn. Onderstaande afbeeldingen zijn screenshots van de uitvoer van de spectroscopie meter.

Screenshot 1: spectrum van de flashlight van de G7+ motorola smartphone
![OpenMV-Phone](https://user-images.githubusercontent.com/48355782/80491351-e16c6880-8962-11ea-8695-7e1911a677d8.png)

Screenshot 2: spectrum van een rode LED
![OpenMV-RedLED](https://user-images.githubusercontent.com/48355782/80491354-e204ff00-8962-11ea-94c7-321e090bbe41.png)

Screenshot 3: spectrum van een witte LED
![OpenMV-WhiteLED](https://user-images.githubusercontent.com/48355782/80491355-e204ff00-8962-11ea-8aec-d222bda8cf69.png)

Screenshot 4: spectrum van een blauwe en een witte LED
![OpenMV-BlueAndWhiteLED](https://user-images.githubusercontent.com/48355782/80491358-e29d9580-8962-11ea-8dfc-d01dd708415d.png)

Screenshot 5: spectrum van een blauwe LED
![OpenMV-BlueLED](https://user-images.githubusercontent.com/48355782/80491359-e29d9580-8962-11ea-859f-2f7296a63cfd.png)

Het valt op dat het spectrum van de blauwe LED cyaan en groen bevat. Deze LED is dus niet van hoge kwaliteit. Echter een LED van hogere kwaliteit (zoals de rode LED), zal het spectrum weergeven van de respectievelijke kleur. 

De volgende afbeelding is een screenshot van het spectrum van Davidoff cool water parfum. De G7+ motorola smartphone schijnt doorheen de blauwe fles. Het licht wordt dus gefilterd door de doorzichtige fles.

![OpenMV-DavidoffCoolWaterParfum](https://user-images.githubusercontent.com/48355782/80494470-f8ad5500-8966-11ea-9059-d6feff24cbed.png)

Davidoff coolwater parfum fles

![IMG_20200428_153752527](https://user-images.githubusercontent.com/48355782/80494346-df0c0d80-8966-11ea-9322-814c253e64ab.jpg)

Future work:

De lichtbron moet vastgemaakt worden aan de doos zodanig dat het spectrum zich meteen juist toont. Nu is de positie van de lichtbron variabel waardoor het spectrum van intensiteit veranderd. Als de lichtintensiteit te groot wordt, licht de inhoud van de doos mee op. De doos reflecteert nog vanwege de glanzende lak. De rode PCB van de camera is ook zichtbaar als de lichtintensiteit te sterk is. 

Conclusie na de upgrades:
De resultaten zijn bevredigend, maar nog niet volledig juist. De implementatie is voldoende geslaagd om het project verder te zetten. De resultaten tonen aan dat Vis spectroscopie van een vloeistof plausibel is met minimalistisch materiaal.









