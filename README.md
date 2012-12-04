Questo progetto nasce dall'idea di creare un albero di natale
connesso alla rete.

Si vorrebbe accendere e spegnere le luci tramite tweet, in modo 
che qualsiasi persona al mondo possa interagire con l'albero e 
vederne gli effetti attraverso una webcam.

Paraimpu da la possibilita' di fare una cosa simile, ma nel caso
in cui ci siano piu uscite ogni arduino viene gestito a se
(richiedendo ognuno una propria shield ethernet che, tra l'altro
occupa parecchi pin).

Con questo progetto invece utilizzo la seriale, attaccando tutti
gli arduini necessari ad un computer (possibilmente una board come
RaspberryPI, tra l'altro meno costoso di uno shield ethernet) e
la classe python gestisce tutto il pool di arduini come se fosse uno
solo, in maniera totalmente trasparente.

Comodo :)
