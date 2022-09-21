rule ExampleRule1
{
       strings:
        $trig01 = "${jndi:ldap:/"
        $trig02 = "${jndi:http:/"
        
   condition:
      1 of ($tring*)

}