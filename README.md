# Hackithon 2025

> autor: Marek Šajner

Vítejte v repozitáři spjatém s přednáškami pro Hackithon. Tématem je rapidní prototypování fullstack aplikací, konvenčně zpracovávaný jako sadu dvou programů zvaných backend a frontend, kde backend je server, který zpracovává data, a frontend je prezentační vrstva.

Ukážu typickou kombinaci streamlit a fastapi pro zhotovení jednoduché aplikace, do které se nahrají datové sady, které se uloží na disk, zpracují a zobrazí jako graf. Uživatel bude moci upravit barvičky v grafu, a tuto informaci budeme zpracovávat pomocí databáze, ale nebude to komplikované a nebudeme psát žádné sql.

Předpokládá se dobrá znalost úplných základů programování

-------

Existuje asi tak milion alternativ ke streamlitu, jako například Shiny v R. Fajnšmekři frontend mohou napsat v reactu, nebo lépe ve svelte nebo s htmx. Backend doporučuji držet v pythonu, protože s tím vám mentoři mohou nejvíce poskytnout podporu, a zároveň se jedná o standardní nástroj pro zpracování dat.

## Spuštění

Musíte mít nainstalovaný python. Já používám `uv` pro výběr verze pythonu a instalaci balíčků, ale všechno snad jde nainstalovat s pomocí `pip install -r requirements.txt`

Dále musíte souběžně spustit backend(`uvicorn backend:app --reload`) a frontend(`streamlit run frontend.py`).

## Ukládání dat

Ani jedna služba by neměla mít žádná interně sdílená data. Co se stane v endpointu, zůstane v endpointu, zbytek jde do databáze. Ukládejte jen to nejnutnější a snažte se neukládat nic, když to aplikace vysloveně nevyžaduje. Nebojte se ukládat do souboru.

## Osnova

- Přečtu vám README.
- Představím vám streamlit.
- Představím vám fastapi.
- Ukážu vám dokumentaci.
- Předvedu vám technologická omezení streamlitu a jak ho obejít.
- Naimplementujeme něco do frontendu.

## Poznámky

V repozitáři [streamlit-workshop](https://github.com/nexovec/streamlit-workshop/blob/master/frontend/__main__.py) je ukázka routování pro streamlit pro složitější stránky ve streamlitu.



## Tipy na závěr

Očekává se, že budete používat git a ne si navzájem posílat různé verze souborů přes discord.

Mějte připravený vzor aplikace, ať můžete už po prezentaci začít pracovat.

Bylo by super, kdybyste za první ~2 hodiny měli rozhodnuto, co chcete dělat a měli již načtená data, ať vám mohou mentoři začít pomáhat.

Místo energeťáků si dejte silný zelený čaj se zázvorem a ženšenem. Neslaďte, z cukru dostanete crash. Dejte si ho do velkého hrníčku, ať nemusíte každých 5 minut chodit do kuchyně. PIJTE HODNĚ a pravidelně, klidně mějte časovač, trapný to není. Pijte méně na začátku a více později.
Pokud si musíte dát energeťák, udělejte to co nejdříve PO jídle. ABSOLUTNĚ ŽÁDNÝ ALKOHOL, nehodí se to ani pro soutěž, ani vzhledem k organizátorům.

Pokud je to možné, nespěte v místnostech, kde je ruch a svítí tam počítače. Zakryjte si na spánek oči, miřte na cca 6 hodin spánku v obvyklých hodinách, ideálně 1-7.

Mějte v každém bodě funkční program, nepřijďte na prezentaci s něčím, co nejde spustit. Kód vysdílejte veřejně.

-----

Z výše uvedených rad je jasné, že na hackathon se dá připravovat i dlouhodobě dopředu, brával jsem si s sebou nafukovací vak na spaní a polštář s dekou, půllitr, vlastní čaj, a dopředu jsem si upravil spací režim tak, abych vstal v poledne, a při začátku soutěže jsem pak měl v podstatě ráno, slabší jedinci si mohou obstarat melaton... tak třeba příště.
