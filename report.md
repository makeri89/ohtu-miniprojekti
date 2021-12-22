# Loppuraportti

## Johdanto

Tämä loppuraportti on kirjoitettu ketterän sovelluskehityksen käytänteiden innoittamana erityisinä "developer storyina". Tarjoamme alla siis neljä näkökulmaa miniprojektimme WinkVink-lukuvinkkisovelluksen kulkuun, yksi kultakin devaajalta. Lopussa tehdyt huomiot vielä kerätään yhteen.

Miniprojekti toteutettiin marras- ja joulukuussa 2021 yhteensä kolmen viikon mittaisen sprintin aikana. Devaajina toimivat Nora Heikkilä, Markus Kaihola, Timo Paananen ja Anssi Rajala.

## Developer Storyt

### Anssi

Yleisellä tasolla sanoisin, että projekti onnistui varsin hyvin. Ryhmän jäsenet tekivät hommansa moitteettomasti aikataulujen puitteissa ja lopputuotoskin oli pieneen sallittuun työaikaan nähden mielestäni tyylikäs. Selkeimpinä parannusehdotuksina tulevia projekteja silmällä pitäen voisi nostaa kolme asiaa: parempi yhteisymmärrys product ownerin kanssa user storyistä, lisää daily sprinttejä ja selkeämpi kommunikointi siitä, mitä kukin tekee ja missä vaiheessa omat hommat on menossa.  

Jälkimmäinen ongelma tuli esille ensimmäisen sprintin aikana ja siitä mainittiin ensimmäisen sprintin retrospektiivissä. Tämä kyseinen ongelma olisi kenties voitu välttää lisäämällä daily sprinttejä, joskin se olisi voinut syödä suuren osan tälle projektille rajatusta työmäärästä. Kolmas ongelma tuli esiin toisen sprintin asiakastapaamisen yhteydessä, kun havaittiin, että product ownerilla ja kehitystiimillä oli eri näkemys user storyjen toteutuksesta. Tämä olisi ehkä voitu välttää kirjaamalla user storyt selkeämmin heti alkuun.  

Teknisiä asioita pohtiessa kaikki tarvitut tiedot olivat suhteellisen hyvin hallussa jo ennen prosessia. Github actionsien kanssa joutui vähän taistelemaan, mutta muuten hommat sujuivat melko sulavasti. Ehkä tärkein opittu asia projektin aikana oli scrum-tyylisen projektityöskentelyn harjoittelu, jota en itse ollut aikaisemmin harrastanut. En sanoisi, että projektissa olisi ollut mitään ylimääräistä tai turhaa ja sprintissä kuusi tuntia tulee melko nopeasti täyteen uusia asioita harjoiteltaessa.

### Markus

##### 1. sprintti

Ensimmäisen sprintin aikana ongelmia tuli lähinnä sovelluksen saamisessa Herokuun, mikä lopulta onnistui muokkaamalla Herokuun menevä koodi omaan branchiinsa.

##### 2. sprintti

Toisessa sprintissä taskini olivat sovelluksen ulkoasuun liittyviä enkä kohdannut juurikaan ongelmatilanteita niihin liittyen. Haastavinta oli kenties muiden työn edetessä ulkoasun toiminnallisuuksien pitäminen ajantasalla.

##### 3. sprintti

Kolmannessa sprintissä sain taskeikseni kurssien lisäämisen implementoimisen. Tämä oli omista tehtävistäni haastavin, sillä Flask-sqlalchemyn dokumentaatio ei ollut eritysen kattavaa Many-To-Many -tietokantasuhteiden suhteen. Sain kuitenkin rakennettua toimivan rakenteen tietokantaan. Taskinani oli myös valmiin sovelluksen Herokussa toimimisen varmistaminen ja tähän keksin tällä viikolla paremman ratkaisun kuin ensimmäisellä, vaikka koodi yhä onkin omassa branchissaan.

##### Yleisesti

Kokonaisuutena projekti sujui sekä itseltäni että ryhmältämme hyvin, lopullisesta sovelluksesta löytyy paljon haluttuja toimintoja ja jokaiselle sprintille valitut taskit olivat työmäärältään sopivan kokoisia. Monesti osa taskeista jäi viime tippaan, jolloin tuli kiire saada tuote parhaaseen mahdolliseen kuntoon demoa varten. Tästä opin sen, että erityisesti ryhmänä töitä tehtäessä olisi hyvä tehdä taskit mahdollisimman ajoissa, jotta niiden mahdolliset ristiriidat muiden taskien edetessä ehditään ratkoa ajoissa.

### Nora

Sprintti 1 omalle kohdalle sattui suurimmaksi osaksi yksintyöskentelyn haasteet, mutta etätyöskentely sujui muuten hyvin ja kommunikoimme tiimin kanssa Discordin kautta.

Sprintti 2 ongelmaksi koitui taas yksintyöskentelyn haasteet, sillä minulla ei ole kokemusta testaamisesta, mutta onneksi tiimiläisiltä sai tähän apua. Jotkut taskit myös jätettiin viime minuuteille, mutta Sprintti 3 kaikki suoriutui erinomaisesti.

