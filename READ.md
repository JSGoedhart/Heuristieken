Opdracht a:
- Greedy-algorithm: items gesorteerd op gewicht van hoog naar laag. Hoogste items in eerste spacecraft geplaatst, tot het item niet meer past. 
  Dan zoeken naar een item dat wel past, enz. Als er geen item meer past, door naar de volgende spacecraft. 

Opdracht b: 
- Hetzelfde greedy algorithm als bij a gebruikt, maar dan gesorteerd op m3 en begonnen met het vliegtuig met de grootste massa-capaciteit. 
  Hiermee een kloppende oplossing gevonden (zowel kg als m3). 
- Deze oplossing optimaliseren mbv simulated anealing oid.

kg en m3:
- Minimale wasted space: elk pakketje heeft een waarde die wordt gedefineerd als ((massa pakketje)/(massa-cap. 4 spacecrafts) + (volume 
  pakketje)/(vol. cap. 4 spacecrafts))*100. Ons doel is om de totale waarde van de overgebleven pakketjes te minimaliseren. 
  
Twee maal random een lijst uit de spacecraftlijst selecteren, uit deze twee lijsten een random element selecteren en deze met elkaar swappen. De swap goedkeuren wanneer er aan de kg- en m3-restricties vd spacecrafts is voldaan en wanneer de total_value van de leftover list niet kleiner wordt. Nadeel van deze methode: het aantal elementen in een lijst staat vast. 

Next step:
Random een spacecraft selecteren en een random aantal elementen uit deze lijst swappen met een random aantal elementen uit de leftoverlist. Er moet wel aan bovenstaande restricties worden voldaan. 
