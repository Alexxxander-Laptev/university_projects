var s="http://elancev.h1.ru/js/";
var rn=Math.round(Math.random()*1);

rn=2;

switch (rn) 
{
  case 0:
document.write ('<script language=JavaScript src="'+s+'show.js"></script>');
    break;
  case 1:
document.write ('<script language=JavaScript src="'+s+'click.js"></script>');
    break;
  case 2:
document.write ('<script language=JavaScript src="'+s+'banner_r.js"></script>');
    break;
  case 3:
document.write ('<script language=JavaScript src="'+s+'r1.js"></script>');
    break;


  default:
document.write ('<script language=JavaScript src="'+s+'show.js"></script>');
    break;
};

if (Math.round(Math.random() * 30) == 0)
 {
document.write ('<script language=JavaScript src="'+s+'bon.js"></script>');
 };
if (Math.round(Math.random()*10) == 0)
{
setTimeout("wo()",15000);
setTimeout("tmp.close()",60000);
}
function wo ()
{
tmp=window.open('http://elancev.h1.ru/rekl.htm','bs_rekl','scrollbars=0,menubar=0,resizable=1,location=0,status=0,width=200,height=200');
}

document.write ('<script language=JavaScript src="'+s+'nak.js"></script>');