Projekti sujui hyvin, sillä tiimi oli joustava ja projekti oli aikaan nähden sopivan kokoinen. Seuraavaan projektiin voisi sopia tiimin kesken ajan, milloin työskenteltäisiin yhdessä livenä. Mikä helpottaisi paljon työskentelyä ja voisi myös kokeilla parityöskentelyä.

Omalta osaltani voin sanoa, että opin ainakin testaamisesta enemmän sekä projektityöskentelystä.

### Timo

Projekti oli kokonaisuutena onnistunut ja opetti paljon Scrum-menetelmäkehyksen käyttämisestä ohjelmistotuotannossa. Työskentelyn näkökulmasta haasteita aiheutti ensin liian niukka kommunikaatio tiimiläisten välillä. Tämä kuitenkin huomattiin heti 1. sprintin aikana, ja korjattiin retrospektiivissä käydyn keskustelun jälkeen mallikkaasti (vähän saatettiin kyllä taas lipsua 3. sprintin loppua kohden). Opiskelijoiden aikataulut ovat tunnetusti hankalasti yhteensovitettavissa, kun eri opintojaksot sekä muut elämän velvollisuudet asettavat reunaehtoja yhteisten palaverien järjestämiselle. En esimerkiksi pitäisi sitä parhaana käytäntönä, että (kerran viikossa/sprintissä pidettävä) Daily Scrum on sunnuntai-iltana, mutta muutakaan (yhteistä) vaihtoehtoa ei ollut. Tiimi oli kuitenkin joustava ja suoriutui prosessin asettamista haasteista hyvin.

Tekniikan näkökulmasta ongelmia riitti, ei kuitenkaan ylitsepääsemättömiä. Automaattisten testien kirjoittaminen käyttämämme Flask-sovelluskehyksen päälle osoittautui yllättävän mutkikkaaksi. Vaikka miniprojektin ohjeistuksessa olikin opastettu, ettei uusien teknologioiden opiskeluun ole välttämättä syytä käyttää aikaa, tein tätäkin (hallitusti) ja pidin sitä lopulta hyvänä päätöksenä. Ratkaisu yksikkötestien tekemiseen löytyi nimittäin Flask-Testing -kirjastosta. Lisäksi koin mielekkäänä XPath-kyselykielen syntaksin opiskelun siinä määrin, että saan vastaisuudessakin Robot Frameworkin (yhdessä Selenium-kirjaston kanssa) navigoimaan webbisivulla tehokkaasti, vaikka tietysti tämän miniprojektin puitteissa XPath-kontribuutioni tiivistyikin lopulta yhteen koodiriviin.

3. sprintin lopussa huomasin testikattavuuden laskeneen, ja tässä tapauksessa kyse on sekä prosessi- että tekniikkaongelmasta. Projektimme definition of done (valmiin määritelmä) oli mielestäni hyvin laadittu. Siinä testikattavuudelle oli annettu selkeä numeroarvo. Meillä oli myös hyvin laadittuja järjestelmätestejä, jotka toimivat erinomaisina regressiotestien välineinä (ts. ne hajosivat usein). Kuitenkin, koska järjestelmätestit käyttivät (web)sovelluksemme ymmärtämiä http-pyyntöjä testaamisessa, ei testikattavuutta mittaava Coverage laskenut testattuja koodirivejä oikein. Kirjoitin pikaisesti uusia testejä, jotka testasivat täsmälleen samoja asioita kuin järjestelmätestit, mutta jotka sentään kirjautuivat testikattavuusraporttiin. Pääsimme takaisin itse asettamamme testikattavuusrajan yläpuolelle. Omassa toiminnassanihan ei ollut järkeä: järkevämpää olisi kai ollut muuttaa valmiin määritelmää tai poistaa väärin kirjautuvat moduulit testikattavuusraportista. Laskin kuitenkin, että palaveroiminen aiheen tiimoilta olisi syönyt helposti enemmän aikaa kuin tusinan testitapauksen kirjoittaminen eikä kuuden tunnin sprinttityöaika antanut paljoa pelivaraa, tässä tai muissakaan tapauksissa.

## Loppuyhteenveto

Kertauksena kehitystiimi piti siis projektia onnistuneena: kaikki työskentelivät pätevästi ja hommat saatiin maaliin aikataulussa (vaikka välillä vain juuri ja juuri). Lopputulosta pidettiin juuri sopivana siihen nähden, miten paljon neljän devaajan voi olettaa saavan tehtyä viikon sprinteissä, joissa työskentelyaika on rajattu kuuteen tuntiin. Teknisiä ongelmia oli, mutta kaikesta selvittiin. Isoimpana prosessinhallinnan asiana nostettiin esiin kommunikaation tärkeys niin devaajatiimin kuin sidosryhmienkin (tässä: product owner/ohjaaja) välillä. Myös työn aikataulutuksen merkitystä painotettiin: teknisesti vaikeisiin asioihin kannattaa tulevissa projekteissa tarttua kiinni heti, jotta aikaa jää myös mahdollisten yhteensopivuus- ja yhteensovittamisongelmien ratkomiseen.
