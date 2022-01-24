# msi_k8s
Domača naloga za k8s

## Uporaba
Preko git clone ali Download zip dobiš potrebne datoteke. Premakni se v ustezno mapo ter zaženi spodnji ukaz, ki bo buildal in zagnal vse potrebno.
To počneš v izbrani VM in potrebuješ imeti naložen kubernetes in minikube. Če si študent pri predmetu MSI imaš med gradivom tutorial kako to narediti.

```bash
cd msi_k8s

# da ima script.sh ustrezne pravice
chmod +x script.sh 
# poženeš
./script.sh
```
Potem traja nekaj časa, da se vsi image-s potegnejo dol. 
Lahko preveriš kaj se dogaja v drugem terminalu z ukazom `kubectl describe pods -n <name_veje>`. Pri meni je bil recimo <name_veje> `default`. Lahko pa odpreš dashboard v brskalniku z ukazom `minikube dashboard` v terminalu.
Da dobiš ip strani odpri dashboard in pod ingress najdeš spletne strani ali pa v terminal vpiši `minikube tunnel` in vnesi sudo geslo. 

Na koncu ugasni z `minikube stop; minikube delete`. Tako se tudi izbriše kar si delal.

Za več navodil si poglej posnetka v mapi posnetki.
    
### Postopek
1. http://<ip>/create_db Če ne dela, samo naloži ponovno. 
2. http://<ip>/ Tukaj lahko uporabljaš aplikacijo.

Kadarkoli lahko greš na http://go/

## Težave pri programiranju
    
Zelo veliko težav sem imela Ingressu in kako povezati backend v flasku s frontendom. 
- Prvo je bil da localhost verjetno ni več prav, tako da sm rabila dodati v frontend javascript ip strani, da ve kam pošiljati POST pakete.
- Mi se mi uspelo povezati v katerkoli fukcijo v backend flask aplikaciji. To mi je potem uspelo rešiti tako da ingress poveže vse aplikacije na '/'
- Potem mi ni uspelo povezati se s pravilno funkcijo v backend flask aplikaciji. Ker mi je uspelo se povezati na '/' sem vse potrebne funkcije premaknila v '/' pot. Ker sem imela dve pomembni funkciji v web aplikaciji, sem razdelila aplikacijo na dve aplikaciji vsaka na svojem portu v svojem image-u.
- Mato sem ugotovila da imam drugačen ime host mysql baze kot pri dockerju.
- Sedaj dela povezava z mqsql bazo samo vsakič prvo reče, da se ne more povezati, potem pa brez spremembe server poda dela.

# Docker del
### Splošno o nalogi

Naredila sem spletno aplikacijo v python flask, ki je razdeljena na dva dela. En del je za prejemanje post requestov od html strani za pisanje in prejemanje napisanega, drugi del je, zaradi manjše možnosti napake, za kreiranje in počiščenje baze.  
Aplikaciji imata bazo MySQL.  
Del za pisanje in prejemanje napisanega se izvaja na statični spletni strani, ki je hostana na nginx strežniku. 
Prav tako je multi-stage build z go aplikacijo, ki jo lahko vidiš na [localhost:5002/text_tukaj](http://localhost:5002/text_tukaj). Namesto `text_tukaj` vpiši karkoli. 

## Uporaba
Če želiš lahko uporabljaš docker. Premakni se v ustezno mapo ter zaženi spodnji ukaz, ki bo buildal in zagnal vse potrebno.

```bash
cd msi_k8s
docker-compose -f docker-compose.yml up --build
```
V brskalniku greš na [localhost:5000/](http://localhost:5000/) ali [localhost:5001/](http://localhost:5001/), kjer so splošna navodila.

Obvezno moraš pred prvo uporabo iti na [localhost:5001/create_db](http://localhost:5001/create_db), to je kot neka registracija. Vse nadaljo delo poteka na [localhost:8080](http://localhost:8080).

### Kreiranje baze
Greš na [localhost:5001/create_db](http://localhost:5001/create_db).  

![create](images/localhost5001_createdb.png) 

### Splošna navodila
Greš na [localhost:5000/](http://localhost:5000/) ali [localhost:5001/](http://localhost:5001/).    

![5000](images/localhost5000.png)  
![5001](images/localhost5001.png) 

### Spletna stran
Greš na [localhost:8080](http://localhost:8080).  

![8080](images/8080.png)  

Kjer lahko vpisuješ vse kar bi drugače lahko pozabil. To je tvoja online beležka. Na koncu klikni `Submit`.  

![write_1](images/write_before.png)  
![write_2](images/write_after.png)  

To kar si si zapisal lahko najdeš po njegovem id-ju oziroma njegovi zaporedni številki. 

![get_11](images/get_before.png)  
![get_12](images/get_before_2.png)  
![get_21](images/get_after.png)  
![get_22](images/get_after2.png)  

### Go stran
Če greš na [localhost:5002/monkeys and tigers](http://localhost:5002/monkeys_and_tigers). Namesto `monkeys and tigers` lahko vpišeš karkoli. 

![multi_stage](images/multi_stage.png)  


## Potencialni problemi s katerimi se lahko srečaš
Če delaš v virtualki ali pa daješ svoj računalnik v spanje, preden ponovno zaženeš ukaz `docker-compose -f docker-compose.yml up --build` zaženi `sudo service docker restart`, saj tako ponovno dns resolution znotra docker-ja pravilno dela. 
