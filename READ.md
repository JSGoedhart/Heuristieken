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
